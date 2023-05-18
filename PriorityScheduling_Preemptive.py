import heapq

def ps(q,d):
    tq = []
    heapq.heapify(tq)
    t = heapq.nsmallest(1, q)[0][0]
    temp = []
    heapq.heapify(temp)
    while len(q)!=0 and heapq.nsmallest(1,q)[0][0]<=t:
        x = heapq.heappop(q)[1]
        heapq.heappush(temp, (-x[3], x))
    x = heapq.heappop(temp)[1]
    while len(temp):
        y = heapq.heappop(temp)[1]
        heapq.heappush(tq,(-y[3], y))
    while 1:
        while len(q) and heapq.nsmallest(1,q)[0][0] <= t+x[2]:
            y = heapq.heappop(q)[1]
            if y[3]>x[3]:
                x[2] -= (y[1]-t)
                t = y[1]
                d[x[0]][3] = t
                d[x[0]][4] = d[x[0]][3] - d[x[0]][0]
                d[x[0]][5] = d[x[0]][4] - d[x[0]][1]
                if x[2]>0:
                    heapq.heappush(tq, (-x[3], x))
                x = y
            else:
                heapq.heappush(tq, (-y[3], y))
        t = max(t+x[2], x[1]+x[2])
        x[2]-=x[2]
        d[x[0]][3] = t
        d[x[0]][4] = d[x[0]][3] - d[x[0]][0]
        d[x[0]][5] = d[x[0]][4] - d[x[0]][1]
        if len(tq):
            x=heapq.heappop(tq)[1]
        elif len(q):
            x=heapq.heappop(q)[1]

        if len(q)==0 and len(tq)==0 and x[2]<=0:
            break

    return d
if __name__ == '__main__':
    n = int(input('Number of processes: '))
    q = []
    print('Input process arrival time, burst time and priority: ')
    d = {}
    for i in range(n):
        x, y, z = input().split()
        q.append((int(x),[i, int(x), int(y), int(z)]))
        d[i] = [int(x), int(y), int(z),0,0,0]
    heapq.heapify(q)
    if len(q):
       d=ps(q,d)
       print("AT BT P CT TAT WT ")
       tat=0
       wt=0
       for i in d.keys():
           print(d[i][0], d[i][1], d[i][2], d[i][3], d[i][4], d[i][5])
           tat+=d[i][4]
           wt+=d[i][5]
       print("Total TAT = ", (tat))
       print("Average TAT = ", (tat)/n)
       print("Total WT = ", (wt))
       print("Average WT = ", (wt)/n)
