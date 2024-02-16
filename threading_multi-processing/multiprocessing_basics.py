import time
from multiprocessing import Process, Value, Array, Lock, Queue, Pool


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


def add_to_shared_value(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add_to_shared_array(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for n in range(len(numbers)):
            with lock:
                numbers[n] += 1


def square(numbers, q):
    for i in numbers:
        q.put(i*i)


def make_negative(numbers, q):
    for i in numbers:
        q.put(-1*i)


def cube(number):
    return number * number * number


if __name__ == '__main__':  # this is required in windows to avoid creating subprocesses recursively.

    # processes = []
    # num_processes = os.cpu_count()
    # # create
    # for i in range(num_processes):
    #     p = Process(target=square_numbers)
    #     processes.append(p)
    #
    # # start
    # for p in processes:
    #     p.start()
    #
    # # join (wait for all to finish, blocking the main thread)
    # for p in processes:
    #     p.join()
    #
    # print('end main')

    # processes use memory objects to share data (Value, Array)
    shared_number = Value('i', 0)  # i for integer
    shared_array = Array('d', [0.0, 100.0, 200.0])  # d for double
    print(f'number at beginning is {shared_number.value}')
    print(f'array at beginning is {shared_array[:]}')

    lock = Lock()
    process1 = Process(target=add_to_shared_value, args=(shared_number, lock))
    process2 = Process(target=add_to_shared_value, args=(shared_number, lock))
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    process1 = Process(target=add_to_shared_array, args=(shared_array, lock))
    process2 = Process(target=add_to_shared_array, args=(shared_array, lock))
    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print(f'number at end is {shared_number.value}')
    print(f'array at end is {shared_array[:]}')

    # queues
    q = Queue()
    numbers = range(1, 6)  # range from 1 to 5
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    # process pool: used to manage multiple processes
    # controls a pool to which jobs can be submitted
    # splits the data into smaller chunks to be processed in parallel
    # has 4 important methods (more in documentation):
    # map, apply, join, close
    pool = Pool()
    numbers = range(10)
    result = pool.map(cube, numbers)  # automatically allocate the max num of available processes and manage the data
    # pool.apply(cube, numbers[0]) executes the function with one argument
    pool.close()
    pool.join()
    print(result)
