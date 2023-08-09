:orphan:

:py:mod:`motulator._plots`
==========================

.. py:module:: motulator._plots

.. autoapi-nested-parse::

   Example plotting scripts.

   ..
       !! processed by numpydoc !!


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   motulator._plots.plot_grid
   motulator._plots.save_plot



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

.. py:function:: save_plot(name)

   
   Save figures.

   This saves figures in a folder "figures" in the current directory. If the
   folder doesn't exist, it is created.

   :param name: Name for the figure
   :type name: string
   :param plt: Handle for the figure to be saved
   :type plt: object















   ..
       !! processed by numpydoc !!

