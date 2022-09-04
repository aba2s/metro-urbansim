# metro-urbansim
Goal
====
This project is to make a bridge beetwen Metropolis and UrbanSim

Metropolis
==========
METROPOLIS is a simulator of road congestion and affluence in public transport, used by organizations such as the "Société du Grand Paris" for the evaluation of projects.

UrbanSim
========

.. image:: https://img.shields.io/pypi/v/urbansim.svg
    :target: https://pypi.python.org/pypi/urbansim/
    :alt: Latest Version

.. image:: https://travis-ci.org/UDST/urbansim.svg?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/UDST/urbansim

.. image:: https://coveralls.io/repos/UDST/urbansim/badge.svg?branch=master
   :alt: Test Coverage
   :target: https://coveralls.io/r/UDST/urbansim?branch=master

UrbanSim is a platform for building statistical models of cities and regions. These models help forecast long-range patterns in real estate development, demographics, and related outcomes, under various policy scenarios.

This ``urbansim`` Python library is a core component. It contains tools for statistical estimation and simulation; domain-specific logic about housing markets, household relocation, and other processes; and frameworks and utilities for assembling a model. 

How it works
------------

Operational UrbanSim models begin with detailed data about a particular region, and then estimate and validate a system of interconnected model components. Full models draw on a number of libraries: not just ``urbansim``, but also `Orca <https://github.com/UDST/orca>`__ for task orchestration, `Synthpop <https://github.com/UDST/synthpop>`__ for population synthesis, `Pandana <https://github.com/UDST/pandana>`__ for network analysis, and so on. Collectively, these make up the `Urban Data Science Toolkit <https://github.com/UDST>`__ (UDST).

UrbanSim models are used by public agencies, consultancies, and researchers in dozens of cities around the U.S. and world. The core platform is open source, but many operational models make use of additional cloud-hosted model building and visualization tools provided by `UrbanSim Inc. <https://urbansim.com>`__

