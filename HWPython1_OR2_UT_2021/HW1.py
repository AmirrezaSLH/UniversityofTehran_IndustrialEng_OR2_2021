# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:33:31 2021

@author: Amirreza
"""

from pyomo.environ import *

HW1 = ConcreteModel() 

#Data

I = 7

Cost = [7, 5 ,8 ,12, 9, 6, 13]
Income = [30, 26, 25, 41, 36, 24, 38]

#Sets

HW1.IDX = RangeSet(I)

#Var
HW1.x = Var(HW1.IDX, within = Binary)

#Objective Function
HW1.obj = Objective( expr = sum( ((Income[i-1]-Cost[i-1]) * HW1.x[i]) for i in HW1.IDX ) , sense = maximize )

#Constraints

HW1.ST = ConstraintList()

HW1.ST.add(sum(HW1.x[i] for i in HW1.IDX) <= 5 )
HW1.ST.add( HW1.x[3] >= HW1.x[4] )
HW1.ST.add( HW1.x[7] + HW1.x[1] <=1 )

solver = SolverFactory('cplex')
solver.solve(HW1)
display(HW1)


