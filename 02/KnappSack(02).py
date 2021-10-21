# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:52:57 2021

@author: Amirreza
"""

from pyomo.environ import *

S02 = ConcreteModel()

#Parameters

I = 7
C = [5, 8, 13, 4, 10, 3, 3]
A = [9, 12, 20, 4, 14, 5, 6]
B = 40
#Sets

S02.IDX = RangeSet(I)

#Variables

S02.x = Var( S02.IDX , within = Binary)

#Objective Function

S02.obj = Objective(expr = sum(C[i-1]*S02.x[i] for i in S02.IDX), sense = maximize)

#Constraint

S02.ST = Constraint(expr = sum(A[i-1]*S02.x[i] for i in S02.IDX) <= B )

solver = SolverFactory('cplex')
solver.solve(S02)
display(S02)



