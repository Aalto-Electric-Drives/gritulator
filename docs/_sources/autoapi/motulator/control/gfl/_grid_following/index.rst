:orphan:

:py:mod:`motulator.control.gfl._grid_following`
===============================================

.. py:module:: motulator.control.gfl._grid_following

.. autoapi-nested-parse::

   This module contains grid-following control for grid-connected converters.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.control.gfl._grid_following.GridFollowingCtrlPars
   motulator.control.gfl._grid_following.GridFollowingCtrl
   motulator.control.gfl._grid_following.PLL
   motulator.control.gfl._grid_following.CurrentRefCalc
   motulator.control.gfl._grid_following.DCVoltageControl




.. py:class:: GridFollowingCtrlPars


   
   grid-following control parameters.
















   ..
       !! processed by numpydoc !!

.. py:class:: GridFollowingCtrl(pars)


   Bases: :py:obj:`motulator.control._common.Ctrl`

   
   Grid following control with the current controller and PLL to synchronize
   with the AC grid.

   :param pars: Control parameters.
   :type pars: GridFollowingCtrlPars

   .. rubric:: References

   .. [#Har2009] L. Harnefors and M. Bongiorno, "Current controller design
      for passivity of the input admittance," 2009 13th European Conference
      on Power Electronics and Applications, Barcelona, Spain, 2009, pp. 1-8.















   ..
       !! processed by numpydoc !!

.. py:class:: PLL(pars)


   
   PLL synchronizing loop.

   :param u_g_abc: Phase voltages at the PCC.
   :type u_g_abc: ndarray, shape (3,)

   :returns: * **u_g_q** (*float*) -- q-axis of the PCC voltage (V)
             * **abs_u_g** (*float*) -- amplitude of the voltage waveform, in V
             * **theta_pll** (*float*) -- estimated phase angle (in rad).















   ..
       !! processed by numpydoc !!
   .. py:method:: output(u_g_abc)

      
      Compute the estimated frequency and phase angle using the PLL.

      :param u_g_abc: Grid 3-phase voltage.
      :type u_g_abc: ndarray, shape (3,)

      :returns: * **u_g_q** (*float*) -- Error signal (in V, corresponds to the q-axis grid voltage).
                * **abs_u_g** (*float*) -- magnitude of the grid voltage vector (in V).
                * **w_g_pll** (*float*) -- estimated grid frequency (in rad/s).
                * **theta_pll** (*float*) -- estimated phase angle (in rad).















      ..
          !! processed by numpydoc !!

   .. py:method:: update(u_g_q)

      
      Update the integral state.

      :param u_g_q: Error signal (in V, corresponds to the q-axis grid voltage).
      :type u_g_q: real















      ..
          !! processed by numpydoc !!


.. py:class:: CurrentRefCalc(pars)


   
   Current controller reference generator

   This class is used to generate the current references for the current
   controllers based on the active and reactive power references.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(p_g_ref, q_g_ref)

      
      Power reference genetator.

      :param p_g_ref: active power reference
      :type p_g_ref: float
      :param q_g_ref: reactive power reference
      :type q_g_ref: float

      :returns: **i_c_ref** -- current reference in the rotationary frame
      :rtype: float















      ..
          !! processed by numpydoc !!


.. py:class:: DCVoltageControl(pars)


   
   DC voltage controller

   This class is used to generate the active power reference for the converter
   controller to ensure that the DC voltage is regulated.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(u_dc_ref, u_dc)

      
      Compute the active power reference sent to the converter control system
      to regulate the DC-bus voltage.

      :param u_dc_ref: DC-bus voltage reference
      :type u_dc_ref: float
      :param u_dc: DC-bus voltage
      :type u_dc: float

      :returns: * **err_dc** (*float*) -- DC capacitance energy error signal
                * **p_dc_ref** (*float*) -- power reference based on DC voltage controller
                * **p_dc_ref_lim** (*float*) -- saturated power reference based on DC voltage controller















      ..
          !! processed by numpydoc !!

   .. py:method:: update(err_dc, p_dc_ref, p_dc_ref_lim)

      
      Update the state of the DC-voltage controller with anti-windup.

      :param err_dc: DC capacitance energy error signal
      :type err_dc: float
      :param p_dc_ref: power reference based on DC voltage controller
      :type p_dc_ref: float
      :param p_dc_ref_lim: saturated power reference based on DC voltage controller
      :type p_dc_ref_lim: float















      ..
          !! processed by numpydoc !!


