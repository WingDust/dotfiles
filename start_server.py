
import time
import os
from multiprocessing import Process,Event
import sys
# import msvcrt
# from string import Template

r'''
[python如何手动实现阻塞](https://segmentfault.com/q/1010000008924200)
'''
tup = (
    #"H:/",
    #"G:/Poring/",
    #"D:/新建文件夹/",
    #"F:/"
    "/run/media/1",
    "/run/media/2",
    "/run/media/3",
    "/run/media/"
    )
p = []

def cmds():
    for i in range(len(tup)):
        global run 
        run = "http-server %s"%(tup[i])
        def r():
            os.system(run)
        # print(run)
        pcs = Process(target=r)
        global p
        p.append(pcs) 
        

def r(e,tup,port):
    e.wait()
    print("http-server %s --port %s"%(tup,port))
    os.system("http-server %s --port %s"%(tup,port))




if __name__ == '__main__':
    # p0 = Process(target=os.system("http-server %s"%(tup[0])))
    e = Event()
    print(len(tup))
    print(tup[3])
    # p0 = Process(target=r,args=(e,tup[0],5000))
    # p1 = Process(target=r,args=(e,tup[1],5001))
    # p2 = Process(target=r,args=(e,tup[2],5002))
    p3 = Process(target=r,args=(e,tup[3],5003))
    # p0.start()
    # p1.start()
    # p2.start()
    p3.start()
    e.set()
    time.sleep(60*60*24*31)
    # cmds()
    # print(p)
    # for i in p:
    #     i.daemon=True
    #     i.start()
    #     print(12)
    # while True:
        # if ord(msvcrt.getch()) in [68,100]:
            # sys.exit()
