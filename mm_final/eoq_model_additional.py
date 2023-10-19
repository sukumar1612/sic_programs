import numpy as np
import matplotlib.pyplot as plt

"""EOQ with price breaks"""

import math
c1 = 3
c2 = 2.5
q = 1000
c = lambda y: c1 if y<=q else c2
D = 187.5
K = 20
h = 0.02

def TCU(y):
  return D*c(y) + K*D/y + h*y/2

print(f"ym = {math.sqrt(2*K*D/h)}")

plt.plot([i for i in range(500, 750)], [TCU(i) for i in range(500, 750)])
  plt.xlabel('Produced')
  plt.ylabel('Cost')
  plt.show()

def TCU1(y):
  return D*c1 + K*D/y + h*y/2

def TCU2(y):
  return D*c2 + K*D/y + h*y/2

plt.plot([i for i in range(500, 750)], [TCU1(i) for i in range(500, 750)])
  plt.xlabel('Produced')
  plt.ylabel('Cost')
  plt.show()

plt.plot([i for i in range(500, 750)], [TCU2(i) for i in range(500, 750)])
  plt.xlabel('Produced')
  plt.ylabel('Cost')
  plt.show()

"""Classical EOQ Model"""

import math

D = 100 # demand unit qty
k = 100 # setup cost $
h = 0.02 # holding cost $
L = 12 # time

y_star = math.sqrt(2*k*D/h)
t0 = y_star/D

n = math.floor(L/t0)

L_effective = L - n*t0

L_effective

reorder_time = L_effective * D

reorder_time

print(f"Order {y_star} units whenever the inventory level drops to {reorder_time} units.")

"""EOQ with price breaks"""

c1 = 3.0
c2 = 2.5
q = 1000
c = lambda y: c1 if y<=q else c2
D = 150 * 1.25
h = 0.02
k = 20
L = 2

ym = math.sqrt(2*k*D/h)
ym

# eqn = Q**2 + 375000.0 + Q*10599.74

(2*D*c2 - (D*c1 + k*D/ym + h*ym/2))/h

(10599.74+(10599.74**2 - 4*1*375000.0)**0.5)/2*1

Q = 10564.242898731623

y_star = q

print(f"Order {y_star} units whenever the inventory level drops to {L*D} units.")

"""Multi-Item EOQ with Storage Limitation"""

import math
from matplotlib import pyplot as plt
import numpy as np
import sympy as sp

K = sp.Array([10,5,15])
a = sp.Array([1,1,1])
D = sp.Array([2,4,4])
h = sp.Array([0.3,0.1,0.2])
A = 25
n = 3
y = sp.IndexedBase('y')
i,k = sp.symbols('i k')
z = sp.summation(K[i]*D[i]/y[i]+h[i]*y[i]/2, (i,0,n-1))
c = sp.summation(a[i]*y[i],(i,0,n-1))-A

z



"""Dynamic EOQ Models (No Setup Cost)"""

init_matrix = [
    [90, 50, 100],
    [100, 60, 190],
    [120, 80, 210],
    [110, 70, 160]
]

def dynamic_eoq_no_setup(init_matrix):
  regular = 6
  overtime = 9
  holding_cost = 0.10
  cost_matrix=[]
  inventory_matrix = []

  # construct cost matrix
  for idx, i in enumerate(init_matrix):
    print(idx)
    cost_matrix.append([0 for _ in range(len(init_matrix)+1)])
    # regular
    for j in range(idx, len(init_matrix)):
      cost_matrix[-1][j] = regular + (j-idx)*holding_cost

    cost_matrix.append([0 for _ in range(len(init_matrix)+1)])
    # overtime
    for j in range(idx, len(init_matrix)):
      cost_matrix[-1][j] = overtime + (j-idx)*holding_cost

  # construct inventory matrix
  for idx, mtx in enumerate(init_matrix):
    inventory_matrix.append([0 for _ in range(len(init_matrix)+1)])
    inventory_matrix.append([0 for _ in range(len(init_matrix)+1)])
    demand = mtx[2]

    # regular
    if max(demand - mtx[0], 0) > 0:
      inventory_matrix[-2][idx] = mtx[0]
    else:
      inventory_matrix[-2][idx] = demand
      inventory_matrix[-2][-1] = mtx[0] - demand
    demand = max(demand - mtx[0], 0)

    # overtime
    if max(demand - mtx[1], 0) > 0:
      inventory_matrix[-1][idx] = mtx[1]
    else:
      inventory_matrix[-1][idx] = demand
      inventory_matrix[-1][-1] = mtx[1] - demand
    demand = max(demand - mtx[1], 0)

    # if demand is not satisfied by existing capacity
    if demand > 0:
      inv_len = len(inventory_matrix)
      cost_list = []
      for x in range(inv_len-2):
        cost_list.append(cost_matrix[x][idx])
      print(f"---demand: {demand}---")
      sorted_cost_list = sorted(cost_list)
      print(cost_list)
      print(sorted_cost_list)

      for scst in sorted_cost_list:
        for idx_cst, cst in enumerate(cost_list):
          if scst == cst:
            remaining_capacity = inventory_matrix[idx_cst][-1]
            if demand > remaining_capacity:
              demand = demand - remaining_capacity
              inventory_matrix[idx_cst][-1] = 0
              inventory_matrix[idx_cst][idx] = remaining_capacity
            else:
              inventory_matrix[idx_cst][-1] = remaining_capacity - demand
              inventory_matrix[idx_cst][idx] = demand
              demand = 0
          if demand == 0:
            break
        if demand == 0:
          break

      print("---")

  return cost_matrix, inventory_matrix

