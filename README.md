# *gritulator:* Grid Converter Simulator in Python

Introduction
------------
This open-source software includes simulation models for grid converter control and related electrical subsystems such as an inductive-capacitive-inductive (LCL) filter connected to an inductive-resistive grid. The electrical subsystem models are simulated in the continuous-time domain while the control methods run in discrete time. The default solver is the explicit Runge-Kutta method of order 5(4) from scipy.integrate.solve_ivp. A number of control methods are provided as examples. The documentation is available here:

https://aalto-electric-drives.github.io/gritulator/

Installation
------------
See the documentation:

https://aalto-electric-drives.github.io/gritulator/installation.html

Usage
-----
The grid-converter system, controllers, reference sequences etc. are configurable. As a starting point, example scripts and Jupyter notebooks can be found here:

https://aalto-electric-drives.github.io/gritulator/auto_examples/index.html

New system models and controllers can be developed using the existing ones as templates.


Acknowledgement
---------------
This project has been sponsored by ABB Oy and by the Research Council of Finland *Centre of Excellence in High-Speed Electromechanical Energy Conversion Systems*. The example control methods included in this repository are based on published algorithms (available in textbooks and scientific articles). They do not present any proprietary control software.
