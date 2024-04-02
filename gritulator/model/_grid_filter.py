"""
Grid and AC filter impedance models.

This module contains continuous-time models for subsystems comprising an AC 
filter and a grid impedance between the converter and grid voltage sources. The 
models are implemented with space vectors in stationary coordinates.

"""
import numpy as np
from gritulator._helpers import complex2abc


# %%
class LFilter:
    """
    Dynamic model for an inductive L filter and an inductive-resistive grid.

    An L filter and inductive-resistive grid impedance, between the converter and
    grid voltage sources, are modeled combining their inductances and series
    resistances in a state equation. The grid current is used as a state 
    variable. The point-of-common-coupling (PCC) voltage between the L filter 
    and the grid impedance is separately calculated.

    Parameters
    ----------
    L_f : float
        Filter inductance (H)
    R_f : float
        Filter series resistance (Ω)
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
        Compute the point-of-common-coupling voltage.
        
        This computes the point-of-common-coupling (PCC) voltage between the 
        L filter and grid impedance.
        
        Parameters
        ----------
        i_gs : complex
            Grid current (A).
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
    Dynamic model for an inductive-capacitive-inductive (LCL) filter and a grid.

    An LCL filter and inductive-resistive grid impedance, between the converter 
    and grid voltage sources, are modeled using converter-side current, capacitor 
    voltage and grid-side current of the LCL filter as state variables. Grid 
    inductance and resistance are included in the state equation of grid-side 
    current. The point-of-common-coupling (PCC) voltage between the LCL filter 
    and the grid impedance is separately calculated.

    Parameters
    ----------
    L_fc : float
        Converter-side LCL filter inductance (H)
    R_fc : float
        Converter-side series resistance (Ω)
    L_fg : float
        Grid-side LCL filter inductance (H)
    R_fg : float
        Grid-side series resistance (Ω)
    C_f : float
        LCL Filter capacitance (F)
    G_f : float
        Conductance of a resistance in parallel with the LCL filter capacitor (S)
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
        Compute the point-of-common-coupling voltage.
        
        This calculates point-of-common-coupling (PCC) voltage that is located 
        between the LCL filter and grid impedance.

        Parameters
        ----------
        i_gs : complex
            Grid current (A).
        u_fs : complex
            Capacitor voltage (V).
        e_gs : complex
            Grid voltage (V).

        Returns
        -------
        u_gs : complex
            Voltage at the point of common coupling (V).

        """
        # PCC voltage in alpha-beta coordinates
        u_gs = (self.L_fg*e_gs + self.L_g*u_fs + 
            (self.R_g*self.L_fg-self.R_fg*self.L_g)*i_gs)/(self.L_g+self.L_fg)
        
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
