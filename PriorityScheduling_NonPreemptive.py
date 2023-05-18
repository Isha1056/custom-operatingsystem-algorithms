import heapq

def ps(q):
    ct=[]
    tat=[]
    wt=[]
    tq=[]
    heapq.heapify(tq)
    t=heapq.nsmallest(1,q)[0][0]
    while 1:
        while len(q)!=0 and heapq.nsmallest(1,q)[0][0]<=t:
            x = heapq.heappop(q)[1]
            heapq.heappush(tq, (-x[3], x))
        if len(tq)!=0:
            x = heapq.heappop(tq)[1]
            temp = []
            heapq.heapify(temp)
            heapq.heappush(temp, (x[1], x))
            while len(tq) and heapq.nsmallest(1,tq)[0][0] == -x[3]:
                x = heapq.heappop(tq)[1]
                heapq.heappush(temp, (x[1], x))
            x = heapq.heappop(temp)[1]
            while len(temp):
                y = heapq.heappop(temp)[1]
                heapq.heappush(tq, (-y[3], y))
            ct.append(max(t+x[2], x[1]+x[2]))
            tat.append(ct[-1]-x[1])
            wt.append(tat[-1]-x[2])
            t=ct[-1]

        if len(q) ==0 and len(tq) ==0:
            break
    return ct, tat, wt


if __name__ == '__main__':
    n = int(input('Number of processes: '))
    q = []
    print('Input process arrival time, burst time and priority: ')
    for i in range(n):
        x, y, z = input().split()
        q.append((int(x),[i, int(x), int(y), int(z)]))
    heapq.heapify(q)
    if len(q):
       ct,tat,wt=ps(q)
       print("CT TAT WT ")
       for i in range(len(ct)):
           print(ct[i], tat[i], wt[i])
       print("Total TAT = ", sum(tat))
       print("Average TAT = ", sum(tat)/n)
       print("Total WT = ", sum(wt))
       print("Average WT = ", sum(wt)/n)
