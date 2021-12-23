# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 00:06:43 2021

@author: Amirreza Salehi
"""

from pyomo.environ import *
import matplotlib.pyplot as plt

M = ConcreteModel()

M.IDX = RangeSet(0,7)

C = [ 54, 57, 48, 42, 42, 42, 42, 45]
D = [ 5, 7, 15, 21, 22, 12, 7, 3]

M.C = Param( M.IDX, initialize = C, mutable =True)
M.D = Param(M.IDX, initialize = D, mutable =True)

M.x = Var(M.IDX, within = NonNegativeReals)
M.obj = Objective( expr = sum( M.C[i]*M.x[i] for i in M.IDX), sense = minimize)
M.ST = ConstraintList()

for i in M.IDX:
    if i == 0:
        M.ST.add( M.x[i] + M.x[i+7] >= M.D[i] )
    else:
        M.ST.add( M.x[i] + M.x[i-1] >= M.D[i] )
        
X = []
Y = []
        
for i in range(15):
    M.C[2] = i*i 
    opt = SolverFactory('cplex')
    results = opt.solve(M)      
    print( value(M.obj) )
    X.append( value(M.C[2]) )
    Y.append( value(M.obj)) 

plt.plot(X,Y)
plt.title('OR S3')
plt.xlabel('Costs')
plt.ylabel('OBJ function')
plt.show()
