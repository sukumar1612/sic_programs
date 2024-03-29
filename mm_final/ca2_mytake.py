# -*- coding: utf-8 -*-
"""ca2_mytake.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LbLC0LLOvhSzjUURe18Ouw-2pc8vsbmD
"""

import numpy as np

"""Classical EOQ"""

D = 100
K = 100
h = 0.02
L = 12

ystar = np.sqrt(2*K*D/h)

ystar

t0 = ystar/D

L - np.floor(L/t0)*t0

(L - np.floor(L/t0)*t0)*D

"""Price Break"""

c1 = 3.0
c2 = 2.5
q = 1000
c = lambda y: c1 if y<=q else c2
D = 150 * 1.25
h = 0.02
k = 20
L = 2

ym = math.sqrt(2*k*D/h)

(2*D*c2 - (D*c1 + k*D/ym + h*ym/2))/h

(10599.74+(10599.74**2 - 4*1*375000.0)**0.5)/2*1

Q = 10564.242898731623

y_star = q

print(f"Order {y_star} units whenever the inventory level drops to {L*D} units.")

"""Multi EOQ"""

import math
from matplotlib import pyplot as plt
import numpy as np
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

lamda = sp.symbols('lambda')
L = z - c*lamda
gradL = [sp.diff(L, y[j]) for j in range(n)] + [sp.diff(L, lamda)]
gradL

sp.nsolve(gradL, [y[i] for i in range(n)] + [lamda], [11.5,20,24.49,0.01])

"""Dynamic EOQ

NO Setup Cost
"""

init_matrix = [
    [90, 50, 100],
    [100, 60, 190],
    [120, 80, 210],
    [110, 70, 160]
]
h = 0.1

regular = 6
overtime = 9

def dynamic_eoq_no_setup(init_matrix, h, regular, overtime):
  # construct cost matrix
  cost_matrix = []
  inventory_matrix = []

  for i in range(len(init_matrix)):
    cost_matrix.append([0 for _ in range(len(init_matrix) + 1)])
    cost_matrix.append([0 for _ in range(len(init_matrix) + 1)])

    inventory_matrix.append([0 for _ in range(len(init_matrix) + 1)])
    inventory_matrix.append([0 for _ in range(len(init_matrix) + 1)])

    cost = regular
    for j in range(i, len(init_matrix)):
      cost_matrix[-2][j] = round(cost, 2)
      cost+=h

    cost = overtime
    for j in range(i, len(init_matrix)):
      cost_matrix[-1][j] = round(cost, 2)
      cost+=h

    # demand
    inventory_matrix[-2][-1] = init_matrix[i][0]
    inventory_matrix[-1][-1] = init_matrix[i][1]

  # construct inventory matrix
  for i in range(len(init_matrix)):
    regular_supply = init_matrix[i][0]
    overtime_supply = init_matrix[i][1]

    demand = init_matrix[i][2]

    max_depth = i*2 + 1
    cost_list = []
    for j in range(max_depth+1):
      cost_list.append(cost_matrix[j][i])

    sorted_cost_list = sorted(cost_list, key=lambda x: x)

    for scslt in sorted_cost_list:
      for idx, cslt in enumerate(cost_list):
        if cslt == scslt:
          if inventory_matrix[idx][-1] >= demand:
            inventory_matrix[idx][-1] = inventory_matrix[idx][-1] - demand
            inventory_matrix[idx][i] = demand
            demand = 0
          else:
            demand = demand - inventory_matrix[idx][-1]
            inventory_matrix[idx][i] = inventory_matrix[idx][-1]
            inventory_matrix[idx][-1] = 0

  for i in cost_matrix:
    print(i)

  print("\n\n---------------------\n\n")
  for i in inventory_matrix:
    print(i)


  cost = 0
  for i, j in zip(inventory_matrix, cost_matrix):
    for x, y in zip(i, j):
      cost += x*y

  print(f"\n\n total cost: {cost}")

dynamic_eoq_no_setup(init_matrix, h, regular, overtime)

"""Setup EOQ"""

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

"""Bioinformatics

Needleman
"""

seq1 = "CGTGAATTCAT"
seq2 = "GACTTAC"

mtch = 1
mis_mtch = -1
gap = -2

def cal_dp_matrix_val_needleman_wunsch(seq1, seq2):
  dp_mat = [[0 for _ in range(len(seq1)+1)] for _ in range(len(seq2)+1)]
  # initialization stage
  for i in range(len(seq1)+1):
    dp_mat[0][i] = gap*i

  for j in range(len(seq2)+1):
    dp_mat[j][0] = gap*j

  # max score filling

  for i in range(1, len(seq2)+1):
    for j in range(1, len(seq1)+1):
      lft = dp_mat[i][j-1] + gap
      rght = dp_mat[i-1][j] + gap
      diag = 0
      if seq1[j-1] == seq2[i-1]:
        diag = dp_mat[i-1][j-1] + mtch
      else:
        diag = dp_mat[i-1][j-1] + mis_mtch

      dp_mat[i][j] = max(lft, rght, diag)

  sol = [["-" if _==0 else "lft-" for _ in range(0, len(seq1)+1)]]
  # traceback
  for i in range(1, len(seq2)+1):
    sol.append(["-up-"])
    for j in range(1, len(seq1)+1):
      up = dp_mat[i-1][j]
      lft = dp_mat[i][j-1]
      diag = dp_mat[i-1][j-1]
      if seq1[j-1] == seq2[i-1]:
        sol[-1].append("diag")
      else:
        if up>=lft and up>=diag:
          sol[-1].append("-up-")
        elif lft>=up and lft>=diag:
          sol[-1].append("lft-")
        else:
          sol[-1].append("diag")

  dp_mat = np.array(dp_mat)
  np.set_printoptions(precision=4, suppress=True, linewidth=100)
  for d in dp_mat:
    print(d)

  return sol

