# AI planner
This repository contains code for reading and solving STRIPS planning problems defined in PDDL. This code was written from scratch as a part of a master thesis merging robotics and AI planning.

The solver supports basic search algorithm for solving planning problems:
* Breadth First Search
* Depth First Search
* Best-first search
* A*
* Weighted A*

The heuristics available for the guided search algorithms are:
* Number of missing sub goals
  * The number of sub goals left to be completed are used as an estimate of the distance to the solution
* Relaxed problem heuristic
  * This heuristic is based on solving a relaxed problem of the initial problem by ignoring the delete lists. The length of the solution is used as an estimated of the distance to the solution of the original problem.

## Initial setup
The code works with Python 2.7

Only Python standard libraries have been used, so it should not be necessary to install anything.

## Use
To solve a problem:
1. open *src/main.py"
2. Define the paths to the *domain.pddl* and *problem.pddl*.
3. Choose solving method
4. run *src/main.py*

There are already some examples in the main file to use and look at if something is unclear.
