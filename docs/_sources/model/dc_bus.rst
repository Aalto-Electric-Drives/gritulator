DC Bus
======

A dynamic model for a capacitive direct current (DC) bus of the converter is 
provided in :mod:`gritulator.model.dc_bus._dc_bus`. An external current source 
is feeding the DC bus that is modeled considering an equivalent circuit 
comprising a parallel connected DC bus capacitor and resitor. The model is 
implemented as

.. math::
   \frac{\mathrm{d}\boldsymbol{u}_\mathrm{dc}}{\mathrm{d} t} 
   = \frac{1}{C_\mathrm{dc}}(i_\mathrm{ext} 
   - i_\mathrm{dc} - G_\mathrm{dc}u_\mathrm{dc})
   :label: DC_bus_model

where :math:`u_\mathrm{dc}` is the DC bus voltage, :math:`i_\mathrm{ext}` is the 
external DC current, :math:`i_\mathrm{dc}` is the converter DC current, 
:math:`C_\mathrm{dc}` is the DC bus capacitance, and :math:`G_\mathrm{dc}` is 
the conductance of the parallel resistor. The converter DC current is calculated 
from the converter phase currents and switching states as 

.. math::
   i_\mathrm{dc} = q_\mathrm{a} i_\mathrm{a} + q_\mathrm{b} i_\mathrm{b}
   + q_\mathrm{c} i_\mathrm{c}
   :label: DC_current

