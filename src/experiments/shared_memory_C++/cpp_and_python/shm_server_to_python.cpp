#include <iostream>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <cstdlib>  // for exit function
#include <unistd.h> // for sleep function

#include <unistd.h>
#include <sys/mman.h>

#include <sys/fcntl.h>



#define MAX_LEN 10000
struct region {        /* Defines "structure" of shared memory */
    char buf[MAX_LEN];
    int len;
};
struct region *rptr;
int main()
{
    int fd;
    /* Create shared memory object and set its size */

    fd = shm_open("/myregion", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
    if (fd == -1) {
        perror("SHM_OPEN error: ");
        exit(1);
    }

    if (ftruncate(fd, sizeof(struct region)) == -1) {
        perror("FTRUCNATE error: ");
        exit(1);
    }


    /* Map shared memory object */


    rptr = static_cast<region *>(mmap(NULL, sizeof(struct region),
        PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0));
    if (rptr == MAP_FAILED) { 
        perror("MMAP error: ");
        exit(1);
    }
    char *s = rptr->buf;
    for (char c = 'a'; c <= 'z'; ++c) {
        *s++ = c;
    }

    *s = '\0';

    while (rptr->buf[0] != '*') {
        sleep(1);
    }

    std::cout << "Client has read the message\n";
    return 0;

}