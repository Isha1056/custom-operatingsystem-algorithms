from collections import deque

def FCFS(d,h,q):
    res = 0
    cur = h
    while len(q):
        a = q.popleft()
        res+=abs(a-cur)
        cur = a
    return res


if __name__ == '__main__':
    d = int(input("Enter size of disk: "))
    h = int(input("Enter initial head position: "))
    q = deque()
    for _ in input("Enter IO request positions: ").split():
        q.append(int(_))

    print("Total head movement while servicing requests: ", FCFS(d,h,q))