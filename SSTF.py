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


def SSTF(dll,h,q):
    res = 0
    while dll.head:
        l = maxsize
        r = maxsize
        nextnode = None

        if dll.head.next:
            r = abs(dll.head.next.data - dll.head.data)
            nextnode = dll.head.next

        if dll.head.prev:
            l = abs(dll.head.prev.data - dll.head.data)
            if l<r:
                nextnode = dll.head.prev

        if nextnode == None:
            break

        res+=abs(nextnode.data-dll.head.data)
        dll.delnode(dll.head)
        dll.head=nextnode

    return res


if __name__ == '__main__':
    d = int(input("Enter size of disk: "))
    h = int(input("Enter initial head position: "))
    q = [int(_) for _ in input("Enter IO request positions: ").split()]
    q.append(h)
    q.sort()
    dll = DLL()
    headpos=None
    for i in q:
        dll.ins(i, h)
    print("Total head movement while servicing requests: ", SSTF(dll,h,q))