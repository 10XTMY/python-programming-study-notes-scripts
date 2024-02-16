# Process: An instance of a program (eg. A Python Interpreter)

# + Takes advantage of multiple CPUs and Cores
# + Separate memory space -> Memory is not shared between processes
# + Great for CPU-bound processing
# + New processes are started independently of other processes
# + Processes are interruptable/killable
# + One GIL per process -> avoids GIL limitation

# - Heavyweight
# - Starting a process is slower than starting a thread
# - More memory than a thread
# - IPC (inter-process communication) is more complicated


# Thread: An entity within a process that can be scheduled (also known as a leightweight process)
# A process can spawn multiple threads

# + All threads within a process share the same memory
# + Lightweight
# + Starting a thread is faster than starting a process
# + Great for I/O-bound tasks (read/write, network comms etc, while waiting can do something else)

# - Threading is limited by GIL: Only one thread at a time
# - No effect for CPU-bound tasks
# - Not interruptable/killable
# - Careful with race conditions due to shared memory
# - Race Condition: two or more threads attempting to modify same variable at same time

# GIL: Global Interpreter lock
# A lock that allows only one thread at a time to execute in Python

# Needed in CPython (standard python install) because its memory management is not thread safe
# CPython uses reference counting for memory management, objects created in python have a reference count variable
# that keeps track of the number of references that point to the object
# when this count reaches zero the memory occupied by the object can be released

# the problem, therefor, in threading is that this reference count variable needs protection from race conditions,
# where two threads may increase or decrease the value simultaneously. Hence, the GIL.

# How to avoid:
# - Use multiprocessing
# - Use a different, free threaded Python (Jython, IronPython)
# - use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy



