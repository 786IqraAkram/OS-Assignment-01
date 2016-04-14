a=[]
b=[]
x=[]
count=0
avg=0
tt=0
n = input( "enter the number of Processes:\n")
print"enter arrival time\n"
for i in range(0 , n):
	a.append(input())
print "enter burst time\n"
for i in range(0 , n):
 	b.append(input()) 
for i in range(0, n ):
	x.append(b[i])
b.append(9999)
  
for time in range(0 , count<>n):
	smallest=9
	for i in range(0 , n):
		if a[i]<=time and  b[i]<b[smallest] and  b[i]>0: 
			smallest=i  
       #	b[smallest].append( b[smallest] - 1 )
	#if b[smallest]==0:
	#	count = count +1
	#	end=time+1
	#	avg=avg+end-a[smallest]-x[smallest]
	#	tt= tt+end-a[smallest]
  
 
print "\n\nAverage waiting time = \n",avg/n
print "Average Turnaround time = ",tt/n
    

