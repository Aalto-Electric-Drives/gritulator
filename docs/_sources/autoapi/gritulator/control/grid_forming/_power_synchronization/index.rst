:orphan:

:py:mod:`gritulator.control.grid_forming._power_synchronization`
================================================================

.. py:module:: gritulator.control.grid_forming._power_synchronization

.. autoapi-nested-parse::

   power synchronization control methods for grid converters.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.control.grid_forming._power_synchronization.PSCCtrlPars
   gritulator.control.grid_forming._power_synchronization.PSCCtrl
   gritulator.control.grid_forming._power_synchronization.PowerCalc
   gritulator.control.grid_forming._power_synchronization.PowerSynch
   gritulator.control.grid_forming._power_synchronization.CurrentCtrl




.. py:class:: PSCCtrlPars


   
   Parameters for the control system.
















   ..
       !! processed by numpydoc !!

.. py:class:: PSCCtrl(pars)


   Bases: :py:obj:`gritulator.control._common.Ctrl`

   
   power synchronization control for grid converters.

   This implements the power synchronization control (PSC) method described in
   [#Har2019]_. The alternative reference-feedforward PSC (RFPSC) can also be
   used and is based on [#Har2020]_.

   :param pars: Control parameters.
   :type pars: PSCtrlPars

   .. rubric:: References

   .. [#Har2019] Harnefors, Hinkkanen, Riaz, Rahman, Zhang, "Robust Analytic
       Design of Power-Synchronization Control," IEEE Trans. Ind. Electron., Aug.
       2019, https://doi.org/10.1109/TIE.2018.2874584

   .. [#Har2020] Harnefors, Rahman, Hinkkanen, Routimo, "Reference-Feedforward
       Power-Synchronization Control," IEEE Trans. Power Electron., Sep. 2020,
       https://doi.org/10.1109/TPEL.2020.2970991















   ..
       !! processed by numpydoc !!

.. py:class:: PowerCalc(pars)


   
   Internal controller power calculator

   This class is used to calculate the active and reactive powers at the
   converter outputs by using voltage and current in complex form
   used in the control.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(i_c, u_c)

      
      Power calculation.

      :param i_c: current in dq frame (A).
      :type i_c: complex
      :param u_c: voltage in dq frame (V).
      :type u_c: complex

      :returns: * **p_calc** (*float*) -- calculated active power
                * **q_calc** (*float*) -- calculated reactive power















      ..
          !! processed by numpydoc !!


.. py:class:: PowerSynch(pars)


   
   Active power/frequency synchronizing loop.

   This control loop is used to synchronize with the grid using the active
   power variations compared to the active power reference.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(p_calc, p_g_ref, w_c_ref)

      
      Compute the estimated frequency and phase angle using the PSC

      :param p_calc: calculated active power at the converter outputs (W).
      :type p_calc: float
      :param pg_ref: active power reference (W).
      :type pg_ref: float
      :param w_c_ref: frequency reference (rad/s).
      :type w_c_ref: float

      :returns: * **w_c** (*float*) -- estimated converter frequency (rad/s).
                * **theta_c** (*float*) -- estimated converter phase angle (rad).















      ..
          !! processed by numpydoc !!

   .. py:method:: update(theta_c)

      
      Update the integral state.

      :param theta_c: estimated converter phase angle (rad).
      :type theta_c: float















      ..
          !! processed by numpydoc !!


.. py:class:: CurrentCtrl(pars)


   
   PSC-based current controller.

   PSC makes the converter operate as a voltage source, however, this block
   is used to damp the current oscillations and limit the current
   flowing through the converter to avoid physical damages of the device.

   It is important to note that this block uses P-type controller and can thus
   encounter steady-state error when the current reference is saturated.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(i_c, p_g_ref, v_ref, w_c_ref)

      
      Compute the converter voltage reference signal

      :param i_c: converter current in dq frame (A).
      :type i_c: complex
      :param p_g_ref: active power reference (W).
      :type p_g_ref: float
      :param v_ref: converter voltage magnitude reference (V).
      :type v_ref: float
      :param w_c_ref: converter frequency reference (rad/s).
      :type w_c_ref: float

      :returns: * **u_c_ref** (*complex*) -- converter voltage reference (V).
                * **i_c_ref** (*complex*) -- converter current reference in dq frame (A).
                * **i_c_filt** (*complex*) -- low-pass filtered converter current in dq frame (A).















      ..
          !! processed by numpydoc !!

   .. py:method:: update(i_c, i_c_filt)

      
      Update the integral state.

      :param i_c: converter current in dq frame (A).
      :type i_c: complex
      :param i_c_filt: low-pass filtered converter current in dq frame (A).
      :type i_c_filt: complex















      ..
          !! processed by numpydoc !!


