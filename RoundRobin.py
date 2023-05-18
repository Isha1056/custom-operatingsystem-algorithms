from collections import deque


def roundrobin(q, timeq, d):
    initial = q.popleft()
    ct = []
    ct.append(min(d[initial[0]][0] + d[initial[0]][1], d[initial[0]][0] + timeq))
    d[initial[0]][2] = ct[-1]
    d[initial[0]][3] = d[initial[0]][2] - d[initial[0]][0]
    d[initial[0]][4] = d[initial[0]][3] - d[initial[0]][1]
    initial[2] = initial[2] - timeq
    tq = deque()

    while 1:
        while len(q) != 0 and q[0][1] <= ct[-1]:
            tq.append(q.popleft())
        if initial[2]>0:
            tq.append(initial)
        if len(tq) != 0:
            initial = tq.popleft()
        elif len(q)!=0:
            initial = q.popleft()
        if len(tq) == 0 and len(q) == 0 and initial[2]<=0:
            break
        ct.append(max(min(ct[-1] + initial[2], ct[-1] + timeq), min(initial[1] + initial[2], initial[1] + timeq)))
        initial[2] -= timeq
        d[initial[0]][2] = ct[-1]
        d[initial[0]][3] = d[initial[0]][2] - d[initial[0]][0]
        d[initial[0]][4] = d[initial[0]][3] - d[initial[0]][1]

    return d


if __name__ == '__main__':
    n = int(input('Number of processes: '))
    timeq = int(input('Time quantum: '))
    q1 = []
    q = deque()
    print('Input process arrival time and burst time: ')
    for i in range(n):
        x, y = input().split()
        q1.append([i, int(x), int(y)])
    q1.sort(key=lambda x: (x[1], x[2]))
    d = {}

    for i in q1:
        d[i[0]] = [i[1], i[2], 0, 0, 0]
        q.append([i[0], i[1], i[2]])
    if len(q)!=0:
        d = roundrobin(q, timeq, d)
        q1.sort(key=lambda x: x[0])
        print("CT",end="\t")
        print("TAT", end= "\t")
        print("WT", end="\t")
        print()
        tat = 0
        wt = 0
        for i in q1:
            print(d[i[0]][2],end="\t")
            print(d[i[0]][3],end="\t")
            print(d[i[0]][4],end="\t")
            tat += d[i[0]][3]
            wt += d[i[0]][4]
            print()
        print()
        print("Total Turn-Around Time: ", tat)
        print("Average Turn-Around Time: ", tat/n)
        print()
        print("Total Waiting Time: ", wt)
        print("Average Waiting Time: ", wt / n)
