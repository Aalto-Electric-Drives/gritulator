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


LCL Filter
----------
