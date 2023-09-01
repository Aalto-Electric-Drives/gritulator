:orphan:

:py:mod:`gritulator.model._grid_filter`
=======================================

.. py:module:: gritulator.model._grid_filter

.. autoapi-nested-parse::

   Grid and converter filter impedance models.

   This module contains continuous-time models for the AC impedance between the
   converter output and the AC grid. In this module, all space vectors are in
   stationary coordinates.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.model._grid_filter.LFilter
   gritulator.model._grid_filter.LCLFilter




.. py:class:: LFilter(U_gN=400 * np.sqrt(2 / 3), L_f=0.006, R_f=0, L_g=0, R_g=0)


   
   Inductive-resistive filter dynamic model.

   An inductive filter model is built using a simple inductance model where
   the two output voltages are imposed and the current can be calculated using
   dynamic equations. This model includes a model for an inductive-resistive
   impedance of the grid combined with the L-filter model.

   :param L_f: Filter inductance (H)
   :type L_f: float
   :param R_f: Filter resistance (Ω)
   :type R_f: float
   :param L_g: Grid inductance (H)
   :type L_g: float
   :param R_g: Grid resistance (Ω)
   :type R_g: float















   ..
       !! processed by numpydoc !!
   .. py:method:: pcc_voltages(i_gs, u_cs, e_gs)

      
      Compute the point of common coupling voltage.

      point of common coupling (PCC) is located at grid-side end of the
      converter output filter.

      :param i_gs: Line current (A).
      :type i_gs: complex
      :param u_cs: Converter voltage (V).
      :type u_cs: complex
      :param e_gs: Grid voltage (V).
      :type e_gs: complex

      :returns: **u_gs** -- Voltage at the point of common coupling (V).
      :rtype: complex















      ..
          !! processed by numpydoc !!

   .. py:method:: f(i_gs, u_cs, e_gs)

      
      Compute the state derivatives.

      :param i_gs: Line current (A).
      :type i_gs: complex
      :param u_cs: Converter-side voltage (V).
      :type u_cs: complex
      :param e_gs: Grid-side voltage (V).
      :type e_gs: complex

      :returns: Time derivative of the complex state vector, [di_gs]
      :rtype: complex list, length 1















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_currents()

      
      Measure the phase currents at the end of the sampling period.

      :returns: **i_g_abc** -- Phase currents (A).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_pcc_voltage()

      
      Measure the PCC voltages at the end of the sampling period.

      :returns: **u_g_abc** -- Phase voltage at the point of common coupling (V).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!


.. py:class:: LCLFilter(U_gN=400 * np.sqrt(2 / 3), L_fc=0.006, R_fc=0, L_fg=0.003, R_fg=0, C_f=1e-05, G_f=0, L_g=0, R_g=0)


   
   Inductive-capacitive-inductive (LCL) filter dynamic model.

   An LCL-type grid model is built using inductive and capacitive dynamic
   models. The two output voltages are imposed and the grid-side current, the
   converter-side current and the capacitance voltage can be calculated using
   dynamic equations. This model includes a model for an inductive-resistive
   impedance of the grid combined with the LCL-filter model.

   :param L_fc: Converter-side filter inductance (H)
   :type L_fc: float
   :param R_fc: Converter-side filter resistance (Ω)
   :type R_fc: float
   :param L_fg: Grid-side filter inductance (H)
   :type L_fg: float
   :param R_fg: Grid-side filter resistance (Ω)
   :type R_fg: float
   :param C_f: Filter capacitance (F)
   :type C_f: float
   :param G_f: LCL filter conductance (S)
   :type G_f: float
   :param L_g: Grid inductance (H)
   :type L_g: float
   :param R_g: Grid resistance (Ω)
   :type R_g: float















   ..
       !! processed by numpydoc !!
   .. py:method:: pcc_voltages(i_gs, u_fs, e_gs)

      
      Compute the point of common coupling voltage.

      point of common coupling (PCC) is located at the grid-side end of the
      converter output filter.

      :param i_gs: Grid-side line current (A).
      :type i_gs: complex
      :param u_fs: Capacitance voltage (V).
      :type u_fs: complex
      :param e_gs: Grid-side voltage (V).
      :type e_gs: complex

      :returns: **u_gs** -- Voltage at the point of common coupling (V).
      :rtype: complex















      ..
          !! processed by numpydoc !!

   .. py:method:: f(i_cs, u_fs, i_gs, u_cs, e_gs)

      
      Compute the state derivatives.

      :param i_cs: Converter line current (A).
      :type i_cs: complex
      :param u_fs: Capacitance voltage (V).
      :type u_fs: complex
      :param i_gs: Grid line current (A).
      :type i_gs: complex
      :param u_cs: Converter voltage (V).
      :type u_cs: complex
      :param e_gs: Grid voltage (V).
      :type e_gs: complex

      :returns: Time derivative of the complex state vector, [di_cs, du_fs, di_gs]
      :rtype: complex list, length 3















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_currents()

      
      Measure the converter currents at the end of the sampling period.

      :returns: **i_c_abc** -- Phase currents.
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_grid_currents()

      
      Measure the grid currents at the end of the sampling period.

      :returns: **i_g_abc** -- Phase currents (A).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_cap_voltage()

      
      Measure the capacitor voltages at the end of the sampling period.

      :returns: **u_f_abc** -- Phase voltage through the capacitance of the LCL filter (V).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_pcc_voltage()

      
      Measure the PCC voltages at the end of the sampling period.

      :returns: **u_g_abc** -- Phase voltage at the point of common coupling (V).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!


