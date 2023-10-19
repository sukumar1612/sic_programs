

import math

D=200 #N(D,sigma) given in question
sig = 20
h = 0.04
K = 100
L = 7
alpha = 0.02

y_star = math.sqrt(2*K*D/h)

t_star = y_star/D

Le=0
if L>t_star:
  Le =  L - math.floor(L/t_star)*t_star

mu_l = D*Le
sigma_l = math.sqrt(Le*sig*sig)

K_alpha = 2.05 #find using alpha value

B = round(sigma_l*K_alpha)

B

print("The optimal inventory policy is order",y_star,"units when inventory drops to",B+mu_l,"units")

