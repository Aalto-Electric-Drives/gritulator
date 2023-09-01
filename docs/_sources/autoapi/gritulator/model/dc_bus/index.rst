:py:mod:`gritulator.model.dc_bus`
=================================

.. py:module:: gritulator.model.dc_bus

.. autoapi-nested-parse::

   
   Continuous-time DC-bus models.
















   ..
       !! processed by numpydoc !!


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.model.dc_bus.DCBus
   gritulator.model.dc_bus.DCBusAndLFilterModel
   gritulator.model.dc_bus.DCBusAndLCLFilterModel




.. py:class:: DCBus(C_dc=0.001, G_dc=0, i_ext=lambda t: 0, u_dc0=650)


   
   DC bus model

   This model is used to compute the DC bus dynamics, represented by a first-
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
              dc current (A)













      ..
          !! processed by numpydoc !!

   .. py:method:: f(t, u_dc, i_c_abc, q)

      
       Compute the state derivatives.


      :Parameters:

          **t** : float
                  Time.
              u_dc: float
                  DC bus voltage (V)

          **i_c_abc** : ndarray, shape (3,)
              Phase currents.

          **q** : complex ndarray, shape (3,)
                 Switching state vectors corresponding to the switching instants.
                 For example, the switching state q[1] is applied at the interval
                 t_n_sw[1].
              Returns
              -------
              double list, length 1
                      Time derivative of the complex state vector, [du_dc]














      ..
          !! processed by numpydoc !!

   .. py:method:: meas_dc_voltage()

      
      Measure the DC voltage at the end of the sampling period.

      :returns: **u_dc** -- DC bus voltage (V)
      :rtype: float















      ..
          !! processed by numpydoc !!


.. py:class:: DCBusAndLFilterModel(grid_filter=None, grid_model=None, dc_model=None, converter=None)


   
   Continuous-time model for a stiff grid model with an RL impedance model.

   :param grid_filter: RL line dynamic model.
   :type grid_filter: LFilter
   :param grid_model: Constant voltage source model.
   :type grid_model: StiffSource
   :param dc_model: DC-bus voltage dynamics.
   :type dc_model: DCBus
   :param converter: Inverter model.
   :type converter: Inverter | PWMInverter















   ..
       !! processed by numpydoc !!
   .. py:method:: get_initial_values()

      
      Get the initial values.

      :returns: **x0** -- Initial values of the state variables.
      :rtype: complex list, length 2















      ..
          !! processed by numpydoc !!

   .. py:method:: set_initial_values(t0, x0)

      
      Set the initial values.

      :param x0: Initial values of the state variables.
      :type x0: complex ndarray















      ..
          !! processed by numpydoc !!

   .. py:method:: f(t, x)

      
      Compute the complete state derivative list for the solver.

      :param t: Time.
      :type t: float
      :param x: State vector.
      :type x: complex ndarray

      :returns: State derivatives.
      :rtype: complex list















      ..
          !! processed by numpydoc !!

   .. py:method:: save(sol)

      
      Save the solution.

      :param sol: Solution from the solver.
      :type sol: Bunch object















      ..
          !! processed by numpydoc !!

   .. py:method:: post_process()

      
      Transform the lists to the ndarray format and post-process them.
















      ..
          !! processed by numpydoc !!


.. py:class:: DCBusAndLCLFilterModel(grid_filter=None, grid_model=None, dc_model=None, converter=None)


   
   Continuous-time model for a stiff grid model with an LCL impedance model.

   :param grid_filter: LCL filter dynamic model.
   :type grid_filter: LCLFilter
   :param grid_model: Constant voltage source model.
   :type grid_model: StiffSource
   :param dc_model: DC-bus voltage dynamics.
   :type dc_model: DCBus
   :param converter: Inverter model.
   :type converter: Inverter | PWMInverter















   ..
       !! processed by numpydoc !!
   .. py:method:: get_initial_values()

      
      Get the initial values.

      :returns: **x0** -- Initial values of the state variables.
      :rtype: complex list, length 4















      ..
          !! processed by numpydoc !!

   .. py:method:: set_initial_values(t0, x0)

      
      Set the initial values.

      :param x0: Initial values of the state variables.
      :type x0: complex ndarray















      ..
          !! processed by numpydoc !!

   .. py:method:: f(t, x)

      
      Compute the complete state derivative list for the solver.

      :param t: Time.
      :type t: float
      :param x: State vector.
      :type x: complex ndarray

      :returns: State derivatives.
      :rtype: complex list















      ..
          !! processed by numpydoc !!

   .. py:method:: save(sol)

      
      Save the solution.

      :param sol: Solution from the solver.
      :type sol: Bunch object















      ..
          !! processed by numpydoc !!

   .. py:method:: post_process()

      
      Transform the lists to the ndarray format and post-process them.
















      ..
          !! processed by numpydoc !!


