import matplotlib.pyplot as plt
import numpy as np

seq1 = "GACTAGGC" # row
seq2 = "AGCTAGGA" # col

def create_dot_matrix_representation(seq1, seq2):
  seq_mat = []
  for c1 in seq1:
    seq_mat.append([])
    for c2 in seq2:
      if c1 == c2:
        seq_mat[-1].append(1)
      else:
        seq_mat[-1].append(0)
  return seq_mat

seq_mat = create_dot_matrix_representation(seq1, seq2)

fig, ax = plt.subplots()
ax.matshow(seq_mat, cmap='Greys', aspect='auto')

for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq_mat[i][j] == 1:
            ax.text(j, i, seq1[i], ha='center', va='center', color='green')

ax.set_xticks(np.arange(len(seq2)))
ax.set_yticks(np.arange(len(seq1)))
ax.set_xticklabels(seq2)
ax.set_yticklabels(seq1)

ax.set_title('Dot Matrix Representation')
plt.show()

"""Needleman-Wunsch Algorithm"""

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

for v in sol:
  print(v)

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

for s in sol:
  print(s)

print(i, j)

construct_sequence_matching_smith_waterman(sol, i, j, seq1, seq2, dp_mat)



"""Practice"""

seq1 = "CGTGAATTCAT"
seq2 = "GACTTAC"

mtch = 5
mis_mtch = -3
gap = -4

def practice_calc(seq1, seq2):
  # init
  dp_mat = [[0 for _ in range(len(seq1)+1)] for __ in range(len(seq2)+1)]

  for i in range(len(seq1)+1):
    dp_mat[0][i] = 0

  for j in range(len(seq2)+1):
    dp_mat[j][0] = 0

  # max score calc
  for i in range(1, len(seq2)+1):
    for j in range(1, len(seq1)+1):
      lft = dp_mat[i][j-1] + gap
      up = dp_mat[i-1][j] + gap
      diag = 0

      if seq2[i-1] == seq1[j-1]:
        diag = dp_mat[i-1][j-1] + mtch
      else:
        diag = dp_mat[i-1][j-1] + mis_mtch

      dp_mat[i][j] = max(max(lft, 0), max(up, 0), max(diag, 0))


  starti = 0
  startj = 0
  max_val = 0

  for i in range(1, len(seq2)+1):
    for j in range(1, len(seq1)+1):
      if dp_mat[i][j] > max_val:
        max_val = dp_mat[i][j]
        starti = i
        startj = j


  # traceback
  sol = [ ["" if _==0 else "lft-" for _ in range(len(seq1)+1)] ]
  for i in range(1, len(seq2)+1):
    sol.append(["-up-"])
    for j in range(1, len(seq1)+1):
      if seq2[i-1] == seq1[j-1]:
        sol[-1].append("diag")
      else:
        lft = dp_mat[i][j-1]
        up = dp_mat[i-1][j]
        diag = dp_mat[i-1][j-1]

        if up>=lft and up>=diag:
          sol[-1].append("-up-")
        elif lft>=up and lft>=diag:
          sol[-1].append("lft-")
        else:
          sol[-1].append("diag")

  return sol, dp_mat, starti, startj


def print_seq(sol, seq1, seq2, starti, startj, dp_mat):
  i = starti
  j = startj

  new_seq1 = ''
  new_seq2 = ''
  score = 0

  while i>0 and j>0:
    if dp_mat[i][j] == 0:
      break
    if seq1[j-1] == seq2[i-1]:
      score+=mtch

      new_seq1+= seq1[j-1]
      new_seq2+= seq2[i-1]
      i-=1
      j-=1
    elif sol[i][j] == "diag":
      score+=mis_mtch

      new_seq1+= seq1[j-1]
      new_seq2+= seq2[i-1]
      i-=1
      j-=1
    elif sol[i][j] == "-up-":
      score+=gap

      new_seq2+= seq2[i-1]
      new_seq1+= '-'
      i-=1
    elif sol[i][j] == "lft-":
      score+=gap

      new_seq1+= seq1[j-1]
      new_seq2+= '-'
      j-=1

  print(f"{new_seq1[::-1]}")
  print(f"{new_seq2[::-1]}")
  print(f"score: {score}")

sol, dp_mat, starti, startj = practice_calc(seq1, seq2)

print_seq(sol, seq1, seq2, starti, startj, dp_mat)

