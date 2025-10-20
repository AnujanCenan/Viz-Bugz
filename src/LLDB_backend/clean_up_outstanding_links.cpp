// Creating and using a shared memory segment

#include <iostream>
#include <sys/mman.h>   // mmap, shm_open, ftruncate
#include <sys/shm.h>
#include <fcntl.h>      // O_CREAT, O_RDWR
#include <unistd.h>     // close, ftruncate
#include <cstring>      // memcpy
#include <semaphore.h>  // For synchronization (essential!)
#include <sys/stat.h>


constexpr const char* SHARED_MEMORY_REGION_NAME = "/viz_bugz_sm";
constexpr const char* SEMAPHORE_NAME = "/viz_bugz_semaphore";


int main()
{
    shm_unlink(SHARED_MEMORY_REGION_NAME);
    sem_unlink(SEMAPHORE_NAME);

    return 0;
}

