:orphan:

:py:mod:`motulator.model._grid_filter`
======================================

.. py:module:: motulator.model._grid_filter

.. autoapi-nested-parse::

   This module contains continuous-time models for AC filters

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.model._grid_filter.LFilter
   motulator.model._grid_filter.LCLFilter




.. py:class:: LFilter(U_gN=400 * np.sqrt(2 / 3), L_f=0.006, R_f=0, L_g=0, R_g=0)


   
   Inductive filter model with a connection made to the inverter outputs.

   An inductive filter model is built using a simple inductance model where
   the two output voltages are imposed and the current can be calculated using
   dynamic equations. This model includes a model for an inductive-resistive
   impedance of the grid combined with the L-filter model.

   :param L_f: Filter inductance (in H)
   :type L_f: float
   :param R_f: Filter resistance (in Ohm)
   :type R_f: float
   :param L_g: Grid inductance (in H)
   :type L_g: float
   :param R_g: Grid resistance (in Ohm)
   :type R_g: float















   ..
       !! processed by numpydoc !!
   .. py:method:: pcc_voltages(i_gs, u_cs, e_gs)

      
      Compute the PCC voltage, located in-between the filter and the line
      impedances

      :param i_gs: Line current (A).
      :type i_gs: complex
      :param u_cs: Converter voltage (V).
      :type u_cs: complex
      :param e_gs: Grid voltage (V).
      :type e_gs: complex

      :returns: **u_gs** -- Voltage at the point of common coupling (PCC).
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

      :returns: **di_gs** -- Time derivative of the complex state i_gs (line current, in A)
      :rtype: complex















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_currents()

      
      Measure the phase currents at the end of the sampling period.

      :returns: **i_g_abc** -- Phase currents.
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_pcc_voltage()

      
      Measure the PCC voltages at the end of the sampling period.

      :returns: **u_g_abc** -- Phase voltage at the point of common coupling (PCC).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!


.. py:class:: LCLFilter(U_gN=400 * np.sqrt(2 / 3), L_fc=0.006, R_fc=0, L_fg=0.003, R_fg=0, C_f=1e-05, G_f=0, L_g=0, R_g=0)


   
   LCL filter and inductive grid model with a connection made to the
   inverter outputs.

   An LCL-type grid model is built using an LCL model where the two output
   voltages are imposed and the grid-side current, the converter-side
   current and the capacitance voltage can be calculated using dynamic
   equations. This model includes a model for an inductive-resistive
   impedance of the grid combined with the LCL-filter model.

   :param L_fc: Converter-side filter inductance (in H)
   :type L_fc: float
   :param R_fc: Converter-side filter resistance (in Ohm)
   :type R_fc: float
   :param L_fg: Grid-side filter inductance (in H)
   :type L_fg: float
   :param R_fg: Grid-side filter resistance (in Ohm)
   :type R_fg: float
   :param C_f: Filter capacitance (in F)
   :type C_f: float
   :param G_f: LCL filter conductance (in S)
   :type G_f: float
   :param L_g: Grid inductance (in H)
   :type L_g: float
   :param R_g: Grid resistance (in Ohm)
   :type R_g: float















   ..
       !! processed by numpydoc !!
   .. py:method:: pcc_voltages(i_gs, u_fs, e_gs)

      
      Compute the PCC voltage, located in-between the filter and the line
      impedances

      :param i_gs: Grid-side line current (A).
      :type i_gs: complex
      :param u_fs: Capacitance voltage (V).
      :type u_fs: complex
      :param e_gs: Grid-side voltage (V).
      :type e_gs: complex

      :returns: **u_gs** -- Voltage at the point of common coupling (PCC).
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

      :returns: * **i_cs** (*complex*) -- Time derivative of the complex i_cs (in A).
                * **u_fs** (*complex*) -- Time derivative of the complex u_fs (in V).
                * **di_gs** (*complex*) -- Time derivative of the complex state i_gs (in A)















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

      :returns: **i_g_abc** -- Phase currents.
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_cap_voltage()

      
      Measure the capacitor voltages at the end of the sampling period.

      :returns: **u_f_abc** -- Phase voltage through the capacitance of the LCL filter.
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_pcc_voltage()

      
      Measure the PCC voltages at the end of the sampling period.

      :returns: **u_g_abc** -- Phase voltage at the point of common coupling (PCC).
      :rtype: 3-tuple of floats















      ..
          !! processed by numpydoc !!


