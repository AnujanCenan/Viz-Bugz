// Part of the documentation linked in SharingMemory,md
#include <iostream>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <stdio.h>
#include <cstdlib>  // for exit function
#include <unistd.h> // for sleep function

#define SHMSZ     27

int main()
{
    key_t key = 5678; // initialising the key value for the memory segment

    int shmid;
    if ((shmid = shmget(key, SHMSZ, IPC_CREAT | 0666)) < 0) {
        perror("SHMGET error");
        exit(1);
    }

    char *shm;
    if ((shm = static_cast<char *>(shmat(shmid, nullptr, 0))) == (char *)(-1)) {
        perror("SHMAT error");
        exit(1);
    }

    char *s = shm;
    for (char c = 'a'; c <= 'z'; c++) {
        *s++ = c;
    }
    *s = '\0';

    while (*shm != '*')
        sleep(1);
    std::cout << "Client has read the message\n";

    return 0;
}