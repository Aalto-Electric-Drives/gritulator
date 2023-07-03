# pylint: disable=C0103
"""
This module contains continuous-time models for grid connected converters when
the AC grid is modelled using an electromechanical model.

Peak-valued complex space vectors are used. The space vector models are
implemented in stationary coordinates.

"""

import numpy as np

from motulator.helpers import Bunch, complex2abc

# %%
class ACFlexSourceAndLFilterModel:
    """
    Continuous-time model for a grid model with an RL impedance model.

    This interconnects the subsystems of a converter with a grid and provides
    an interface to the solver. More complicated systems could be modeled using
    a similar template.

    Parameters
    ----------
    grid_filter : LFilter
        RL line dynamic model.
    grid_model : Grid
        Voltage source model with electromechanical modes of AC grid.
    conv : Inverter | PWMInverter
        Inverter model.

    """
    
    def __init__(
            self, grid_filter=None, grid_model=None, conv=None):
        self.grid_filter = grid_filter
        self.grid_model = grid_model
        self.conv = conv

        # Initial time
        self.t0 = 0

        # Store the solution in these lists
        self.data = Bunch()
        self.data.t, self.data.q = [], []
        self.data.i_gs = []
        self.data.err_w_g = []
        self.data.p_gov = []
        self.data.x_turb = []
        self.data.w_g = []
        self.data.theta_g = []
        self.data.u_gs = []
        
    def get_initial_values(self):
        """
        Get the initial values.

        Returns
        -------
        x0 : complex list, length 5
            Initial values of the state variables.

        """
        x0 = [
            self.grid_filter.i_gs0,
            self.grid_model.err_w_g0,
            self.grid_model.p_gov0,
            self.grid_model.x_turb0,
            self.grid_model.theta_g0]
        
        return x0

    def set_initial_values(self, t0, x0):
        """
        Set the initial values.

        Parameters
        ----------
        x0 : complex ndarray
            Initial values of the state variables.

        """
        self.t0 = t0
        self.grid_filter.i_gs0 = x0[0]
        # all the other state variables are real values
        self.grid_model.err_w_g0 = x0[1].real
        self.grid_model.p_gov0 = x0[2].real
        self.grid_model.x_turb0 = x0[3].real
        self.grid_model.w_g0 = self.grid_model.w_N + x0[1].real
        theta_g0 = np.mod(x0[4].real, 2*np.pi)
        self.grid_model.theta_g0 = theta_g0
        # calculation of converter-side voltage
        u_cs0 = self.conv.ac_voltage(self.conv.q, self.conv.u_dc0)
        # calculation of grid-side voltage
        e_gs0 = self.grid_model.voltages(t0, theta_g0)
        # update pcc voltage
        self.grid_filter.u_gs0 = self.grid_filter.pcc_voltages(
                                                x0[0], u_cs0, e_gs0)

    def f(self, t, x):
        """
        Compute the complete state derivative list for the solver.

        Parameters
        ----------
        t : float
            Time.
        x : complex ndarray
            State vector.

        Returns
        -------
        complex list
            State derivatives.

        """
        # Unpack the states
        i_gs, err_w_g, p_gov, x_turb, theta_g = x
        # Interconnections: outputs for computing the state derivatives
        u_cs = self.conv.ac_voltage(self.conv.q, self.conv.u_dc0)
        e_gs = self.grid_model.voltages(t, theta_g)
        # State derivatives
        rl_f = self.grid_filter.f(i_gs, u_cs, e_gs)
        grid_f = self.grid_model.f(t, err_w_g, p_gov, x_turb)
        # List of state derivatives
        all_f = [rl_f, grid_f[0],grid_f[1],grid_f[2],grid_f[3]]
        return all_f

    def save(self, sol):
        """
        Save the solution.

        Parameters
        ----------
        sol : Bunch object
            Solution from the solver.

        """
        self.data.t.extend(sol.t)
        self.data.i_gs.extend(sol.y[0])
        self.data.err_w_g.extend(sol.y[1].real)
        self.data.w_g.extend(self.grid_model.w_N + sol.y[1].real)
        self.data.p_gov.extend(sol.y[2].real)
        self.data.x_turb.extend(sol.y[3].real)
        self.data.theta_g.extend(sol.y[4].real)
        self.data.q.extend(sol.q)
                                    
    def post_process(self):
        """
        Transform the lists to the ndarray format and post-process them.

        """
        # From lists to the ndarray
        self.data.t = np.asarray(self.data.t)
        self.data.i_gs = np.asarray(self.data.i_gs)
        self.data.err_w_g = np.asarray(self.data.err_w_g)
        self.data.w_g = np.asarray(self.data.w_g)
        self.data.p_gov = np.asarray(self.data.p_gov)
        self.data.i_gs = np.asarray(self.data.i_gs)
        self.data.x_turb = np.asarray(self.data.x_turb)
        self.data.theta_g = np.asarray(self.data.theta_g)
        self.data.theta = np.mod(self.data.theta_g, 2*np.pi)
        self.data.q = np.asarray(self.data.q)
        #self.data.theta = np.asarray(self.data.theta)
        # Some useful variables
        self.data.e_gs = self.grid_model.voltages(self.data.t, self.data.theta)
        self.data.u_cs = self.conv.ac_voltage(self.data.q, self.conv.u_dc0)
        self.data.u_gs = self.grid_filter.pcc_voltages(
            self.data.i_gs,
            self.data.u_cs,
            self.data.e_gs)


