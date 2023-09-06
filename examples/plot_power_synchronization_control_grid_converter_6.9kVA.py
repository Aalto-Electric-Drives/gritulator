"""
Example simulation script: 6.9-kVA grid-forming controlled converter connected
to a perfect AC voltage source (grid) with an L filter.
    
The control system includes:
    - Power synchronization loop;
    - Inner current controller used to damp the current oscillations.
    - DC-bus controller (optional)
"""


# %%
# Import the packages.
import numpy as np
from gritulator import model, control
from gritulator import BaseValuesElectrical, plot_grid

# To check the computation time of the program
import time
start_time = time.time()

# %%
# Compute base values based on the nominal values (just for figures).
base_values = BaseValuesElectrical(
    U_nom=400, I_nom=10, f_nom=50.0, P_nom=6.9e3)


# %%
# Configure the system model (grid model)
grid_filter = model.LFilter(L_f = 8e-3, L_g=65.8e-3, R_g=0)
grid_model = model.StiffSource(w_N=2*np.pi*50)
conv = model.Inverter(u_dc=650)

mdl = model.ac_grid.StiffSourceAndLFilterModel(grid_filter, grid_model, conv)

pars = control.grid_forming.PSCCtrlPars(
        L_f=8e-3,
        R_f=0,
        f_sw = 4e3,
        T_s = 1/(8e3),
        on_rf=False,
        on_v_dc=False,
        i_max = 1.5*base_values.i,
        w_0_cc = 2*np.pi*5,
        R_a = .2*base_values.Z)
ctrl = control.grid_forming.PSCCtrl(pars)

# %%

# Set the active power reference
ctrl.p_g_ref = lambda t: ((t > .2)*(2.3e3) + (t > .5)*(2.3e3) + 
    (t > .8)*(2.3e3) - (t > 1.2)*(6.9e3))

# AC-voltage magnitude (to simulate voltage dips or short-circuits)
e_g_abs_var =  lambda t: np.sqrt(2/3)*400
mdl.grid_model.e_g_abs = e_g_abs_var # grid voltage magnitude

# Create the simulation object and simulate it
sim = model.Simulation(mdl, ctrl, pwm=False)
sim.simulate(t_stop = 1.5)

# Print the execution time
print('\nExecution time: {:.2f} s'.format((time.time() - start_time)))

# %%
# Plot results in SI or per unit values.

plot_grid(sim, base=base_values, plot_pcc_voltage=True)
