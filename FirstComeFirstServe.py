from collections import deque

def ganttchart(q):
    initial = q.popleft()
    ct = []
    ct.append(initial[0] + initial[1])
    tat = []
    tat.append(ct[-1] - initial[0])
    wt = []
    wt.append(tat[-1] - initial[1])
    while len(q) != 0:
        i = q.popleft()
        ct.append(max(ct[-1]+i[1], i[0]+i[1]))
        tat.append(ct[-1] - i[0])
        wt.append(tat[-1] - i[1])
    return ct, tat, wt


if __name__ == '__main__':
    n = int(input('Number of processes: '))
    q = deque()
    q1 = []
    print('Input process arrival time and burst time: ')
    for i in range(n):
        x, y = input().split()
        q1.append([i, int(x), int(y)])
    q1.sort(key=lambda x: x[1])
    for i in q1:
        q.append([i[1],i[2]])
    if len(q)!=0:
        ct,tat,wt = ganttchart(q)
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
