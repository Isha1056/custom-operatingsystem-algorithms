def check(available, process_need):
    for _ in range(len(available)):
        if available[_]<process_need[_]:
            return False
    return True

def bankers(n,m_need,c_alloc,r_need,available,seq,sol):
    if len(seq) == n:
        sol.append(seq)
        return
    for i in range(n):
        if i not in seq and check(available, r_need[i]):
            bankers(n, m_need,c_alloc,r_need, [available[_]+c_alloc[i][_] for _ in range(len(available))], seq+[i], sol)


if __name__ == '__main__':
    n=int(input('Enter number of processes: '))
    print("Enter max need and current allocation for all process: ")
    m_need={}
    c_alloc={}
    r_need={}
    for i in range(n):
        m_need[i] = [int(_) for _ in input("Max need for process "+str(i)+":").split()]
        c_alloc[i] = [int(_) for _ in input("Current allocation for process "+str(i)+":").split()]
        r_need[i] = [m_need[i][_]-c_alloc[i][_] for _ in range(len(m_need[i]))]
    available = [int(_) for _ in input('Enter currently available resources: ').split()]
    sol=[]
    bankers(n,m_need,c_alloc,r_need,available,[],sol)
    print("All Safe Sequences: ")
    for i in sol:
        print(i)