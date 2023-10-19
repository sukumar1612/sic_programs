
import sympy as sp
import math

y, D = sp.symbols('y D')
alpha = 0.9
p = 10
r = 10
c = 8
h = 1

function = 0.08*D
a = 0
b = y
S = sp.integrate(function, (D, a, b))
print(f"Result: {S}")

rhs = (p + (1 - alpha)*(r - c))/(p + h + (1 - alpha) * r)
print("=",rhs)

solution = sp.solve(sp.Eq(S, rhs), y)

#print(solution)

final_ans =0
for i in solution:
  if i > 0:
    final_ans = i

print("order ",final_ans,"-x if x<= ",final_ans)
print("else order 0")

