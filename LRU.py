def LRU(p, f):
    frame = []
    pf = 0
    ph = 0
    d = {}
    print("Input\tFrame")
    for i in range(len(p)):
        if p[i] not in frame:
            if len(frame) != f:
                frame.append(p[i])
                d[len(frame)-1] = i
                pf += 1
            else:
                c = min(d, key=d.get)
                frame[c] = p[i]
                d[c] = i
                pf += 1
        else:
            ph += 1
            c = frame.index(p[i])
            frame[c] = p[i]
            d[c] = i
        print(p[i],"\t",frame)

    print("\nPage Faults = ", pf)
    print("Page Hits = ", ph)
    print("Total References = ", len(p))
    print("Fault Rate = ", pf/len(p))
    print("Hit Rate = ", ph/len(p))


if __name__ == "__main__":
    p = [i for i in input('Enter process sizes: ').split()]
    f = int(input('Enter size of frame: '))
    LRU(p,f)
