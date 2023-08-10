"""
Grid and converter filter impedance models.

This module contains continuous-time models for the AC impedance between the 
converter output and the AC grid. In this module, all space vectors are in
stationary coordinates.

"""
import numpy as np
from gritulator._helpers import complex2abc


# %%
class LFilter:
    """
    Inductive-resistive filter dynamic model. 

    An inductive filter model is built using a simple inductance model where
    the two output voltages are imposed and the current can be calculated using
    dynamic equations. This model includes a model for an inductive-resistive
    impedance of the grid combined with the L-filter model. 

    Parameters
    ----------
    L_f : float
        Filter inductance (H)
    R_f : float
        Filter resistance (Ω)
    L_g : float
        Grid inductance (H)
    R_g : float
        Grid resistance (Ω)

    """
    def __init__(self, U_gN=400*np.sqrt(2/3), L_f = 6e-3, R_f=0, L_g=0, R_g=0):
        self.L_f = L_f
        self.R_f = R_f
        self.L_g = L_g
        self.R_g = R_g
        # Storing the PCC voltage value
        self.u_gs0 = U_gN + 0j
        # Initial values
        self.i_gs0 = 0j


    def pcc_voltages(self, i_gs, u_cs, e_gs):
        """
        Compute the point of common coupling voltage.
        
        point of common coupling (PCC) is located at the other end of the
        converter output filter.
        
        Parameters
        ----------
        i_gs : complex
            Line current (A).
        u_cs : complex
            Converter voltage (V).
        e_gs : complex
            Grid voltage (V).

        Returns
        -------
        u_gs : complex
            Voltage at the point of common coupling (V).

        """

        # PCC voltage in stationary coordinates
        u_gs = (self.L_g*u_cs + self.L_f*e_gs + 
            (self.R_g*self.L_f - self.R_f*self.L_g)*i_gs)/(self.L_g+self.L_f)
        
        return u_gs
    
    
    def f(self, i_gs, u_cs, e_gs):
        # pylint: disable=R0913
        """
        Compute the state derivatives.

        Parameters
        ----------
        i_gs : complex
            Line current (A).
        u_cs : complex
            Converter-side voltage (V).
        e_gs : complex
            Grid-side voltage (V).

        Returns
        -------
        complex list, length 1
            Time derivative of the complex state vector, [di_gs]

        """
        # Calculation of the total impedance
        L_t = self.L_f + self.L_g
        R_t = self.R_f + self.R_g
        di_gs = (u_cs - e_gs - R_t*i_gs)/L_t
        return di_gs

    def meas_currents(self):
        """
        Measure the phase currents at the end of the sampling period.

        Returns
        -------
        i_g_abc : 3-tuple of floats
            Phase currents (A).

        """
        # Line current space vector in stationary coordinates
        i_g_abc = complex2abc(self.i_gs0)
        return i_g_abc
    
    
    def meas_pcc_voltage(self):
        """
        Measure the PCC voltages at the end of the sampling period.

        Returns
        -------
        u_g_abc : 3-tuple of floats
            Phase voltage at the point of common coupling (V).

        """  
        # PCC voltage space vector in stationary coordinates
        u_g_abc = complex2abc(self.u_gs0)
        return u_g_abc
    
    
    # %%
