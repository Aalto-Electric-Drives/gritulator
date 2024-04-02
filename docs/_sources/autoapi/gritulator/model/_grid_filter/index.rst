:orphan:

:py:mod:`gritulator.model._grid_filter`
=======================================

.. py:module:: gritulator.model._grid_filter

.. autoapi-nested-parse::

   Grid and AC filter impedance models.

   This module contains continuous-time models for subsystems comprising an AC
   filter and a grid impedance between the converter and grid voltage sources. The
   models are implemented with space vectors in stationary coordinates.

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


   
   Dynamic model for an inductive L filter and an inductive-resistive grid.

   An L filter and inductive-resistive grid impedance, between the converter and
   grid voltage sources, are modeled combining their inductances and series
   resistances in a state equation. The grid current is used as a state
   variable. The point-of-common-coupling (PCC) voltage between the L filter
   and the grid impedance is separately calculated.

   :param L_f: Filter inductance (H)
   :type L_f: float
   :param R_f: Filter series resistance (Ω)
   :type R_f: float
   :param L_g: Grid inductance (H)
   :type L_g: float
   :param R_g: Grid resistance (Ω)
   :type R_g: float















   ..
       !! processed by numpydoc !!
   .. py:method:: pcc_voltages(i_gs, u_cs, e_gs)

      
      Compute the point-of-common-coupling voltage.

      This computes the point-of-common-coupling (PCC) voltage between the
      L filter and grid impedance.

      :param i_gs: Grid current (A).
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


   
   Dynamic model for an inductive-capacitive-inductive (LCL) filter and a grid.

   An LCL filter and inductive-resistive grid impedance, between the converter
   and grid voltage sources, are modeled using converter-side current, capacitor
   voltage and grid-side current of the LCL filter as state variables. Grid
   inductance and resistance are included in the state equation of grid-side
   current. The point-of-common-coupling (PCC) voltage between the LCL filter
   and the grid impedance is separately calculated.

   :param L_fc: Converter-side LCL filter inductance (H)
   :type L_fc: float
   :param R_fc: Converter-side series resistance (Ω)
   :type R_fc: float
   :param L_fg: Grid-side LCL filter inductance (H)
   :type L_fg: float
   :param R_fg: Grid-side series resistance (Ω)
   :type R_fg: float
   :param C_f: LCL Filter capacitance (F)
   :type C_f: float
   :param G_f: Conductance of a resistance in parallel with the LCL filter capacitor (S)
   :type G_f: float
   :param L_g: Grid inductance (H)
   :type L_g: float
   :param R_g: Grid resistance (Ω)
   :type R_g: float















   ..
       !! processed by numpydoc !!
   .. py:method:: pcc_voltages(i_gs, u_fs, e_gs)

      
      Compute the point-of-common-coupling voltage.

      This calculates point-of-common-coupling (PCC) voltage that is located
      between the LCL filter and grid impedance.

      :param i_gs: Grid current (A).
      :type i_gs: complex
      :param u_fs: Capacitor voltage (V).
      :type u_fs: complex
      :param e_gs: Grid voltage (V).
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


