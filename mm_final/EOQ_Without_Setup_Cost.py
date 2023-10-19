#input dictionary
inputDict = {"Month":[1,2,3,4], "Regular":[90,100,120,110], "Overtime":[50,60,80,70], "Demand":[100,190,210,160]}

rows = len(inputDict['Month']) * 2
cols = len(inputDict['Month'])

mat = []
for i in range(rows):
    tempList = []
    for j in range(cols):
        tempList.append(0)
    mat.append(tempList)
    
demand = inputDict['Demand']
regular = inputDict['Regular']
overtime = inputDict['Overtime']

#exhaust regular demand
for i in range(cols):
    output = min(demand[i], regular[i])
    demand[i] -= output
    regular[i] -= output
    mat[i*2][i] = output
    
    if(demand[i] > 0):
        for j in reversed(range(i)):
            output = min(demand[i], regular[j])
            if(output > 0):
                demand[i] -= output
                regular[j] -= output
                mat[j*2][i] = output

#exhaust overtime demand
for i in range(cols):
    output = min(demand[i], overtime[i])
    demand[i] -= output
    overtime[i] -= output
    mat[(i*2) + 1][i] = output
    
    if(demand[i] > 0):
        for j in reversed(range(i)):
            output = min(demand[i], overtime[j])
            if(output > 0):
                demand[i] -= output
                overtime[j] -= output
                mat[(j*2) + 1][i] = output

print(mat)
#find surplus
surplus = 0
for i in range(cols):
    surplus += regular[i]
    surplus += overtime[i]

print(surplus)

totalCost = 0

for i in range(rows):
    idx = 0
    for j in range(i//2, cols):
        if i%2 == 0:
            totalCost += mat[i][j] * (6 + (idx * 0.1))
        else:
            totalCost += mat[i][j] * (9 + (idx * 0.1))
        idx += 1

print(totalCost)