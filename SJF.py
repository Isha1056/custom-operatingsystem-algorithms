from collections import deque

def sjf(q):
    initial = q.popleft()
    ct = []
    tat = []
    wt = []
    ct.append(initial[0] + initial[1])
    tat.append(ct[-1] - initial[0])
    wt.append(tat[-1] - initial[1])
    tq = []

    while 1:
        while len(q)!=0 and q[0][0] <= ct[-1]:
            tq.append(q.popleft())
        if len(tq)!=0:
            initial = min(tq, key=lambda x:x[1])
            tq.remove(initial)
        else:
            initial = q.popleft()
        ct.append(max(ct[-1]+initial[1], initial[0]+initial[1]))
        tat.append(ct[-1] - initial[0])
        wt.append(tat[-1] - initial[1])
        if len(tq) == 0 and len(q) ==0:
            break

    return ct,tat,wt


if __name__ == '__main__':
    n = int(input('Number of processes: '))
    q1 = []
    q = deque()
    print('Input process arrival time and burst time: ')
    for i in range(n):
        x, y = input().split()
        q1.append([i, int(x), int(y)])
    q1.sort(key=lambda x: (x[1],x[2]))
    for i in q1:
        q.append([i[1], i[2]])
    if len(q)!=0:
        ct,tat,wt = sjf(q)
        print("CT",end="\t")
        print("TAT", end= "\t")
        print("WT", end="\t")
        print()
        for i in range(len(ct)):
            print(ct[i],end="\t")
            print(tat[i],end="\t")
            print(wt[i],end="\t")
            print()
        print()
        print("Total Turn-Around Time: ", sum(tat))
        print("Average Turn-Around Time: ", sum(tat)/n)
        print()
        print("Total Waiting Time: ", sum(wt))
        print("Average Waiting Time: ", sum(wt) / n)