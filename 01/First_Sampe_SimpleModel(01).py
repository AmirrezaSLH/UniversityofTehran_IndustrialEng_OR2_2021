# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 23:33:47 2021

@author: Amirreza
"""

from pyomo.environ import *

#M1 = AbstractModel()

M = ConcreteModel() #data

#set
M.IDX = RangeSet(3) # 1 , 2 , 3

#variable

M.x = Var( M.IDX , within = NonNegativeReals)   #Binary, NonNegativeInteger , ....

#Objective Function

M.obj = Objective( expr= 8*M.x[1] + 6*M.x[2]+ 5*M.x[3], sense = maximize)

#Constraints

M.ST = ConstraintList()

M.ST.add(M.x[1] + 2*M.x[2] +M.x[3] <= 5)
M.ST.add(2* M.x[1] - M.x[2] + M.x[3] <= 3)

solver = SolverFactory('ipopt')
solver.solve(M)
display(M)
