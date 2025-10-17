#include <iostream>
#include <semaphore.h>

#include <sys/stat.h> // For mode_t
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <cstdlib>  // for exit function
#include <unistd.h> // for sleep function
#include <sys/mman.h>
#include <sys/fcntl.h>

constexpr int MAX_LEN = 1000;

struct region {
    char buf[MAX_LEN];
};


bool read_data(region *rptr)
{

    std::string s(rptr->buf);
    std::cout << s;
    if (s == "quit") {
        return true;
    }

    return false;
}

constexpr const char* REGION = "/my_fancy_region";

int main()
{   
    // SEMAPHORE
    sem_t *sem = sem_open("/my_sem", O_CREAT | O_EXCL, 0644, 1);

    // SHARED MEMORY
    int fd = shm_open(REGION, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
    if (fd == -1) {
        perror("SHM_OPEN error: ");
        exit(1);
    }

    if (ftruncate(fd, sizeof(region)) == -1) {
        perror("FTRUNCATE error: ");
        exit(1);
    }


    region *rptr = static_cast<region *>(mmap(NULL, sizeof(struct region),
        PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0));
    if (rptr == MAP_FAILED) { 
        perror("MMAP error: ");
        exit(1);
    }

    int count = 0;
    do {
        sem_wait(sem);
        if (rptr->buf[0] != '\0' && read_data(rptr)) {
            break;
        }

        const char* s = "C++ backend has access to the data\n";
        char *b = rptr->buf;
        for (const char *c = s; *c != '\0'; ++c) {
            std::cout << *c;
            *b++ = *c;
        }

        sem_post(sem);
        count++;

    } while (count < 5000000);


    sem_unlink("/my_sem");
    shm_unlink(REGION);

    return 0;
}