def FIFO(p, f):
    frame = [None]*f
    c=0
    pf = 0
    ph = 0
    print("Input\tFrame")
    for i in range(len(p)):
        if p[i] not in frame:
            frame[c] = p[i]
            c= (c+1)%len(frame)
            pf+=1
        else:
            ph+=1
        print(p[i], frame)
    print("\nPage Faults = ", pf)
    print("Page Hits = ", ph)
    print("Total References = ", len(p))
    print("Fault Rate = ", pf/len(p))
    print("Hit Rate = ", ph/len(p))



if __name__=="__main__":
    p = [i for i in input('Enter process sizes: ').split()]
    f = int(input('Enter size of frame: '))
    FIFO(p,f)