def construct_sequence_matching_needleman_wunsch(sol, seq1, seq2):
  new_seq1 = ''
  new_seq2 = ''

  i = len(seq2)
  j = len(seq1)

  score = 0

  while i>0 and j>0:
    if sol[i][j] == "diag":
      if seq1[j-1] == seq2[i-1]:
        score+=mtch
      else:
        score+=mis_mtch

      new_seq1+=seq1[j-1]
      new_seq2+=seq2[i-1]
      i=i-1
      j=j-1

    elif sol[i][j] == "lft-":
      new_seq1+=seq1[j-1]
      new_seq2+='-'
      j=j-1
      score+=gap
    else:
      new_seq1+='-'
      new_seq2+=seq2[i-1]
      i=i-1
      score+=gap

  while i>0:
    new_seq1+='-'
    new_seq2+=seq2[i-1]
    i=i-1
    score+=gap

  while j>0:
    new_seq1+=seq1[j-1]
    new_seq2+='-'
    j=j-1
    score+=gap

  # print(f"{new_seq1[::-1]}")
  # print(f"{new_seq2[::-1]}")
  # print(f"score: {score}")
  return score, new_seq1[::-1], new_seq2[::-1]

sol = cal_dp_matrix_val_needleman_wunsch(seq1, seq2)

construct_sequence_matching_needleman_wunsch(sol, seq1, seq2)

"""Smith Waterman"""

seq1 = "CGTGAATTCAT"
seq2 = "GACTTAC"

mtch = 5
mis_mtch = -3
gap = -4

def cal_dp_matrix_val_smith_waterman(seq1, seq2):
  dp_mat = [[0 for _ in range(len(seq1)+1)] for _ in range(len(seq2)+1)]
  # initialization stage -> all negtive vals = 0 therefore it is all init to 0
  for i in range(len(seq1)+1):
    dp_mat[0][i] = 0

  for j in range(len(seq2)+1):
    dp_mat[j][0] = 0

  # max score filling
  for i in range(1, len(seq2)+1):
    for j in range(1, len(seq1)+1):
      lft = dp_mat[i][j-1] + gap
      rght = dp_mat[i-1][j] + gap
      diag = 0
      if seq1[j-1] == seq2[i-1]:
        diag = dp_mat[i-1][j-1] + mtch
      else:
        diag = dp_mat[i-1][j-1] + mis_mtch

      # all negative vals = 0
      dp_mat[i][j] = max(max(lft, 0), max(rght, 0), max(diag, 0))


  starting_vali = 0
  starting_valj = 0
  starting_max_val = 0

  for i, val in enumerate(dp_mat):
    print(val)
    for j, v in enumerate(val):
      if v > starting_max_val:
        starting_max_val = v
        starting_vali = i
        starting_valj = j

  print(starting_vali, starting_valj)
  sol = [["-" if _==0 else "lft-" for _ in range(0, len(seq1)+1)]]
  # traceback
  for i in range(1, len(seq2)+1):
    sol.append(["-up-"])
    for j in range(1, len(seq1)+1):
      up = dp_mat[i-1][j]
      lft = dp_mat[i][j-1]
      diag = dp_mat[i-1][j-1]
      if seq1[j-1] == seq2[i-1]:
        sol[-1].append("diag")
      else:
        if up>=lft and up>=diag:
          sol[-1].append("-up-")
        elif lft>=up and lft>=diag:
          sol[-1].append("lft-")
        else:
          sol[-1].append("diag")

  return sol, starting_vali, starting_valj, dp_mat

def construct_sequence_matching_smith_waterman(sol, i, j, seq1, seq2, dp_mat):
  new_seq1 = ''
  new_seq2 = ''

  sq1 = j
  sq2 = i
  score = 0

  while i>0 and j>0:
    if dp_mat[i][j] == 0:
      break
    if sol[i][j] == "diag":
      if seq1[j-1] == seq2[i-1]:
        score+=mtch
      else:
        score+=mis_mtch

      new_seq1+=seq1[j-1]
      new_seq2+=seq2[i-1]
      i=i-1
      j=j-1

    elif sol[i][j] == "lft-":
      new_seq1+=seq1[j-1]
      new_seq2+='-'
      j=j-1
      score+=gap
    else:
      new_seq1+='-'
      new_seq2+=seq2[i-1]
      i=i-1
      score+=gap



  print(f"{new_seq1[::-1]}")
  print(f"{new_seq2[::-1]}")
  print(f"score: {score}")

sol, i, j, dp_mat = cal_dp_matrix_val_smith_waterman(seq1, seq2)

construct_sequence_matching_smith_waterman(sol, i, j, seq1, seq2, dp_mat)

