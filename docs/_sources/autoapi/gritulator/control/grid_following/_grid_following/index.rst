:orphan:

:py:mod:`gritulator.control.grid_following._grid_following`
===========================================================

.. py:module:: gritulator.control.grid_following._grid_following

.. autoapi-nested-parse::

   grid following control methods for grid onverters.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.control.grid_following._grid_following.GridFollowingCtrlPars
   gritulator.control.grid_following._grid_following.GridFollowingCtrl
   gritulator.control.grid_following._grid_following.PLL
   gritulator.control.grid_following._grid_following.CurrentCtrl
   gritulator.control.grid_following._grid_following.CurrentRefCalc




.. py:class:: GridFollowingCtrlPars


   
   grid-following control parameters.
















   ..
       !! processed by numpydoc !!

.. py:class:: GridFollowingCtrl(pars)


   Bases: :py:obj:`gritulator.control._common.Ctrl`

   
   Grid following control for power converters.

   :param pars: Control parameters.
   :type pars: GridFollowingCtrlPars

   .. rubric:: References

   .. [#Har2009] Harnefors, Bongiorno, "Current controller design
      for passivity of the input admittance," 2009 13th European Conference
      on Power Electronics and Applications, Barcelona, Spain, 2009.















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


.. py:class:: CurrentCtrl(par, alpha_c)


   Bases: :py:obj:`gritulator.control._common.ComplexFFPICtrl`

   
   2DOF PI current controller for grid converters.

   This class provides an interface for a current controller for grid
   converters. The gains are initialized based on the desired closed-loop
   bandwidth and the filter inductance.

   :param par: Grid converter parameters, contains the filter inductance `L_f` (H).
   :type par: ModelPars
   :param alpha_c: Closed-loop bandwidth (rad/s).
   :type alpha_c: float















   ..
       !! processed by numpydoc !!

.. py:class:: CurrentRefCalc(pars)


   
   Current controller reference generator

   This class is used to generate the current references for the current
   controllers based on the active and reactive power references.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(p_g_ref, q_g_ref)

      
      Current reference genetator.

      :param p_g_ref: active power reference
      :type p_g_ref: float
      :param q_g_ref: reactive power reference
      :type q_g_ref: float

      :returns: **i_c_ref** -- current reference in the rotationary frame
      :rtype: float















      ..
          !! processed by numpydoc !!


