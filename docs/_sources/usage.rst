Usage
=====
After :doc:`installation`, gritulator can be used by creating a continuous-time 
system model, a discrete-time controller, and a simulation object, as shown 
below. A 10-kW grid-following converter is used as an example.

.. code:: bash

   from gritulator import model, control
   from gritulator import BaseValuesElectrical, plot_grid

   # Compute base values based on the nominal voltage, current, frequency and power
   base_values = BaseValuesElectrical(
      U_nom=400, I_nom=14.5, f_nom=50.0, P_nom=10e3)

   # Create the continous-time system model for a grid coverter
   grid_filter = model.LFilter(L_f=0.15*base_values.L, L_g=0, R_g=0)
   grid_voltage_source = model.StiffSource(w_N=base_values.w)
   converter = model.Inverter(u_dc=650)
   mdl = model.ac_grid.StiffSourceAndLFilterModel(
      grid_filter, grid_voltage_source, converter)

   # Configure a discrete-time control system.
   pars = control.grid_following.GridFollowingCtrlPars(
               L_f=0.15*base_values.L, f_sw = 5e3, T_s = 1/(10e3), 
               i_max = 1.5*base_values.i)
   ctrl = control.grid_following.GridFollowingCtrl(pars)

   # Set the active and reactive power references to change stepwise at t = 0.02 s
   # and t = 0.06 s, respectively
   ctrl.p_g_ref = lambda t: (t > .02)*1.0*base_values.p
   ctrl.q_g_ref = lambda t: (t > .06)*0.5*base_values.p

   # Set grid voltage magnitude
   mdl.grid_model.e_g_abs = lambda t: base_values.u

   # Create the simulation object, simulate, and plot results.
   sim = model.Simulation(mdl, ctrl, pwm=False)
   sim.simulate(t_stop = .1)
   plot_grid(sim, base=base_values)


The :doc:`auto_examples/index` folder includes a variety of different example 
scripts to run the simulation. System and controller configurations can be 
changed as shown in the examples. Furthermore, new features can be added by 
modifying the source code.