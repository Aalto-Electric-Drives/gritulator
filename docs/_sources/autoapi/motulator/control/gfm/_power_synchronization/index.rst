:orphan:

:py:mod:`motulator.control.gfm._power_synchronization`
======================================================

.. py:module:: motulator.control.gfm._power_synchronization

.. autoapi-nested-parse::

   This module contains Power Synchronization Control (PSC) for grid converters

   This control scheme is based on the updated version presented in [1]. More info
   can be found in this reference.

   [1] Reference-feedforward power-synchronization control, L Harnefors,
   FMM Rahman, M Hinkkanen, M Routimo - IEEE Transactions on Power Electronics,
   2020.

   ..
       !! processed by numpydoc !!


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.control.gfm._power_synchronization.PSCtrlPars
   motulator.control.gfm._power_synchronization.PSCtrl
   motulator.control.gfm._power_synchronization.PowerCalc
   motulator.control.gfm._power_synchronization.PowerSynch
   motulator.control.gfm._power_synchronization.CurrentCtrl
   motulator.control.gfm._power_synchronization.DCVoltageControl




.. py:class:: PSCtrlPars


   
   power synchronization control(PSC-)based parameters.
















   ..
       !! processed by numpydoc !!

.. py:class:: PSCtrl(pars)


   Bases: :py:obj:`motulator.control._common.Ctrl`

   
   Grid forming control (PSC) with the power synchronization loop and a current
   loop implemented as in [1].

   Can be combined with the DC-voltage controller as well.

   :param pars: Control parameters.
   :type pars: PSCtrlPars















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


.. py:class:: DCVoltageControl(pars)


   
   DC voltage controller

   This class is used to generate the active power reference for the converter
   controller to ensure that the DC voltage is regulated.















   ..
       !! processed by numpydoc !!
   .. py:method:: output(u_dc_ref, u_dc)

      
      Compute the active power reference sent to the converter control system
      to regulate the DC-bus voltage.

      :param u_dc_ref: DC-bus voltage reference
      :type u_dc_ref: float
      :param u_dc: DC-bus voltage
      :type u_dc: float

      :returns: * **err_dc** (*float*) -- DC capacitance energy error signal
                * **p_dc_ref** (*float*) -- power reference based on DC voltage controller (W)
                * **p_dc_ref_lim** (*float*) -- saturated power reference based on DC voltage controller (W)















      ..
          !! processed by numpydoc !!

   .. py:method:: update(err_dc, p_dc_ref, p_dc_ref_lim)

      
      Update the state of the DC-voltage controller with anti-windup.

      :param err_dc: DC capacitance energy error signal
      :type err_dc: float
      :param p_dc_ref: power reference based on DC voltage controller
      :type p_dc_ref: float
      :param p_dc_ref_lim: saturated power reference based on DC voltage controller
      :type p_dc_ref_lim: float















      ..
          !! processed by numpydoc !!


