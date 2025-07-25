n = int(input("Enter number of processes: "))
at = list(map(int, input("Enter arrival times: ").split()))
bt = list(map(int, input("Enter burst times: ").split()))
processes = []
for i in range(n):
    processes.append([i, at[i], bt[i]]) 
processes.sort(key=lambda x: x[1])
time = 0
ct = [0] * n
completed = 0
visited = [False] * n

while completed < n:
    # Select processes that have arrived and not completed
    available = [p for p in processes if p[1] <= time and not visited[p[0]]]
    if available:
        shortest = min(available, key=lambda x: x[2])
        idx = shortest[0]
        time += shortest[2]
        ct[idx] = time
        visited[idx] = True
        completed += 1
    else:
        time += 1
tat =[0] * n
wt = [0] * n
rt = [0] * n

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
    rt[i] = wt[i]

print("\n--- SJF ")
print("{:<10} {:<15} {:<15} {:<20} {:<20} {:<20} {:<20}".format(
    "Process", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time", "Response Time"
))
print("-" * 120)

for i in range(n):
    print("{:<10} {:<15} {:<15} {:<20} {:<20} {:<20} {:<20}".format(
        f"P{i+1}", at[i], bt[i], ct[i], tat[i], wt[i], rt[i]
    ))