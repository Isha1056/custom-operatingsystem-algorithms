import threading
import time


class ReaderWriter:
    def __init__(self):
        self.shared_data=open("SharedData.txt", 'a+')
        self.active_lock=0
        self.reader_count=0
        self.lock = threading.Lock()
        self.reader_ready = threading.Condition(self.lock)
        self.writer_ready=threading.Condition(self.lock)

    def reader_acquire(self,reader):
        self.lock.acquire()
        self.reader_count+=1
        while self.active_lock<0:
            self.reader_ready.wait()
        self.active_lock = 1
        self.shared_data.seek(0)
        x=''
        l=self.shared_data.readlines()
        for i in l:
            x+="\t"+i
        print(str(reader)+' File output:\n'+x)
        self.lock.release()

    def writer_acquire(self, writer):
        self.lock.acquire()
        while self.active_lock!=0:
            self.writer_ready.wait()
        self.active_lock = -1
        self.shared_data.write("Text written by "+str(writer)+"\n")
        self.lock.release()

    def release(self, object):
        self.lock.acquire()
        self.active_lock=0
        self.lock.release()
        print(str(object)+" Stop")
        if self.reader_count==0:
            self.writer_ready.acquire()
            self.writer_ready.notify()
            self.writer_ready.release()
        elif self.reader_count and self.active_lock == 0:
            self.reader_ready.acquire()
            self.reader_ready.notifyAll()
            self.reader_ready.release()


sem = ReaderWriter()


class Reader(threading.Thread):
    def run(self) -> None:
        print(str(self) + " Start")
        sem.reader_acquire(self)
        sem.release(self)


class Writer(threading.Thread):
    def run(self) -> None:
        print(str(self) + " Start")
        sem.writer_acquire(self)
        print(str(self)+" Written to File")
        sem.release(self)


if __name__=='__main__':
    r = int(input('Enter number of reader threads: '))
    w = int(input('Enter number of writer threads: '))
    x=w
    if r>w:
        x=r
    for _ in range(x):
        if _<=w:
            Writer().start()
        if _<=r:
            Reader().start()
