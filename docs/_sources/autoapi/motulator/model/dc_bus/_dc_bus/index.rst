:orphan:

:py:mod:`motulator.model.dc_bus._dc_bus`
========================================

.. py:module:: motulator.model.dc_bus._dc_bus

.. autoapi-nested-parse::

   This module contains dc grid model.

   The dc grid model defined here is used if the dc bus is modelled as a current
   source and the capacitance dynamics need to be modeled.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.model.dc_bus._dc_bus.DCBus




.. py:class:: DCBus(C_dc=0.001, G_dc=0, i_ext=lambda t: 0, u_dc0=650)


   
   DC bus model

   This model is used to compute the DC bus dynamics, represented by a first
   order system with the DC-bus capacitance dynamics.

   :Parameters:

       **C_dc** : float
               DC bus capacitance (in Farad)
           G_dc : float
               DC bus conductance (in Siemens)

       **i_ext** : function
           External dc current, seen as disturbance, `i_ext(t)`.














   ..
       !! processed by numpydoc !!
   .. py:method:: dc_current(i_c_abc, q)
      :staticmethod:

      
       Compute the converter DC current, used to model the DC-bus voltage
       dynamics.


      :Parameters:

          **i_c_abc** : ndarray, shape (3,)
              Phase currents.

          **q** : complex ndarray, shape (3,)
              Switching state vectors corresponding to the switching instants.
              For example, the switching state q[1] is applied at the interval
              t_n_sw[1].

      :Returns:

          i_dc: float
              dc current (in A)













      ..
          !! processed by numpydoc !!

   .. py:method:: f(t, u_dc, i_c_abc, q)

      
       Compute the state derivatives.


      :Parameters:

          **t** : float
                  Time.
              u_dc: float
                  DC bus voltage (in V)

          **i_c_abc** : ndarray, shape (3,)
              Phase currents.

          **q** : complex ndarray, shape (3,)
                 Switching state vectors corresponding to the switching instants.
                 For example, the switching state q[1] is applied at the interval
                 t_n_sw[1].
              Returns
              -------
              du_dc: float
                  Time derivative of the state variable, u_dc (capacitance voltage)














      ..
          !! processed by numpydoc !!

   .. py:method:: meas_dc_voltage()

      
      Measure the DC voltage at the end of the sampling period.

      :returns: **u_dc** -- DC bus voltage (in V)
      :rtype: float















      ..
          !! processed by numpydoc !!


