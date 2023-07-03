# pylint: disable=C0103
'''
This module contains Power Synchronization Control (PSC) for grid converters

This control scheme is based on the updated version presented in [1]. More info
can be found in this reference.

[1] Reference-feedforward power-synchronization control, L Harnefors,
FMM Rahman, M Hinkkanen, M Routimo - IEEE Transactions on Power Electronics,
2020.

'''
# %%
from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
import numpy as np
from motulator.helpers import Bunch
from motulator.helpers import abc2complex
from motulator.control.common import Ctrl, PWM

# %%
@dataclass
class PSCtrlPars:
    """
    power synchronization control(PSC-)based parameters.

    """
    # pylint: disable=too-many-instance-attributes
    # General control parameters
    p_g_ref: Callable[[float], float] = field(
        repr=False, default=lambda t: (t > .2)*(5e3)) # active power reference
    q_g_ref: Callable[[float], float] = field(
        repr=False, default=lambda t: 0) # reactive power reference
    w_c_ref: Callable[[float], float] = field(
        repr=False, default=lambda t: 2*np.pi*50) # frequency reference
    v_ref: Callable[[float], float] = field(
        repr=False, default=lambda t: np.sqrt(2/3)*400) # voltage magnitude ref
    u_dc_ref: Callable[[float], float] = field(
        repr=False, default=lambda t: 650) # DC voltage reference, only used if
                                    # the dc voltage control mode is activated.
    T_s: float = 1/(16e3) #sampling time of the controller.
    u_g_N: float = np.sqrt(2/3)*400  # PCC voltage, in volts.
    w_g: float = 2*np.pi*50 # grid frequency, in Hz
    f_sw: float = 8e3 # switching frequency, in Hz.
    
    # Control of the converter voltage or the PCC voltage
    on_u_g: bool = 0 # put 1 to control PCC voltage. 0 if not.
    
    # Power synchronization loop control parameters
    R_a: float = 4.6 # Damping resistance, in Ohm
    k_scal: float = 3/2 # scaling ratio of the abc/dq transformation
    on_rf: bool = 1 # Boolean: 1 to activate reference-feedforward. 0 is PSC
    
    # Low pass filter for the current controller of PSC
    w_0_cc: float = 2*np.pi*5 # filter undamped natural frequency, in rad/s.
    K_cc: float = 1 # low pass filter gain
    I_max: float = 20 # maximum current modulus in A
    
    # DC-voltage controller
    on_v_dc: bool = 0 # put 1 to activate dc voltage controller. 0 is p-mode
    zeta_dc: float = 1 # damping ratio
    p_max: float = 10e3 # maximum power reference, in W.
    w_0_dc: float = 2*np.pi*30 # controller undamped natural frequency, in rad/s.
    
    # Passive component parameter estimates
    L_f: float = 10e-3 # filter inductance, in H.
    R_f: float = 0 # filter resistance, in Ohm.
    C_dc: float = 1e-3 # DC bus capacitance, in F.


