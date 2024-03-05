AC Filter and Grid Impedance
============================

This document describes continuous-time alternating current (AC) filter and 
grid-impedance models. 

Space Vectors
-------------


The models apply peak-valued complex space vectors, marked with boldface in the 
following equations. As an example, the space vector of the converter current is

.. math::
	\boldsymbol{i}^\mathrm{s}_\mathrm{c} 
   = \frac{2}{3}\left(i_\mathrm{a} + i_\mathrm{b}\mathrm{e}^{\mathrm{j}2\pi/3} 
   + i_\mathrm{c}\mathrm{e}^{\mathrm{j} 4\pi/3}\right) 
   :label: space_vector

where :math:`i_\mathrm{a}`, :math:`i_\mathrm{b}`, and :math:`i_\mathrm{c}` 
are the phase currents, which may vary freely in time. In our notation, the 
subscript c refers to the converter-side AC quantities and the superscript s 
refers to the stationary coordinates. The space vector does not include the 
zero-sequence component, which is defined as

.. math::
	i_\mathrm{c0} = \frac{1}{3}\left(i_\mathrm{a} + i_\mathrm{b} + i_\mathrm{c}\right) 
   :label: zero_sequence

.. Even though the zero-sequence voltage exists at the ouput of typical 
.. converters (see :doc:`/model/converters`), there is no path for the 
.. zero-sequence current to flow in three-phase three-wire grid-converter systems, 
.. i.e., :math:`i_\mathrm{c0} = 0`.

The space vector transformation in :eq:`space_vector` is implemented in the 
function :func:`gritulator.abc2complex` and its inverse transformation in the 
function :func:`gritulator.complex2abc`. 

L Filter 
--------

A dynamic model for an inductive L filter and inductive-resistive grid impedance 
is provided in the package :mod:`gritulator.model._grid_filter`. The model is 
implemented in stationary coordinates as

.. math::
   \frac{\mathrm{d}\boldsymbol{i}_\mathrm{g}^\mathrm{s}}{\mathrm{d} t} 
   = \frac{1}{L_\mathrm{t}}(\boldsymbol{u}_\mathrm{c}^\mathrm{s} 
   - \boldsymbol{e}_\mathrm{g}^\mathrm{s} 
   - R_\mathrm{t}\boldsymbol{i}_\mathrm{g}^\mathrm{s})
   :label: L_filt_model

where :math:`\boldsymbol{i}_\mathrm{g}^\mathrm{s}` is the grid current, 
:math:`\boldsymbol{u}_\mathrm{c}^\mathrm{s}` is the converter voltage, 
:math:`\boldsymbol{e}_\mathrm{g}^\mathrm{s}` is the grid voltage, 
:math:`R_\mathrm{t} = R_\mathrm{f} + R_\mathrm{g}` is the total resistance 
comprising the filter series resistance :math:`R_\mathrm{f}` and the grid 
resistance :math:`R_\mathrm{g}`, and :math:`L_\mathrm{t} = L_\mathrm{f} + L_\mathrm{g}` 
is the total inductance comprising the filter inductance 
:math:`L_\mathrm{f}` and the grid inductance :math:`L_\mathrm{g}`. The point of 
common coupling (PCC) is modeled to be between the L filter and grid impedance. 
The voltage at the PCC is obtained as

.. math::
   \boldsymbol{u}_\mathrm{g}^\mathrm{s} 
   = \frac{L_\mathrm{g}(\boldsymbol{u}_\mathrm{c}^\mathrm{s} 
   - R_\mathrm{f}\boldsymbol{i}_\mathrm{g}^\mathrm{s})
   + L_\mathrm{f}(\boldsymbol{e}_\mathrm{g}^\mathrm{s} 
   + R_\mathrm{g}\boldsymbol{i}_\mathrm{g}^\mathrm{s})}{L_\mathrm{t}}
   :label: L_filt_PCC_voltage


LCL Filter
----------

This section will be extended in the future.
