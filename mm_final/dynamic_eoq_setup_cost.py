
inputDict = {
    "periods" : [1, 2, 3],
    "demand" : [3, 2, 4],
    "setup" : [3, 7, 6],
    "holding": [1, 3, 2]
}

def findCost(z, s):
  if z == 0:
    return 0
  elif z <= 3:
    return (10*z) + s
  else:
    return (30 + 20*(z-3)) + s

def baseInventory():
  demand = inputDict['demand'][0]
  xList = [1]

  maxRange = sum(inputDict['demand']) - demand
  diffOrder = demand - xList[0]
  holdingCost = inputDict['holding'][0]
  setupCost = inputDict['setup'][0]
  baseMinInventCost = []

  for x in range(0,maxRange + 1):
    hx = holdingCost * x
    z = x + diffOrder
    CZ = findCost(z, setupCost)
    fx = CZ + hx
    baseMinInventCost.append(fx)

  return baseMinInventCost

def helper(period,MinInvestCost):
  demand = inputDict['demand'][period - 1]

  maxRange = 0
  for i in range(period, len(inputDict['demand'])):
    maxRange += inputDict['demand'][i]

  diffZ = demand

  zMaxRange = maxRange + diffZ
  setupCost = inputDict['setup'][period - 1]
  holdingCost = inputDict['holding'][period -1]

  finalFxList = []

  for x in range(0, maxRange + 1):
    fxList = []
    for z in range(0, x + diffZ + 1):
      hx = holdingCost * x
      CZ = findCost(z, setupCost)
      fxList.append(CZ + hx + MinInvestCost[x - z + demand])
    finalFxList.append(min(fxList))

  return finalFxList

MinInvestCost = baseInventory()
print("The optimum costs at period 1 is f1(x2)",MinInvestCost)
for p in range(2, len(inputDict['periods']) + 1):
  MinInvestCost = helper(p,MinInvestCost)
  print("The optimum costs at period",p,"is f( x",p+1,")",MinInvestCost)

print("The optimal cost is ",MinInvestCost[0])