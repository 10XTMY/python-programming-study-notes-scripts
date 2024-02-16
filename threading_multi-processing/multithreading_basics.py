from threading import Thread, Lock, current_thread
from queue import Queue
import time


database_value = 0


# race condition without using lock
def increase(lock):
    global database_value
    # lock.acquire()
    # to ensure you never forget to release the lock, use a context manager:
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy
    # lock.release()


def worker(q, lock):
    while True:
        value = q.get()  # this will block and wait until elements are available
        # process value
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':

    lock = Lock()
    threads = []
    num_threads = 10
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    for t in threads:
        t.start()
    print('started all')
    for t in threads:
        t.join()
    print('joined all')

    print('end threads')

    print(f'start value: {database_value}')

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    thread1.start()
    thread2.start()
    print('ping')
    thread1.join()
    print('pong')
    thread2.join()
    print(f'end value: {database_value}')

    # queue is FIFO (first in first out)
    q = Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)
    # first = q.get()  # returns first in and removes from the queue
    # print(first)
    # print(q.empty())
    # # when done processing, always use
    # q.task_done()
    # q.join()  # blocks main process until entire queue is processed

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon = True  # this is a background thread that will die when main process dies
        # our worker function contains an infinite while True loop, if not a daemon it will never die
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

