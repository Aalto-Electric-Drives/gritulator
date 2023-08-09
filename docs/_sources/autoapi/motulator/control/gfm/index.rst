:py:mod:`motulator.control.gfm`
===============================

.. py:module:: motulator.control.gfm

.. autoapi-nested-parse::

   
   This package contains example controllers for grid forming converters.
















   ..
       !! processed by numpydoc !!


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.control.gfm.PSCtrl
   motulator.control.gfm.PSCtrlPars




.. py:class:: PSCtrl(pars)


   Bases: :py:obj:`motulator.control._common.Ctrl`

   
   Grid forming control (PSC) with the power synchronization loop and a current
   loop implemented as in [1].

   Can be combined with the DC-voltage controller as well.

   :param pars: Control parameters.
   :type pars: PSCtrlPars















   ..
       !! processed by numpydoc !!

.. py:class:: PSCtrlPars


   
   power synchronization control(PSC-)based parameters.
















   ..
       !! processed by numpydoc !!

