from sys import maxsize
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.start = None
        self.end = None
        self.head = None

    def ins(self, data, h):
        newnode = Node(data)
        if data == h:
            self.head = newnode
        if not self.start:
            self.start = newnode
            self.end = newnode
            return
        self.end.next = newnode
        self.end.next.prev = self.end
        self.end = newnode


    def delnode(self,cur):
        if cur.prev:
            cur.prev.next = cur.next
        if cur.next:
            cur.next.prev = cur.prev

        if self.start == cur:
            if cur.prev:
                self.start = cur.prev
            elif cur.next:
                self.start = cur.next
            else:
                self.start = cur.prev

        if self.end == cur:
            if cur.next:
                self.end = cur.next
            elif cur.prev:
                self.end = cur.prev
            else:
                self.end = cur.next


    def show(self):
        t = self.start
        while t:
            print(t.data,end=" ")
            t=t.next
        print()


def CSCAN(dll, h, dir):
    res = 0
    if dir == 1:
        while dll.head:
            nextnode = None

            if dll.head.next:
                nextnode = dll.head.next
            elif dll.start:
                nextnode = dll.start

            if nextnode == None:
                break

            res += abs(dll.head.data - nextnode.data)
            dll.delnode(dll.head)
            dll.head = nextnode
    else:
        while dll.head:
            nextnode = None

            if dll.head.prev:
                nextnode = dll.head.prev
            elif dll.end:
                nextnode = dll.end

            if nextnode == None:
                break

            res += abs(dll.head.data - nextnode.data)
            dll.delnode(dll.head)
            dll.head = nextnode

    return res



if __name__ == '__main__':
    d = int(input("Enter size of disk: "))
    h = int(input("Enter initial head position: "))
    q = [int(_) for _ in input("Enter IO request positions: ").split()]
    q.append(h)
    q.append(d)
    q.append(0)
    q.sort()
    dir = 0
    if h-0<d-h:
        dir = 0
    else:
        dir = 1
    dll = DLL()
    headpos = None
    for i in q:
        dll.ins(i, h)
    print("Total head movement while servicing requests: ", CSCAN(dll,h,dir))