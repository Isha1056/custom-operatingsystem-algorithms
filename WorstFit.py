from collections import deque


def WorstFit(p,b):
    p = deque(p)
    for i in range(len(p)):
        x = p.popleft()
        worst=-1
        for i in range(len(b)):
            if b[i][1] == 0 and x[1] <= b[i][0]:
                if worst == -1 or b[worst][0]<b[i][0]:
                    worst=i
        if worst == -1:
            p.append(x)
        else:
            b[worst][2] = x[0]
            b[worst][1] = x[1]
    p = list(p)
    print("Allocated processes:\nBlock\tSize\tAllocated Process\tProcess Size")
    for i in range(len(b)):
        print(str(i)+"\t"+str(b[i][0])+"\t"+str(b[i][2])+"\t"+str(b[i][1]))
    print("\nUnallocated processes:\nProcess\tSize")
    for i in p:
        print(str(i[0])+"\t"+str(i[1]) )


if __name__ == '__main__':
    p = [[i,int(_)] for i,_ in enumerate(input('Enter process sizes: ').split(),0)]
    b = [[int(_),0,"None"] for _ in input('Enter block sizes: ').split()]
    WorstFit(p,b)