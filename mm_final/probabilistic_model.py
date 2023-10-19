import sympy as sp
import math

x, R, yi = sp.symbols('x R yi')

D = 1000
K = 100
h = 2
p = 10

func1 = (x-R)/100
a = R
b = 100
S = sp.integrate(func1, (x, a, b))
print(f"Result: {S}")

func2 = 1/100
lhs = sp.integrate(func2,(x,a,b))
rhs = (h*yi)/(D*p)
Rsolution = sp.solve(sp.Eq(lhs, rhs), R)
print(f"Solution for R: {Rsolution}")

def iterations(Y_val,R_val,iter):
  print("iteration number is ",iter)
  prevY = Y_val
  prevR = R_val

  s_i = S.subs(R,R_val)
  print("The value of S is ",s_i)

  y_cur = math.sqrt((2*D*(K+(p*s_i)))/h)

  print("the value of y is ",y_cur)

  r_cur = Rsolution[0].subs(yi,y_cur)

  print("The value r is ",r_cur)

  if (prevY - y_cur) < 0.01 and (prevR - r_cur) < 0.01:
    print("\n")
    print("The y* value is ",y_cur)
    print("The R* value is ",r_cur)
    return

  else:
    iterations(y_cur,r_cur,iter+1)

#iteration 1
y1 = math.sqrt((2*D*K)/h)
R1 = Rsolution[0].subs(yi,y1)
print("iteration number is 1")
print("The value of y is ",y1)
print("The value of r is ",R1)

iterations(y1,R1,2)