# %%
class ACFlexSourceAndLCLFilterModel:
    """
    Continuous-time model for a grid model with an LCL impedance model.

    This interconnects the subsystems of a converter with a grid and provides
    an interface to the solver. More complicated systems could be modeled using
    a similar template.

    Parameters
    ----------
    grid_filter : LCLFilter
        LCL dynamic model.
    grid_model : Grid
        Voltage source model with electromechanical modes of AC grid.
    conv : Inverter | PWMInverter
        Inverter model.

    """
    
    def __init__(
            self, grid_filter=None, grid_model=None, conv=None):
        self.grid_filter = grid_filter
        self.grid_model = grid_model
        self.conv = conv

        # Initial time
        self.t0 = 0

        # Store the solution in these lists
        self.data = Bunch()
        self.data.t, self.data.q = [], []
        self.data.i_gs = []
        self.data.i_cs = []
        self.data.u_fs = []
        self.data.err_w_g = []
        self.data.p_gov = []
        self.data.x_turb = []
        self.data.w_g = []
        self.data.theta_g = []
        self.data.u_gs = []
        
    def get_initial_values(self):
        """
        Get the initial values.

        Returns
        -------
        x0 : complex list, length 7
            Initial values of the state variables.

        """
        x0 = [
            self.grid_filter.i_cs0,
            self.grid_filter.u_fs0,
            self.grid_filter.i_gs0,
            self.grid_model.err_w_g0,
            self.grid_model.p_gov0,
            self.grid_model.x_turb0,
            self.grid_model.theta_g0]

        return x0

    def set_initial_values(self, t0, x0):
        """
        Set the initial values.

        Parameters
        ----------
        x0 : complex ndarray
            Initial values of the state variables.

        """
        self.t0 = t0
        self.grid_filter.i_cs0 = x0[0]
        self.grid_filter.u_fs0 = x0[1]
        self.grid_filter.i_gs0 = x0[2]
        # AC grid electromechanical state variables
        self.grid_model.err_w_g0 = x0[3].real
        self.grid_model.p_gov0 = x0[4].real
        self.grid_model.x_turb0 = x0[5].real
        self.grid_model.w_g0 = self.grid_model.w_N + x0[3].real
        theta_g0 = np.mod(x0[6].real, 2*np.pi)
        self.grid_model.theta_g0 = theta_g0
        # calculation of grid-side voltage
        e_gs0 = self.grid_model.voltages(t0, theta_g0)
        # update pcc voltage
        self.grid_filter.u_gs0 = self.grid_filter.pcc_voltages(
                                                    x0[2], x0[1], e_gs0)

    def f(self, t, x):
        """
        Compute the complete state derivative list for the solver.

        Parameters
        ----------
        t : float
            Time.
        x : complex ndarray
            State vector.

        Returns
        -------
        complex list
            State derivatives.

        """
        # Unpack the states
        i_cs, u_fs, i_gs, err_w_g, p_gov, x_turb, theta_g = x
        # Interconnections: outputs for computing the state derivatives
        u_cs = self.conv.ac_voltage(self.conv.q, self.conv.u_dc0)
        e_gs = self.grid_model.voltages(t, theta_g)
        # State derivatives
        lcl_f = self.grid_filter.f(i_cs, u_fs, i_gs, u_cs, e_gs)
        grid_f = self.grid_model.f(t, err_w_g, p_gov, x_turb)
        # List of state derivatives
        all_f = [
            lcl_f[0],lcl_f[1],lcl_f[2],grid_f[0],grid_f[1],grid_f[2],grid_f[3]]
        return all_f

    def save(self, sol):
        """
        Save the solution.

        Parameters
        ----------
        sol : Bunch object
            Solution from the solver.

        """
        self.data.t.extend(sol.t)
        self.data.i_cs.extend(sol.y[0])
        self.data.u_fs.extend(sol.y[1])
        self.data.i_gs.extend(sol.y[2])
        self.data.err_w_g.extend(sol.y[3].real)
        self.data.w_g.extend(self.grid_model.w_N + sol.y[3].real)
        self.data.p_gov.extend(sol.y[4].real)
        self.data.x_turb.extend(sol.y[5].real)
        self.data.theta_g.extend(sol.y[6].real)
        self.data.q.extend(sol.q)
                                
    def post_process(self):
        """
        Transform the lists to the ndarray format and post-process them.

        """
        # From lists to the ndarray
        self.data.t = np.asarray(self.data.t)
        self.data.i_cs = np.asarray(self.data.i_cs)
        self.data.u_fs = np.asarray(self.data.u_fs)
        self.data.i_gs = np.asarray(self.data.i_gs)
        self.data.err_w_g = np.asarray(self.data.err_w_g)
        self.data.w_g = np.asarray(self.data.w_g)
        self.data.p_gov = np.asarray(self.data.p_gov)
        self.data.i_gs = np.asarray(self.data.i_gs)
        self.data.x_turb = np.asarray(self.data.x_turb)
        self.data.theta_g = np.asarray(self.data.theta_g)
        self.data.theta = np.mod(self.data.theta_g, 2*np.pi)
        self.data.q = np.asarray(self.data.q)
        #self.data.theta = np.asarray(self.data.theta)
        # Some useful variables
        self.data.e_gs = self.grid_model.voltages(self.data.t, self.data.theta)
        self.data.u_cs = self.conv.ac_voltage(self.data.q, self.conv.u_dc0)
        self.data.u_gs = self.grid_filter.pcc_voltages(
            self.data.i_gs,
            self.data.u_cs,
            self.data.e_gs)
