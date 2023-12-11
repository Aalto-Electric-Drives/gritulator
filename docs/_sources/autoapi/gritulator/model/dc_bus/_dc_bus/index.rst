:orphan:

:py:mod:`gritulator.model.dc_bus._dc_bus`
=========================================

.. py:module:: gritulator.model.dc_bus._dc_bus

.. autoapi-nested-parse::

   DC-bus dynamic model.

   The dc bus is defined as a current source with a DC capacitance model, which
   despicted the DC-bus voltage dynamics.

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

   This model is used to compute the DC bus dynamics, represented by a first-
   order system with the DC-bus capacitance dynamics.

   :param C_dc: DC bus capacitance (in Farad)
   :type C_dc: float
   :param G_dc: DC bus conductance (in Siemens)
   :type G_dc: float
   :param i_ext: External dc current, seen as disturbance, `i_ext(t)`.
   :type i_ext: function















   ..
       !! processed by numpydoc !!
   .. py:method:: dc_current(i_c_abc, q)
      :staticmethod:

      
      Compute the converter DC current, used to model the DC-bus voltage
      dynamics.

      :param i_c_abc: Phase currents.
      :type i_c_abc: ndarray, shape (3,)
      :param q: Switching state vectors corresponding to the switching instants.
                For example, the switching state q[1] is applied at the interval
                t_n_sw[1].
      :type q: complex ndarray, shape (3,)

      :returns: **i_dc** -- dc current (A)
      :rtype: float















      ..
          !! processed by numpydoc !!

   .. py:method:: f(t, u_dc, i_c_abc, q)

      
      Compute the state derivatives.

      :param t: Time.
      :type t: float
      :param u_dc: DC bus voltage (V)
      :type u_dc: float
      :param i_c_abc: Phase currents.
      :type i_c_abc: ndarray, shape (3,)
      :param q: Switching state vectors corresponding to the switching instants.
                For example, the switching state q[1] is applied at the interval
                t_n_sw[1].
      :type q: complex ndarray, shape (3,)

      :returns: Time derivative of the complex state vector, [du_dc]
      :rtype: double list, length 1















      ..
          !! processed by numpydoc !!

   .. py:method:: meas_dc_voltage()

      
      Measure the DC voltage at the end of the sampling period.

      :returns: **u_dc** -- DC bus voltage (V)
      :rtype: float















      ..
          !! processed by numpydoc !!


