# allow you to allocate and release resources with minimal effort

# file modes:

# r read mode, pointer at beginning of the file
# r+ reading and writing, pointer at the beginning
# w writing only, overwrites if file exists, creates a new file if not
# w+ writing and reading, overwrites if file exists, creates new file if not
# rb reading in binary format, pointer at beginning
# rb+ reading and writing in binary format
# wb+ writing and reading in binary format, overwrites if file exists, creates new file if not
# a append mode, pointer at the end of the file if exists, creates new file if not
# a+ append and read, pointer at the end of the file if exists, creates new file if not
# ab append binary mode, pointer at the end of the file if exists, creates new file if not
# ab+ append and read in binary, pointer at the end of the file if exists, creates new file if not
# x exclusive file creation mode, fails if file exists
from threading import Lock
from contextlib import contextmanager

# with open('note.txt', 'w') as file:  # 'w' for write mode
#     file.write('something')  # once this operation is complete, the resource os closed/released
#
# lock = Lock()

# 'with lock' is the same as lock.acquire() and lock.release()
# with lock:  # this saves you from ever forgetting to use lock.release() after acquiring a lock in a thread
#     print('safe operation')


@contextmanager  # now we can use this function using 'with'
def generator_func(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with generator_func('notes.txt') as f:
    f.write('todon\'t')


class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):  # executed as soon as we enter the 'with' statement
        print('enter')
        self.file = open(self.filename, 'w')  # allocate resource
        return self.file  # return the file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:  # handle the exception
            print('exception has been handled')
        # print('exc:', exc_type, exc_val)  # trigger the exception
        print('exit')
        return True  # stops an exception being triggered as we handled it above


with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write('todo')
    file.nonexistingmethod()
