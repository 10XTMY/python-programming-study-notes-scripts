# Python Concurrency Notes

## Process

A process is an instance of a program (e.g., A Python Interpreter).

### Advantages
- Takes advantage of multiple CPUs and cores.
- Separate memory space: Memory is not shared between processes.
- Great for CPU-bound processing.
- New processes are started independently from other processes.
- Processes are interruptable/killable.
- One GIL (Global Interpreter Lock) per process avoids GIL limitation.

### Disadvantages
- Heavyweight.
- Starting a process is slower than starting a thread.
- Requires more memory than a thread.
- IPC (Inter-Process Communication) is more complicated.

## Thread

A thread is an entity within a process that can be scheduled (also known as a lightweight process). A process can spawn multiple threads.

### Advantages
- All threads within a process share the same memory.
- Lightweight.
- Starting a thread is faster than starting a process.
- Great for I/O-bound tasks (read/write, network communications etc.), while waiting, can do something else.

### Disadvantages
- Threading is limited by the GIL: Only one thread can execute at a time.
- No effect for CPU-bound tasks.
- Not interruptable/killable.
- Careful management is needed to avoid race conditions due to shared memory.
- **Race Condition**: Two or more threads attempting to modify the same variable at the same time.

## Global Interpreter Lock (GIL)

A lock that allows only one thread at a time to execute in Python.

- **Necessity**: Needed in CPython (the standard Python installation) because its memory management is not thread-safe.
- **Memory Management**: CPython uses reference counting for memory management. Objects created in Python have a reference count variable that keeps track of the number of references pointing to the object. When this count reaches zero, the memory occupied by the object can be released.
- **Problem with Threading**: The reference count variable needs protection from race conditions, where two threads may increase or decrease the value simultaneously. Hence, the GIL.

### How to Avoid GIL Limitations
- Use multiprocessing.
- Use a different, free-threaded Python interpreter (Jython, IronPython).
- Use Python as a wrapper for third-party libraries (C/C++), such as NumPy, SciPy.
