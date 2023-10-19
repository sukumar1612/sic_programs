I={"p":[1,2,3,4,5,6],"D":[10,15,7,20,13,25],"K":[20,17,10,18,5,50],"h":[1,1,1,3,1,1]}

List_of_Tc = {}
for i in range(1,len(I["p"])+1):
  for j in range(i,len(I["p"])+1):
    if i==j:
      List_of_Tc[str(i)+str(j)] = I["K"][i-1]
    else:
      List_of_Tc[str(i)+str(j)] = 0
      holding_sum=0
      for k in range(i,j):
        holding_sum+= I["h"][k-1]
      holding_sum*= I["D"][j-1]
      holding_sum+= List_of_Tc[str(i)+str(j-1)]
      List_of_Tc[str(i)+str(j)] = holding_sum


sum=0
cummulative_demand=[]
cummulative_demand.append(0)
for i in range(1,len(I["D"])+1):
  sum+=I["D"][i-1]
  cummulative_demand.append(sum)

quantity=0

List_of_TCU = []
i=1
Units=[]
while(i<=len(I["p"])):

  if i == len(I["p"]):
    quantity += cummulative_demand[i] - cummulative_demand[i-1]
    break

  t=i
  while(1):
    flag=0
    print("i val ",i," t val ",t)
    Tcu = List_of_Tc[str(i)+str(t)]/(t-i+1)

    List_of_TCU.append(Tcu)
    print(List_of_TCU)
    if len(List_of_TCU)>2 and i!=0:
      for j in range(i,len(List_of_TCU)-1):
        if List_of_TCU[j] < List_of_TCU[j-1] and List_of_TCU[j] < List_of_TCU[j+1]:
          print("local minima occurs at",t-1)
          print("demand to be ordered in iteration ",i,"is ",cummulative_demand[t-1] - cummulative_demand[i-1])
          quantity+=cummulative_demand[t-1] - cummulative_demand[i-1]
          i=t
          flag=1
          break;

    t=t+1
    if flag==1:
      break


#print(List_of_Tc)

print("the final order quantity is ",quantity)