transportation_matrix, inventory_matrix = dynamic_eoq_no_setup(init_matrix)

print("----------------------------")
for t in transportation_matrix:
  print(t)

print("----------------------------")
for i in inventory_matrix:
  print(i)
print("----------------------------")

def total_cost(transportation_matrix, inventory_matrix):
  cost = 0
  for trsn_mat, ivn_mat in zip(transportation_matrix, inventory_matrix):
    for cst, qty in zip(trsn_mat, ivn_mat):
      cost+=cst*qty

  print(f"total cost is : {cost}")

total_cost(transportation_matrix, inventory_matrix)

"""Dynamic EOQ Models (Setup Cost)"""

init_mat = [
    [3,3,1],
    [2,7,3],
    [4,6,2]
]

def ci_zi(zi, ki):
  if zi == 0:
    return 0
  if zi <=3:
    return ki+10*zi
  return ki+30+20*(zi-3)

x1 = 1
# di, ki, hi

def initial_case_i_1(init_mat):
  x2_range = sum([init_mat[i][0] for i in range(1, len(init_mat))])
  z1 = lambda x2, d1, x1: x2 + d1 - x1
  dp_table = [[]]
  d1 = init_mat[0][0]
  k1 = init_mat[0][1]
  h1 = init_mat[0][-1]
  f1_x2 = lambda ci_zi, h1_x2: ci_zi + h1_x2

  for x2 in range(0, x2_range+1):
    dp_table[0].append([x2, h1*x2, f1_x2(ci_zi(z1(x2, d1, x1), k1), h1*x2), z1(x2, d1, x1)])

  for t in dp_table[0]:
    print(t)

  return dp_table

def fi_xi_1(hi, di, ki, zi, xi_1, dp_table, i):
  min_val = 10**10
  z_star = 0
  for z in range(zi+1):
    v = ci_zi(z, ki) + hi*xi_1 + dp_table[i-1][xi_1 + di - z][2]
    if v < min_val:
      min_val = v
      z_star = z

  return min_val, z_star

def case_i_gt_1(init_mat, period_i, dp_table):
  period_i = period_i - 1
  di = init_mat[period_i][0]
  ki = init_mat[period_i][1]
  hi = init_mat[period_i][-1]

  dp_table.append([])
  xi = sum([init_mat[i][0] for i in range(period_i+1, len(init_mat))])
  for x in range(xi+1):
    zi = di + x
    min_val, z_star =  fi_xi_1(hi, di, ki, zi, x, dp_table, period_i)
    dp_table[-1].append([x, x*hi, min_val, z_star])

  return dp_table

dp_table = initial_case_i_1(init_mat)

dp_table = case_i_gt_1(init_mat, 2, dp_table)

dp_table = case_i_gt_1(init_mat, 3, dp_table)

dp_table

import sympy as sp

K = sp.Array([10, 5, 15])
D = sp.Array([2, 4, 4])
H = sp.Array([0.3, 0.1, 0.2])

a = sp.Array([1, 1, 1])
y = sp.IndexedBase('y')
A = 25
i = sp.symbols('i')
n = 3

z = sp.summation(K[i]*D[i]/y[i] + H[i]*y[i]/2, (i, 0, n-1)) # optimize
c = sp.summation(a[i]*y[i], (i, 0, n-1)) - A # constraint

z

c

[L for j in range(n)]

lamda = sp.symbols('lambda')
L = z - c*lamda
gradL = [sp.diff(L, y[j]) for j in range(n)] + [sp.diff(L, lamda)]
gradL

sp.nsolve(gradL, [y[i] for i in range(n)] + [lamda], [11.5,20,24.49,0.01])

"""Probabilistic EOQ"""