# %%
class PSCtrl(Ctrl):
    """
    Grid forming control (PSC) with the power synchronization loop and a current
    loop implemented as in [1].
    
    Can be combined with the DC-voltage controller as well.

    Parameters
    ----------
    pars : PSCtrlPars
        Control parameters.

    """

    # pylint: disable=too-many-instance-attributes, too-few-public-methods
    def __init__(self, pars):
        super().__init__()
        self.t = 0
        self.T_s = pars.T_s
        # Instantiate classes
        self.pwm = PWM(pars)
        self.power_calc = PowerCalc(pars)
        self.current_ctrl = CurrentCtrl(pars)
        self.power_synch = PowerSynch(pars)
        self.dc_voltage_control = DCVoltageControl(pars)
        # Parameters
        self.u_g_N = pars.u_g_N
        self.w_g = pars.w_g
        self.f_sw = pars.f_sw
        # Activation of reference feedforward action
        self.on_rf = pars.on_rf
        # Activation of DC-voltage controller
        self.on_v_dc = pars.on_v_dc
        # References sent from the user
        self.p_g_ref = pars.p_g_ref
        self.q_g_ref = pars.q_g_ref
        self.w_c_ref = pars.w_c_ref
        self.v_ref = pars.v_ref
        self.u_dc_ref = pars.u_dc_ref
        # If the pcc voltage should be used as controlled voltage
        # States
        self.theta_psc = 0 # Integrator state of the phase angle estimation
        self.u_c_ref_lim = pars.u_g_N + 1j*0
        ####
        self.desc = pars.__repr__()
        
 
    def __call__(self, mdl):
        """
        Run the main control loop.

        Parameters
        ----------
        mdl : GridCompleteModel / ACDCGridCompleteModel
            Continuous-time model of  a grid model with an RL impedance for
            getting the feedback signals.

        Returns
        -------
        T_s : float
            Sampling period.
        d_abc_ref : ndarray, shape (3,)
            Duty ratio references.

        """
        # Measure the feedback signals
        i_c_abc = mdl.grid_filter.meas_currents()
        u_dc = mdl.conv.meas_dc_voltage()
        u_g_abc = mdl.grid_filter.meas_pcc_voltage()
        
        # Calculation of PCC voltage in synchronous frame
        u_g = np.exp(-1j*self.theta_psc)*abc2complex(u_g_abc)
        
        # Define the active and reactive power references at the given time
        u_dc_ref = self.u_dc_ref(self.t)
        if self.on_v_dc:
            e_dc, p_dc_ref, p_dc_ref_lim =self.dc_voltage_control.output(
                u_dc_ref,
                u_dc)
            p_g_ref = p_dc_ref_lim
            q_g_ref = self.q_g_ref(self.t)
        else:
            p_g_ref = self.p_g_ref(self.t)
            q_g_ref = self.q_g_ref(self.t)
            
        # Define the user-defined voltage magnitude and frequency references
        w_c_ref = self.w_c_ref(self.t)
        v_ref = self.v_ref(self.t)
        
        # Transform the measured current in dq frame
        i_c = np.exp(-1j*self.theta_psc)*abc2complex(i_c_abc)
        
        # Calculation of active and reactive powers:
        p_calc, __ = self.power_calc.output(i_c, self.u_c_ref_lim)
        # remark: there is no need to use u_g when self.on_u_g = 1 if we 
        # make the assumption that the output filter is lossless.
        
        # Synchronization through active power variations
        w_c, theta_c = self.power_synch.output(p_calc, p_g_ref, w_c_ref)

        # Voltage reference in synchronous coordinates
        u_c_ref, i_c_ref, i_c_filt = self.current_ctrl.output(
                                        i_c,p_g_ref,v_ref,w_c_ref)
        
        # Compute the PWM
        d_abc_ref, u_c_ref_lim = self.pwm.output(u_c_ref, u_dc,
                                           self.theta_psc, self.w_g)

        # Data logging
        data = Bunch(
            w_c = w_c, theta_c = self.theta_psc, v_ref = v_ref,
            w_c_ref = w_c_ref, u_c_ref = u_c_ref, u_c_ref_lim = u_c_ref_lim,
            i_c = i_c, d_abc_ref = d_abc_ref, i_c_ref = i_c_ref,
            u_dc = u_dc, t = self.t, p_g_ref = p_g_ref, u_dc_ref = u_dc_ref,
            q_g_ref = q_g_ref, u_g = u_g
                     )
        self.save(data)

        # Update the states
        self.u_c_ref_lim = u_c_ref_lim
        self.update_clock(self.T_s)
        self.pwm.update(u_c_ref_lim)
        self.power_synch.update(theta_c)
        self.theta_psc = theta_c
        self.current_ctrl.update(i_c, i_c_filt)
        if self.on_v_dc == 1:
            self.dc_voltage_control.update(e_dc, p_dc_ref, p_dc_ref_lim)
        
        return self.T_s, d_abc_ref
    

    def __repr__(self):
        return self.desc


        
