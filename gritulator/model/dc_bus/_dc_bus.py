"""
Dynamic model of a DC bus.

A DC bus between an external current source or sink and a converter is modeled 
considering an equivalent circuit comprising a capacitor and parallel resistor.
"""

from gritulator._helpers import complex2abc

# %%
class DCBus:
    """
    DC bus model

    This model is used to compute the capacitive DC bus dynamics. Dynamics are 
    modeled with an equivalent circuit comprising a capacitor and its parallel 
    resistor that is parametrized using a conductance. The capacitor voltage is 
    used as a state variable.

    Parameters
    ----------
    C_dc : float
        DC-bus capacitance (F)
    G_dc : float
        Parallel conductance of the capacitor (S)
    i_ext : function
        External DC current, seen as disturbance, `i_ext(t)`.

    """
    def __init__(self, C_dc=1e-3, G_dc=0, i_ext=lambda t: 0, u_dc0 = 650):
        self.C_dc = C_dc
        self.G_dc = G_dc
        self.i_ext = i_ext
        # Initial values
        self.u_dc0 = u_dc0
    
    @staticmethod
    def dc_current(i_c_abc, q):
        """
        Compute the converter DC current from the switching states and phase 
        currents.
    
        Parameters
        ----------
        i_c_abc : ndarray, shape (3,)
            Phase currents (A).
        q : complex ndarray, shape (3,)
            Switching state vectors corresponding to the switching instants.
            For example, the switching state q[1] is applied at the interval
            t_n_sw[1].
    
        Returns
        -------
        i_dc: float
            Converter DC current (A)
    
        """
        # Duty ratio back into three-phase ratios
        q_abc = complex2abc(q)
        # Dot product
        i_dc = q_abc[0]*i_c_abc[0] + q_abc[1]*i_c_abc[1] + q_abc[2]*i_c_abc[2]
        return i_dc
    
    def f(self, t, u_dc, i_dc):
        """
        Compute the state derivatives.

        Parameters
        ----------
        t : float
            Time (s)
        u_dc: float
            DC bus voltage (V)
        i_dc : float
            Converter DC current (A)
        Returns
        -------
        double list, length 1
                Time derivative of the complex state vector, [du_dc]

        """
        # State derivative
        du_dc = (self.i_ext(t) - i_dc - self.G_dc*u_dc)/self.C_dc
        return du_dc

    def meas_dc_voltage(self):
        """
        Measure the DC bus voltage at the end of the sampling period.
    
        Returns
        -------
        u_dc: float
            DC bus voltage (V)
    
        """
        return self.u_dc0