class LCLFilter:
    """
    Inductive-capacitive-inductive (LCL) filter dynamic model. 

    An LCL-type grid model is built using inductive and capacitive dynamic
    models. The two output voltages are imposed and the grid-side current, the
    converter-side current and the capacitance voltage can be calculated using
    dynamic equations. This model includes a model for an inductive-resistive
    impedance of the grid combined with the LCL-filter model.

    Parameters
    ----------
    L_fc : float
        Converter-side filter inductance (H)
    R_fc : float
        Converter-side filter resistance (Ω)
    L_fg : float
        Grid-side filter inductance (H)
    R_fg : float
        Grid-side filter resistance (Ω)
    C_f : float
        Filter capacitance (F)
    G_f : float
        LCL filter conductance (S)
    L_g : float
        Grid inductance (H)
    R_g : float
        Grid resistance (Ω)


    """
    def __init__(
            self, U_gN=400*np.sqrt(2/3), L_fc=6e-3, R_fc=0, L_fg=3e-3,
            R_fg=0, C_f=10e-6, G_f=0, L_g=0, R_g=0):
        self.L_fc = L_fc
        self.R_fc = R_fc
        self.L_fg = L_fg
        self.R_fg = R_fg
        self.C_f = C_f
        self.G_f = G_f
        self.L_g = L_g
        self.R_g = R_g
        # Storing useful variables
        self.u_gs0 = U_gN + 0j
        # Initial values
        self.i_cs0 = 0j
        self.i_gs0 = 0j
        self.u_fs0 = U_gN + 0j


    def pcc_voltages(self, i_gs, u_fs, e_gs):
        """
        Compute the point of common coupling voltage.
        
        point of common coupling (PCC) is located at the other end of the
        converter output filter.

        Parameters
        ----------
        i_gs : complex
            Grid-side line current (A).
        u_fs : complex
            Capacitance voltage (V).
        e_gs : complex
            Grid-side voltage (V).

        Returns
        -------
        u_gs : complex
            Voltage at the point of common coupling (V).

        """
        # calculation of the voltage-related term
        v_tu = e_gs*((self.L_g/(self.L_g+self.L_fg))*u_fs + 
            self.L_fg/(self.L_g+self.L_fg))
        # calculation of the current-related term
        v_ti = i_gs*((self.R_g*self.L_fg - self.R_fg*self.L_g)/
                 (self.L_g+self.L_fg))
        # PCC voltage in alpha-beta coordinates
        u_gs = v_tu + v_ti
        return u_gs
    
    def f(self, i_cs, u_fs, i_gs, u_cs, e_gs):
        # pylint: disable=R0913
        """
        Compute the state derivatives.

        Parameters
        ----------
        i_cs : complex
            Converter line current (A).
        u_fs : complex
            Capacitance voltage (V).
        i_gs : complex
            Grid line current (A).
        u_cs : complex
            Converter voltage (V).
        e_gs : complex
            Grid voltage (V).

        Returns
        -------
        complex list, length 3
            Time derivative of the complex state vector, [di_cs, du_fs, di_gs]

        """
        # Converter-side dynamics
        di_cs = (u_cs - u_fs - self.R_fc*i_cs)/self.L_fc
        # Capacitance dynamics
        du_fs = (i_cs - i_gs - self.G_f*u_fs)/self.C_f
        # Calculation of the total grid-side impedance
        L_t = self.L_fg + self.L_g
        R_t = self.R_fg + self.R_g
        di_gs = (u_fs - e_gs - R_t*i_gs)/L_t
        return [di_cs, du_fs, di_gs]

    def meas_currents(self):
        """
        Measure the converter currents at the end of the sampling period.

        Returns
        -------
        i_c_abc : 3-tuple of floats
            Phase currents.

        """
        # Line current space vector in stationary coordinates
        i_c_abc = complex2abc(self.i_cs0)
        return i_c_abc
    
    def meas_grid_currents(self):
        """
        Measure the grid currents at the end of the sampling period.

        Returns
        -------
        i_g_abc : 3-tuple of floats
            Phase currents (A).

        """
        # Line current space vector in stationary coordinates
        i_g_abc = complex2abc(self.i_gs0)
        return i_g_abc

    def meas_cap_voltage(self):
        """
        Measure the capacitor voltages at the end of the sampling period.

        Returns
        -------
        u_f_abc : 3-tuple of floats
            Phase voltage through the capacitance of the LCL filter (V).

        """  
        # Capacitor voltage space vector in stationary coordinates
        u_f_abc = complex2abc(self.u_fs0)  # + noise + offset ...
        return u_f_abc
    
    def meas_pcc_voltage(self):
        """
        Measure the PCC voltages at the end of the sampling period.

        Returns
        -------
        u_g_abc : 3-tuple of floats
            Phase voltage at the point of common coupling (V).

        """  
        # PCC voltage space vector in stationary coordinates
        u_g_abc = complex2abc(self.u_gs0)
        return u_g_abc
