flag = 0
sum_wait = 0
sum_turnaround = 0
at = []
bt = []
rt = []

n = input ("enter the number of processes: ")
remain = n
for i in range(0 , n):
        a = input("enter the arrival time: ")
	at.append(a)
	b = input("enter the burst time: ")
	bt.append(b)
	rt.append(bt[i])
ts = input ("enter the time slice : ")
print "\n\nProcess\t|Turnaround Time|waiting Time\n\n"
time = 0
i = 0
for time, i in range(0 , n ) :
	if rt[i] <= ts and rt[i] > 0:
		time = rt[i] + time
		rt.append(0)
		flag = 1
	elif rt[i] > 0:
		rt.append(rt[i] - ts)
		time = time + ts
	if rt[i] == 0 and flag == 1:
		remain = remain - 1
		print i+1 , time-at[i] , time - at[i] - bt[i]
		sum_wait = sum_wait +( time - at[i] - bt[i])
		sum_turnaround = sum_turnaround + (time - at[i] )
		flag = 0
	if i == n-1:
		i = 0
	elif at[i+1] <= time:
		i = i+1
	else:
		i = 0
print "avg sum_wait = " , (sum_wait*1.0)/n
print "avg sum_turnaround = " , (sum_turnaround * 1.0)/n 
