import numpy as np

def generate(flag):

  Inter_arrival=[]

  if flag=='R':
    a=1
    b=3
    m=5
    x0=1
    ele=((a*x0)+b)%m
    for i in range(1,451):
      Inter_arrival.append(ele)
      ele=((a*ele)+b)%m + 1
    return Inter_arrival

  elif flag=='P':
    Inter_arrival = np.random.poisson(5,451)
    return Inter_arrival

def Calculate_Arrival(flag):
  Inter_arrival = generate(flag)
  start=0
  Arriving_time=[]
  for i in range(0,len(Inter_arrival)):
    start+=Inter_arrival[i]
    Arriving_time.append(start)

  return Arriving_time

def Calculate_Waiting_time_one_server(flag):


  rng=np.random.default_rng()
  Service_duration=int(rng.exponential(3,1))+1
  Arriving_time = Calculate_Arrival(flag)
  Waiting_time=0
  Server_idle=Arriving_time[0]
  Service_start=[]
  Service_start.append(Arriving_time[0])

  for i in range(1,len(Arriving_time)):
    Service_start.append(max(Service_duration + Service_start[i-1],Arriving_time[i]))

    if Service_duration + Service_start[i-1] > Arriving_time[i]:
      Waiting_time += Service_duration + Service_start[i-1] - Arriving_time[i]

    elif Service_duration + Service_start[i-1] < Arriving_time[i]:
      Server_idle += Arriving_time[i] - (Service_duration + Service_start[i-1])

    Service_duration=int(rng.exponential(3,1))+1

  customer_server_waiting=[]
  customer_server_waiting.append(Waiting_time)
  customer_server_waiting.append(Server_idle)
  ReturnList=[]
  ReturnList.append(Arriving_time)
  ReturnList.append(Service_start)
  ReturnList.append(customer_server_waiting)

  return ReturnList

def printTime(flag):

  two_d_list = Calculate_Waiting_time_one_server(flag)

  for j in range(0,2):
    time =  two_d_list[j]
    # 12 0 clock
    Timer = 12
    minutes = 0
    for i in range(0,len(time)):
      hr = int(time[i]/60)
      min = time[i]%60

      hour = (Timer+hr)%12

      if(hour==0):
        hour=12

      if j==0:
        print("Customer ",i+1," arrive at ",hour," : ",minutes+min)

      elif j==1:
        print("Service for  Customer ",i+1," starts at ",hour," : ",minutes+min)

  return two_d_list[2]

def main():

  #Random number technique
  customer_server_waiting = printTime('R')
  print("The customer waiting time is ",customer_server_waiting[0])
  print("The server waiting time is ",customer_server_waiting[1])

  #Poisson
  customer_server_waiting = printTime('P')
  print("The customer waiting time is ",customer_server_waiting[0])
  print("The server waiting time is ",customer_server_waiting[1])

main()

"""TWO SERVERS"""

def Calculate_Waiting_time_two_server(flag):

  rng=np.random.default_rng()
  Service_time=int(rng.exponential(3,1))+1
  Arriving_time_2_severs = Calculate_Arrival(flag)
  server1_waiting_time=Arriving_time_2_severs[0]
  server2_waiting_time=0
  server1_end_time = Arriving_time_2_severs[0] + Service_time
  server2_end_time = 0
  customer_waiting = 0

  for i in range(1,len(Arriving_time_2_severs)):

    if server1_end_time > server2_end_time:
      if server2_end_time > Arriving_time_2_severs[i]:

        customer_waiting = customer_waiting + (server2_end_time - Arriving_time_2_severs[i])
        server2_end_time += Service_time

      else:
        server2_waiting_time =   server2_waiting_time + (Arriving_time_2_severs[i] - server2_end_time)
        server2_end_time = Arriving_time_2_severs[i]+Service_time


    else:
      if server1_end_time > Arriving_time_2_severs[i]:
        customer_waiting = customer_waiting + (server1_end_time - Arriving_time_2_severs[i])
        server1_end_time +=  Service_time
      else:
        server1_waiting_time =  server1_waiting_time + (Arriving_time_2_severs[i] - server1_end_time)
        server1_end_time = Arriving_time_2_severs[i]+Service_time

    Service_time=int(rng.exponential(3,1))+1

  print("the server one waits for ",server1_waiting_time," minutes")
  print("the server one averagely waits for ",server1_waiting_time/450," minutes")
  print("the server two waits for ",server2_waiting_time," minutes")
  print("the server two averagely waits for ",server2_waiting_time/450," minutes")
  print("The overall customer waiting time is ",customer_waiting," minutes")
  print("The average customer waiting time is ",customer_waiting/450," minutes")

Calculate_Waiting_time_two_server('R')
Calculate_Waiting_time_two_server('P')

