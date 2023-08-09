"""
Example simulation script: 10-kVA grid converter connected to a symmetrical
three-phase AC voltage source (grid) through an inductive filter.
    
The control system includes
    - Phase-Locked Loop (PLL) to synchronize with the grid;
    - Current reference generation;
    - Proportional-integral (PI) vector current controller
"""

# %%
# Import the packages.
import numpy as np
from motulator import model, control
from motulator import BaseValuesElectrical, plot_grid

# To check the computation time of the program
import time
start_time = time.time()

# %%
# Compute base values based on the nominal values (just for figures).
base_values = BaseValuesElectrical(
    U_nom=400, I_nom=14.5, f_nom=50.0, P_nom=10e3)


# %%
# Configure the system model
grid_filter = model.LFilter(L_f=10e-3, L_g=0, R_g=0)
grid_model = model.StiffSource(w_N=2*np.pi*50)
converter = model.Inverter(u_dc=650)

mdl = model.ac_grid.StiffSourceAndLFilterModel(
    grid_filter, grid_model, converter)

pars = control.gfl.GridFollowingCtrlPars(
            L_f=10e-3,
            R_f=0,
            f_sw = 5e3,
            T_s = 1/(10e3),
            I_max = 1.5*base_values.i,
            )
ctrl = control.gfl.GridFollowingCtrl(pars)


# %%

# Set the active and reactive power references
# that are inputs to the control system
ctrl.p_g_ref = lambda t: (t > .02)*(5e3)
ctrl.q_g_ref = lambda t: (t > .04)*(4e3)

# AC-voltage magnitude (to simulate voltage dips or short-circuits)
e_g_abs_var =  lambda t: np.sqrt(2/3)*400
mdl.grid_model.e_g_abs = e_g_abs_var # grid voltage magnitude

# Create the simulation object and simulate it
sim = model.Simulation(mdl, ctrl, pwm=False)
sim.simulate(t_stop = .1)

# Print the execution time
print('\nExecution time: {:.2f} s'.format((time.time() - start_time)))

# Plot results in SI or per unit values
plot_grid(sim, base=base_values,plot_pcc_voltage=True)
