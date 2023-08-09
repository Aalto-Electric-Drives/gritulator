:orphan:

:py:mod:`motulator.model.dc_bus._dc_dyn_model`
==============================================

.. py:module:: motulator.model.dc_bus._dc_dyn_model

.. autoapi-nested-parse::

   This module contains continuous-time models for grid connected converters when
   the DC bus is modelled using a current-source model.

   Peak-valued complex space vectors are used. The space vector models are
   implemented in stationary coordinates.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.model.dc_bus._dc_dyn_model.DCBusAndLFilterModel
   motulator.model.dc_bus._dc_dyn_model.DCBusAndLCLFilterModel




.. py:class:: DCBusAndLFilterModel(grid_filter=None, grid_model=None, dc_model=None, converter=None)


   
   Continuous-time model for a grid model with an RL impedance model.

   This interconnects the subsystems of a converter with a grid and provides
   an interface to the solver. More complicated systems could be modeled using
   a similar template.

   :param grid_filter: RL line dynamic model.
   :type grid_filter: LFilter
   :param grid_model: Constant voltage source model.
   :type grid_model: Grid
   :param dc_model: DC grid voltage dynamics (capacitance model)
   :type dc_model: DcGrid
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


   
   Continuous-time model for a grid model with an LCL impedance model.

   This interconnects the subsystems of a converter with a grid and provides
   an interface to the solver. More complicated systems could be modeled using
   a similar template.

   :param grid_filter: LCL dynamic model.
   :type grid_filter: LCLFilter
   :param grid_model: Constant voltage source model.
   :type grid_model: Grid
   :param dc_model: DC grid voltage dynamics (capacitance model)
   :type dc_model: DcGrid
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


