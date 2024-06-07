gritulator
==========

.. py:module:: gritulator

.. autoapi-nested-parse::

   
   *gritulator*: Grid Converter Simulator in Python

   This software includes continuous-time simulation models for grid converters.
   Furthermore, selected examples of discrete-time control algortihms are also
   included as well as various utilities.















   ..
       !! processed by numpydoc !!


Subpackages
-----------

.. toctree::
   :maxdepth: 1

   /autoapi/gritulator/control/index
   /autoapi/gritulator/model/index


Classes
-------

.. autoapisummary::

   gritulator.BaseValues
   gritulator.BaseValuesElectrical
   gritulator.Sequence
   gritulator.Step


Functions
---------

.. autoapisummary::

   gritulator.abc2complex
   gritulator.complex2abc
   gritulator.plot_grid


Package Contents
----------------

.. py:function:: abc2complex(u)

   
   Transform three-phase quantities to a complex space vector.

   :param u: Phase quantities.
   :type u: array_like, shape (3,)

   :returns: Complex space vector (peak-value scaling).
   :rtype: complex

   .. rubric:: Examples

   >>> from gritulator import abc2complex
   >>> y = abc2complex([1, 2, 3])
   >>> y
   (-1-0.5773502691896258j)















   ..
       !! processed by numpydoc !!

.. py:function:: complex2abc(u)

   
   Transform a complex space vector to three-phase quantities.

   :param u: Complex space vector (peak-value scaling).
   :type u: complex

   :returns: Phase quantities.
   :rtype: ndarray, shape (3,)

   .. rubric:: Examples

   >>> from gritulator import complex2abc
   >>> y = complex2abc(1-.5j)
   >>> y
   array([ 1.       , -0.9330127, -0.0669873])















   ..
       !! processed by numpydoc !!

.. py:class:: BaseValues

   
   Base values.

   Base values are computed from the nominal values and the number of pole
   pairs. They can be used, e.g., for scaling the plotted waveforms.

   :param U_nom: Voltage (V, rms, line-line).
   :type U_nom: float
   :param I_nom: Current (A, rms).
   :type I_nom: float
   :param f_nom: Frequency (Hz).
   :type f_nom: float
   :param tau_nom: Torque (Nm).
   :type tau_nom: float
   :param P_nom: Power (W).
   :type P_nom: float
   :param n_p: Number of pole pairs.
   :type n_p: int

   .. attribute:: u

      Base voltage (V, peak, line-neutral).

      :type: float

   .. attribute:: i

      Base current (A, peak).

      :type: float

   .. attribute:: w

      Base angular frequency (rad/s).

      :type: float

   .. attribute:: psi

      Base flux linkage (Vs).

      :type: float

   .. attribute:: p

      Base power (W).

      :type: float

   .. attribute:: Z

      Base impedance (Ω).

      :type: float

   .. attribute:: L

      Base inductance (H).

      :type: float

   .. attribute:: tau

      Base torque (Nm).

      :type: float















   ..
       !! processed by numpydoc !!

.. py:class:: BaseValuesElectrical

   
   Base values.

   Base values are computed from the nominal values.
   They can be used, e.g., for scaling the plotted waveforms.















   ..
       !! processed by numpydoc !!

.. py:class:: Sequence(times, values, periodic=False)

   
   Sequence generator.

   The time array must be increasing. The output values are interpolated
   between the data points.

   :param times: Time values.
   :type times: ndarray
   :param values: Output values.
   :type values: ndarray
   :param periodic: Enables periodicity. The default is False.
   :type periodic: bool, optional















   ..
       !! processed by numpydoc !!

.. py:class:: Step(step_time, step_value, initial_value=0)

   
   Step function.
















   ..
       !! processed by numpydoc !!

.. py:function:: plot_grid(sim, t_range=None, base=None, plot_pcc_voltage=False, plot_w=False)

   
   Plot example figures of grid converter simulations.

   Plots figures in per-unit values, if the base values are given. Otherwise
   SI units are used.

   :param sim: Should contain the simulated data.
   :type sim: Simulation object
   :param t_range: Time range. The default is (0, sim.ctrl.t[-1]).
   :type t_range: 2-tuple, optional
   :param base: Base values for scaling the waveforms.
   :type base: BaseValues, optional
   :param plot_pcc_voltage: 'True' if the user wants to plot the 3-phase waveform at the PCC. This
                            is an optional feature and the grid voltage is plotted by default.
   :type plot_pcc_voltage: Boolean, optional
   :param plot_w: 'True' if the user wants to plot the grid frequency instead of the
                  phase angles (by default).
   :type plot_w: Boolean, optional















   ..
       !! processed by numpydoc !!

