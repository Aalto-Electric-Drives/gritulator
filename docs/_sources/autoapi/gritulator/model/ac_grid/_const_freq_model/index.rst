:orphan:

:py:mod:`gritulator.model.ac_grid._const_freq_model`
====================================================

.. py:module:: gritulator.model.ac_grid._const_freq_model

.. autoapi-nested-parse::

   Electromechanical stiff AC grid and converter model interconnectors.

       This interconnects the subsystems of a converter with a grid and provides
       an interface to the solver. More complicated systems could be modeled using
       a similar template. Peak-valued complex space vectors are used. The space
       vector models are implemented in stationary coordinates.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.model.ac_grid._const_freq_model.StiffSourceAndLFilterModel
   gritulator.model.ac_grid._const_freq_model.StiffSourceAndLCLFilterModel




.. py:class:: StiffSourceAndLFilterModel(grid_filter=None, grid_model=None, converter=None)


   
   Continuous-time model for a stiff grid model with an RL impedance model.

   :param grid_filter: RL line dynamic model.
   :type grid_filter: LFilter
   :param grid_model: Constant voltage source model.
   :type grid_model: StiffSource
   :param converter: Inverter model.
   :type converter: Inverter | PWMInverter















   ..
       !! processed by numpydoc !!
   .. py:method:: get_initial_values()

      
      Get the initial values.

      :returns: **x0** -- Initial values of the state variables.
      :rtype: complex list, length 1















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


.. py:class:: StiffSourceAndLCLFilterModel(grid_filter=None, grid_model=None, converter=None)


   
   Continuous-time model for a stiff grid model with an LCL impedance model.

   :param grid_filter: LCL dynamic model.
   :type grid_filter: LCLFilter
   :param grid_model: Constant voltage source model.
   :type grid_model: StiffSource
   :param converter: Inverter model.
   :type converter: Inverter | PWMInverter















   ..
       !! processed by numpydoc !!
   .. py:method:: get_initial_values()

      
      Get the initial values.

      :returns: **x0** -- Initial values of the state variables.
      :rtype: complex list, length 3















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


