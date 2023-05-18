from collections import deque

def bankers(n,r,m_need,c_alloc,r_need,available):
    p=deque()
    for i in range(n):
        p.append(i)
    p_order=[]
    while True:
        check = len(p)
        for i in range(check):
            curr_process = p.popleft()
            flag=0
            for _ in range(len(available)):
                if available[_] - r_need[curr_process][_] <0:
                    flag=1
                    break
            if flag==1:
                p.append(curr_process)
            else:
                p_order.append(curr_process)
                available=[available[_]+c_alloc[curr_process][_] for _ in range(len(available))]
        if check==len(p) or len(p) == 0:
            break
    if len(p) == 0:
        print("Process Order: "+str(p_order))
    else:
        print("Deadlock, caused by processes: "+str(list(p)))


if __name__ == '__main__':
    n=int(input('Enter number of processes: '))
    r=int(input('Enter number of resources: '))
    print("Enter max need and current allocation for all process: ")
    m_need={}
    c_alloc={}
    r_need={}
    for i in range(n):
        m_need[i] = [int(_) for _ in input("Max need for process "+str(i)+":").split()]
        c_alloc[i] = [int(_) for _ in input("Current allocation for process "+str(i)+":").split()]
        r_need[i] = [m_need[i][_]-c_alloc[i][_] for _ in range(r)]
    available = [int(_) for _ in input('Enter currently available resources: ').split()]
    bankers(n,r,m_need,c_alloc,r_need,available)
