// Creating and using a shared memory segment

#include <iostream>
#include <sys/mman.h>   // mmap, shm_open, ftruncate
#include <sys/shm.h>
#include <fcntl.h>      // O_CREAT, O_RDWR
#include <unistd.h>     // close, ftruncate
#include <cstring>      // memcpy
#include <semaphore.h>  // For synchronization (essential!)

constexpr char* SHM_NAME = "/lldb_mem_viz_shm";
constexpr size_t SHM_SIZE = 4096; // 4KB for simple state data

int main()
{
    int shm_fd; // TODO: alias types for better readability
    
    
    return 0;
}

