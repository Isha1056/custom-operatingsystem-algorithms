from collections import deque


def srtf(q, d):
    initial = q.popleft()
    ct = []
    ct.append(initial[1])
    tq = deque()

    while 1:
        while len(q) != 0 and q[0][1] <= ct[-1]+initial[2]:
            if initial[2]+ct[-1] > q[0][2]+q[0][1]:
                initial[2] -= (q[0][1]-ct[-1])
                tq.append(initial)
                ct.append(q[0][1])
                d[initial[0]][2] = ct[-1]
                d[initial[0]][3] = d[initial[0]][2] - d[initial[0]][0]
                d[initial[0]][4] = d[initial[0]][3] - d[initial[0]][1]
                initial = q.popleft()
            else:
                tq.append(q.popleft())

        ct.append(max(ct[-1]+initial[2], initial[1]+initial[2]))
        initial[2] -= initial[2]
        d[initial[0]][2] = ct[-1]
        d[initial[0]][3] = d[initial[0]][2] - d[initial[0]][0]
        d[initial[0]][4] = d[initial[0]][3] - d[initial[0]][1]
        if len(tq)!=0:
            initial = min(tq, key=lambda x:x[2])
            tq.remove(initial)
        elif len(q)!=0:
            initial = q.popleft()

        if len(q) == 0 and len(tq) == 0 and initial[2]<=0:
            break

    return d


if __name__ == '__main__':
    n = int(input('Number of processes: '))
    q1 = []
    q = deque()
    print('Input process arrival time and burst time: ')
    for i in range(n):
        x, y = input().split()
        q1.append([i, int(x), int(y)])
    q1.sort(key=lambda x: (x[1],x[2]))
    d = {}

    for i in q1:
        d[i[0]] = [i[1], i[2], 0, 0, 0]
        q.append([i[0], i[1], i[2]])
    if len(q)!=0:
        d = srtf(q, d)
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
