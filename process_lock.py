from multiprocessing import Process, Lock


# with lock
# def f(l, i):
#     l.acquire()
#     print 'hello world', i
#     l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()


# without lock
def f(i):
    print ('hello world', i)

if __name__ == '__main__':
    for num in range(10):
        p = Process(target=f, args=(num, )) # args requires to have iterable objects
        p.start()
        p.join()    # if join() method is used, everything works just like using lock
