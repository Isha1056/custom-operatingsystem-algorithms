def CLOOK(dll, h, d):
    res = 0
    print(q[h], d)
    if q[h] - 0 >= d - q[h]:
        for i in range(len(q)-1):
            print(q[(h+i)%len(q)], q[(h+i+1)%len(q)])
            res += abs(q[(h+i)%len(q)] - q[(h+i+1)%len(q)])
    else:
        for i in range(len(q)-1):
            print(q[(h-i+len(q))%len(q)], q[(h-i-1+len(q))%len(q)])
            res += abs(q[(h-i+len(q))%len(q)] - q[(h-i-1+len(q))%len(q)])
    return res


if __name__ == '__main__':
    d = int(input("Enter size of disk: "))
    h = int(input("Enter initial head position: "))
    q = [int(_) for _ in input("Enter IO request positions: ").split()]
    q.append(h)
    q.sort()
    dir = 0
    print("Total head movement while servicing requests: ", CLOOK(q,q.index(h),d))