# %%        
class PowerCalc:
    
    """
    Internal controller power calculator
    
    This class is used to calculate the active and reactive powers at the
    converter outputs by using voltage and current in complex form
    used in the control.
    
    """
    
    def __init__(self, pars):
         
        """
        Parameters
        ----------
        pars : PSCtrlPars
            Control parameters.
    
        """
        self.k_scal = pars.k_scal

    
    def output(self, i_c, u_c):
    
        """
        Power calculation.
        
        Parameters
        ----------
        
        i_c : complex
            current in dq frame (A).
        u_c : complex
            voltage in dq frame (V).
        
    
        Returns
        -------
        p_calc : float
            calculated active power
        q_calc : float
            calculated reactive power
            
        """ 
    
        # Calculation of active and reactive powers:
        p_calc = self.k_scal*np.real(u_c*np.conj(i_c))
        q_calc = self.k_scal*np.imag(u_c*np.conj(i_c))
        
        return p_calc, q_calc


# %%
class PowerSynch:
    
    """
    Active power/frequency synchronizing loop.
    
    This control loop is used to synchronize with the grid using the active
    power variations compared to the active power reference.

    """
        
        
    def __init__(self, pars):
         
        """
        Parameters
        ----------
        pars : PSCtrlPars
           Control parameters.
     
        """
        # controller parameters
        self.T_s = pars.T_s
        self.k_p_psc = pars.w_g*pars.R_a/(pars.k_scal*pars.u_g_N*pars.u_g_N)
        # Initial states
        self.theta_p = 0
    
            
    def output(self, p_calc, p_g_ref, w_c_ref):
        
        """
        Compute the estimated frequency and phase angle using the PSC
    
        Parameters
        ----------
        p_calc : float
            calculated active power at the converter outputs (W).
        pg_ref : float
            active power reference (W).
        w_c_ref : float
            frequency reference (rad/s).
    
        Returns
        -------
        w_c : float
            estimated converter frequency (rad/s).
        theta_c : float
            estimated converter phase angle (rad).

        """
        
        # Calculation of power droop
        dp = p_g_ref - p_calc
        w_c = w_c_ref + (self.k_p_psc)*dp
                
        # Estimated phase angle
        theta_c = self.theta_p + self.T_s*w_c
        theta_c = np.mod(theta_c, 2*np.pi)    # Limit to [0, 2*pi]
        
        return w_c, theta_c
    
        
    def update(self, theta_c):
        """
        Update the integral state.
    
        Parameters
        ----------
        theta_c : float
            estimated converter phase angle (rad).

        """

        # Update the grid-voltage angle state
        self.theta_p = theta_c
        
        
# %%
class CurrentCtrl:
    
    """
    PSC-based current controller.
    
    PSC makes the converter operate as a voltage source, however, this block
    is used to damp the current oscillations and limit the current
    flowing through the converter to avoid physical damages of the device.
    
    It is important to note that this block uses P-type controller and can thus
    encounter steady-state error when the current reference is saturated.
        
    """
        
        
    def __init__(self, pars):
         
        """
        Parameters
        ----------
        pars : PSCtrlPars
            Control parameters.
    
        """
        # controller parameters
        self.T_s = pars.T_s
        self.R_a = pars.R_a
        self.L_f = pars.L_f
        self.w_0_cc = pars.w_0_cc
        self.K_cc = pars.K_cc
        self.k_scal= pars.k_scal
        # activation/deactivation of reference feedforward action
        self.on_rf = pars.on_rf
        # activation/deactivation of PCC voltage control option
        self.on_u_g = pars.on_u_g
        # Calculated maximum current in A
        self.I_max = pars.I_max
        #initial states
        self.i_c_filt =0j 
    
            
    def output(self, i_c, p_g_ref, v_ref, w_c_ref):
        
        """
        Compute the converter voltage reference signal
    
        Parameters
        ----------
        i_c : complex
            converter current in dq frame (A).
        p_g_ref : float
            active power reference (W).
        v_ref : float
            converter voltage magnitude reference (V).
        w_c_ref : float
            converter frequency reference (rad/s).
    
        Returns
        -------
        u_c_ref : complex
            converter voltage reference (V).
        i_c_ref : complex
            converter current reference in dq frame (A).
        i_c_filt : complex
            low-pass filtered converter current in dq frame (A).

        """

        # Low pass filter for the current:
        i_c_filt = self.i_c_filt
        
        # Definition of the voltage reference in complex form
        v_c_ref = v_ref + 1j*0
        
        # Use of reference feedforward for d-axis current
        if self.on_rf:
            i_c_ref = p_g_ref/(v_ref*self.k_scal) + 1j*np.imag(i_c_filt)
        else:
            i_c_ref = i_c_filt
            
        # Calculation of the modulus of current reference
        i_abs = np.abs(i_c_ref)
        i_c_d_ref = np.real(i_c_ref)
        i_c_q_ref = np.imag(i_c_ref)
    
        # And current limitation algorithm
        if i_abs > 0:
            i_ratio = self.I_max/i_abs
            i_c_d_ref = np.sign(i_c_d_ref)*np.min(
                [i_ratio*np.abs(i_c_d_ref),np.abs(i_c_d_ref)])
            i_c_q_ref = np.sign(i_c_q_ref)*np.min(
                [i_ratio*np.abs(i_c_q_ref),np.abs(i_c_q_ref)])
            i_c_ref = i_c_d_ref + 1j*i_c_q_ref
        
                
        # Calculation of converter voltage output (reference sent to PWM)
        u_c_ref = (v_c_ref + self.R_a*(i_c_ref - i_c) +
           self.on_u_g*1j*self.L_f*w_c_ref*i_c)
        
        
        return u_c_ref, i_c_ref, i_c_filt
    
        
    def update(self, i_c, i_c_filt):
        """
        Update the integral state.
    
        Parameters
        ----------
        i_c : complex
            converter current in dq frame (A).
        i_c_filt : complex
            low-pass filtered converter current in dq frame (A).
    
        """

        # Update the current low pass filer integrator
        self.i_c_filt = (1 - self.T_s*self.w_0_cc)*i_c_filt + (
            self.K_cc*self.T_s*self.w_0_cc*i_c)

