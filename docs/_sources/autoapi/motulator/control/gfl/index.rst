:py:mod:`motulator.control.gfl`
===============================

.. py:module:: motulator.control.gfl

.. autoapi-nested-parse::

   
   This package contains example controllers for grid following converters.
















   ..
       !! processed by numpydoc !!


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   motulator.control.gfl.GridFollowingCtrl
   motulator.control.gfl.GridFollowingCtrlPars




.. py:class:: GridFollowingCtrl(pars)


   Bases: :py:obj:`motulator.control._common.Ctrl`

   
   Grid following control with the current controller and PLL to synchronize
   with the AC grid.

   :param pars: Control parameters.
   :type pars: GridFollowingCtrlPars

   .. rubric:: References

   .. [#Har2009] L. Harnefors and M. Bongiorno, "Current controller design
      for passivity of the input admittance," 2009 13th European Conference
      on Power Electronics and Applications, Barcelona, Spain, 2009, pp. 1-8.















   ..
       !! processed by numpydoc !!

.. py:class:: GridFollowingCtrlPars


   
   grid-following control parameters.
















   ..
       !! processed by numpydoc !!

