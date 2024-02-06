*gritulator:* Grid Converter Simulator in Python
================================================

This open-source software includes simulation models for grid converter control 
and related electrical subsystems such as an inductive-capacitive-inductive 
(LCL) filter connected to an inductive-resistive grid. The electrical subsystem 
models are simulated in the continuous-time domain while the control methods run 
in discrete time. The default solver is the explicit Runge-Kutta method of order 
5(4) from `scipy.integrate.solve_ivp`_. A number of control methods are provided 
as examples. The example methods aim to be simple yet feasible. 

.. _scipy.integrate.solve_ivp: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

.. toctree::
   :titlesonly:
   :caption: Getting Started
   :name: getting_started
   :maxdepth: 1

   installation
   usage
   API Reference <autoapi/gritulator/index>

.. toctree::
   :titlesonly:
   :caption: System Models
   :name: models
   :maxdepth: 2

   model/index

.. toctree::
   :titlesonly:
   :caption: Control Methods
   :name: controllers
   :maxdepth: 1

   auto_examples/index
   control/design_notes
