:orphan:

:py:mod:`gritulator.model.dc_bus._dc_bus`
=========================================

.. py:module:: gritulator.model.dc_bus._dc_bus

.. autoapi-nested-parse::

   Dynamic model of a DC bus.

   A DC bus between an external current source or sink and a converter is modeled
   considering an equivalent circuit comprising a capacitor and parallel resitor.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.model.dc_bus._dc_bus.DCBus




.. py:class:: DCBus(C_dc=0.001, G_dc=0, i_ext=lambda t: 0, u_dc0=650)


   
   DC bus model

   This model is used to compute the capacitive DC bus dynamics. Dynamics are
   modeled with an equivalent circuit comprising a capacitor and its parallel
   resistor that is parametrized using a conductance. The capacitor voltage is
   used as a state variable.

   :param C_dc: DC-bus capacitance (F)
   :type C_dc: float
   :param G_dc: Parallel conductance of the capacitor (S)
   :type G_dc: float
   :param i_ext: External DC current, seen as disturbance, `i_ext(t)`.
   :type i_ext: function















   ..
       !! processed by numpydoc !!
   .. py:method:: dc_current(i_c_abc, q)
      :staticmethod:

      
      Compute the converter DC current from the switching states and phase
      currents.

      :param i_c_abc: Phase currents (A).
      :type i_c_abc: ndarray, shape (3,)
      :param q: Switching state vectors corresponding to the switching instants.
                For example, the switching state q[1] is applied at the interval
                t_n_sw[1].
      :type q: complex ndarray, shape (3,)

      :returns: **i_dc** -- Converter DC current (A)
      :rtype: float















      ..
          !! processed by numpydoc !!

   .. py:method:: f(t, u_dc, i_dc)

      
      Compute the state derivatives.

      :param t: Time (s)
      :type t: float
      :param u_dc: DC bus voltage (V)
      :type u_dc: float
      :param i_dc: Converter DC current (A)
      :type i_dc: float

      :returns: Time derivative of the complex state vector, [du_dc]
      :rtype: double list, length 1















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_dc_voltage()

      
      Measure the DC bus voltage at the end of the sampling period.

      :returns: **u_dc** -- DC bus voltage (V)
      :rtype: float















      ..
          !! processed by numpydoc !!


