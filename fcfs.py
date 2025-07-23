n = int(input("Enter number of processes: "))
bt = list(map(int, input("Enter burst times separated by space: ").split()))
ct = []
ct.append(bt[0])
for i in range(1, n):
    ct.append(ct[i-1]+bt[i])
print("Completion time of processes respectively:",ct)
tat= []
for i in range(0,n):
    tat.append(ct[i]-i)
print("Turn around time of processes respectively:",tat)
wt=[]
for i in range(0,n):
    wt.append(tat[i]-bt[i])
print("Waiting time of processes respectively:",wt)
cpu_allocation=[]
cpu_allocation.append(0)
for i in range(0,n-1):
    cpu_allocation.append(ct[i])
rt=[]
for i in range(0,n):
    rt.append(cpu_allocation[i]-i)
print("Response time of processes respectively:",rt)