:py:mod:`gritulator.control.grid_forming`
=========================================

.. py:module:: gritulator.control.grid_forming

.. autoapi-nested-parse::

   
   This package contains example controllers for grid forming converters.
















   ..
       !! processed by numpydoc !!


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   gritulator.control.grid_forming.PSCCtrl
   gritulator.control.grid_forming.PSCCtrlPars




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

.. py:class:: PSCCtrlPars


   
   Parameters for the control system.
















   ..
       !! processed by numpydoc !!

