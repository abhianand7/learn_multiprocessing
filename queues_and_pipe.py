from multiprocessing import Process, Queue, Pipe


# there are two ways to communicate between processes, queues and pipes
# queues are thread and process safe
#
def f(q):
    q.put([42, None, 'hello'])


def g(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    q = Queue()
    # The Pipe() function returns a pair of connection objects
    # connected by a pipe which by default is duplex (two-way).
    # The two connection objects returned by Pipe() represent the two ends of the pipe.
    # Each connection object has send() and recv() methods (among others).
    # Note that data in a pipe may become corrupted
    # if two processes (or threads) try to read from or write to the same end of the pipe at the same time.
    # there is no risk of corruption from processes using different ends of the pipe at the same time.
    parent_conn, child_conn = Pipe()
    p_0 = Process(target=f, args=(q,))
    p_1 = Process(target=g, args=(child_conn,))
    p_0.start()
    p_1.start()
    print (q.get())    # prints "[42, None, 'hello']"
    print (parent_conn.recv())  # prints "[42, None, 'hello']"
    p_0.join()
    p_1.join()

