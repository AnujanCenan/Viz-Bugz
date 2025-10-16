# How to Share Memory Between a C++ and Python Program


## How to Share Memory Between Two C++ Programs
Documentation: https://users.cs.cf.ac.uk/Dave.Marshall/C/node27.html

### shmget()
A.k.a shared-memory-get
Obtains access to a shared memory segment

Prototype: **int shmget(key_t key, size_t size, int shmflg);**

- key: an access value associated with the *semaphore* ID
- size: the number of bytes the memory segment should have
- shmflg: flags set to indicate access rights and creation control flags

Typical control flags is IPC_CREAT | 0666
Meaning of this flag is explained in below image

![Read and write permissions for all groups](./images/control_flags_explained.png "IPC_CREAT | 0666 explained")

[Source](https://stackoverflow.com/questions/40380327/what-is-the-use-of-ipc-creat-0666-flag-in-shmget-function-in-c)


### shmctl
A.k.a shared-memory-control
Alters the permissions (and other characteristics) of a shared memory segment

Prototype: **int shmctl(int shmid, int cmd, struct shmid_ds *buf);**

- shmid: id of memory segment; what yuo get from shmget()
- cmd: one of the following
    - SHM_LOCK: lock the specific shared memory segment in memory.
    - SHM_UNLOCK: unlock the specific shared memory segment in memory.
    - IPC_STAT: return the status info contained in the control structure and place it in the buffer *buf*
    - IPC_SET: set the effective user and group identification and access permissions.

### shmat() and shmdt()
A.k.a shared memory attach and shared memory detach

Prototype: **void *shmat(int shmid, const void *shmaddr, int shmflg);**

Returns an address, *shmaddr* to the head of the shared memory segment

Prototype: **int shmdt(const void *shmaddr);**

Detaches the shared memory segment pointed at *shmaddr*


## C++ POSIX Memory
Same documentation at previous

Use shm_open() to open a shared memory object, shm_unlink() to close it.

## How to Share Memory Between a C++ and Python Program

Documentation: https://docs.python.org/3/library/multiprocessing.shared_memory.html

Requires the module **from multiprocessing import shared_memory**

The module provides the class **Shared Memory**
Good for allocation and management of shared memory

### SharedMemory() Constructor
SharedMemory(name=None, create=False, size=0, *, track=True)
- name: str|None -> a unique name for memory segment. If None, then a name is generated. For our purposes, should be the stringified shm_key from C++
- create: bool -> Is a new shared memory block created (True) or an existing memory block is attached (False)
- size: int -> The requested number of bytes
- track: bool -> If true, a resource tracker process is provided; ensures proper clean up

### Close() method
close()
When access to the block is no longer needed
To ensure *proper* cleanup, use the unlink method

### Unlink method
unlink()

