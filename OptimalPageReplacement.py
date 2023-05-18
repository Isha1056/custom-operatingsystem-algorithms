from collections import deque
from sys import maxsize

def OPR(p, f):
    d = {}
    for i in range(len(p)):
        if p[i] in d:
            d[p[i]].append(i)
        else:
            d[p[i]]=deque()
            d[p[i]].append(i)

    frame = []
    frame_dict = {}
    pf = 0
    ph = 0

    print("Input\tFrame")
    for i in range(len(p)):
        d[p[i]].popleft()
        if not len(d[p[i]]):
            d[p[i]].append(maxsize)
        if p[i] not in frame:
            if len(frame) != f:
                frame.append(p[i])
                frame_dict[len(frame)-1] = d[p[i]].copy()
                pf += 1
            else:
                c = max(frame_dict, key=frame_dict.get)
                frame[c] = p[i]
                frame_dict[c] = d[p[i]].copy()
                pf += 1
        else:
            ph += 1
            c = frame.index(p[i])
            frame_dict[c].popleft()
            if not len(frame_dict[c]):
                frame_dict[c].append(maxsize)
        print(p[i],"\t",frame)

    print("\nPage Faults = ", pf)
    print("Page Hits = ", ph)
    print("Total References = ", len(p))
    print("Fault Rate = ", pf/len(p))
    print("Hit Rate = ", ph/len(p))


if __name__ == "__main__":
    p = [i for i in input('Enter process sizes: ').split()]
    f = int(input('Enter size of frame: '))
    OPR(p,f)