# %%        
class DCVoltageControl:
    
    """
    DC voltage controller
    
    This class is used to generate the active power reference for the converter
    controller to ensure that the DC voltage is regulated.
    
    """
    
    def __init__(self, pars):
         
        """
        Parameters
        ----------
        pars : GridFollowingCtrlPars
            Control parameters.
    
        """
        self.T_s = pars.T_s
        self.w_0_dc = pars.w_0_dc
        self.zeta_dc = pars.zeta_dc
        self.k_p_dc = 2*pars.zeta_dc*pars.w_0_dc
        self.k_i_dc = pars.w_0_dc*pars.w_0_dc
        self.C_dc = pars.C_dc
        # Saturation of power reference
        self.p_max = pars.p_max
        self.p_g_i = 0 # integrator state of the controller
    
    def output(self, u_dc_ref, u_dc):
        
        """
        Compute the active power reference sent to the converter control system
        to regulate the DC-bus voltage.
    
        Parameters
        ----------
        u_dc_ref : float
            DC-bus voltage reference
        u_dc : float
            DC-bus voltage
    
        Returns
        -------

        err_dc: float
            DC capacitance energy error signal
        p_dc_ref: float
            power reference based on DC voltage controller (W)
        p_dc_ref_lim: float
            saturated power reference based on DC voltage controller (W)

        """

        # Compute the error signal (the capacitor energy)
        err_dc = 0.5*self.C_dc*(u_dc_ref*u_dc_ref - u_dc*u_dc)

        # PI controller
        p_dc_ref = -self.k_p_dc*err_dc - self.p_g_i
        
        
        # Limit the output reference
        p_dc_ref_lim = p_dc_ref
        if p_dc_ref_lim > self.p_max:
            p_dc_ref_lim = self.p_max
        elif p_dc_ref_lim < -self.p_max:
            p_dc_ref_lim = -self.p_max
           
        
        return err_dc, p_dc_ref, p_dc_ref_lim
    
        
    def update(self, err_dc, p_dc_ref, p_dc_ref_lim):
        """
        Update the state of the DC-voltage controller with anti-windup.

        Parameters
        ----------
        err_dc: float
            DC capacitance energy error signal
        p_dc_ref: float
            power reference based on DC voltage controller
        p_dc_ref_lim: float
            saturated power reference based on DC voltage controller
        
        """
        # Update the integrator state (the last term is antiwindup)
        self.p_g_i = (self.p_g_i + self.T_s*self.k_i_dc*(err_dc +
            (p_dc_ref_lim - p_dc_ref)/self.k_p_dc))
