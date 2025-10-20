// Creating and using a shared memory segment

#include <iostream>
#include <sys/mman.h>   // mmap, shm_open, ftruncate
#include <sys/shm.h>
#include <fcntl.h>      // O_CREAT, O_RDWR
#include <unistd.h>     // close, ftruncate
#include <cstring>      // memcpy
#include <semaphore.h>  // For synchronization (essential!)
#include <sys/stat.h>

constexpr int buff_size = 4000;

constexpr int8_t READ_REQ = 1;
constexpr int8_t WRITE_RES = 2;
constexpr int8_t READ_RES = 4;
constexpr int8_t WRITE_REQ = 8;

constexpr const char* SHARED_MEMORY_REGION_NAME = "/viz_bugz_sm";
constexpr const char* SEMAPHORE_NAME = "/viz_bugz_semaphore";

struct Memory_Layout {
    char _buf[buff_size];        // 0 - 3999 bytes of memory
    int _message_length;         // 4000 - 4003 bytes
    char _mode;                  // 4004
};

class Handle_Shared_Memory
{
public:
    void write_buffer(std::string message, int message_length) {
        if (_m._mode != WRITE_RES) {
            std::logic_error("Mode is not WRITE_RES");
        }

        for (int i = 0; i < message_length; ++i) {
            _m._buf[i] = message[i];
        }

        _m._message_length = message_length;
        _m._mode = READ_RES;
    }

    std::string read_buffer() {
        if (_m._mode != READ_REQ) {
            std::logic_error("Mode is not READ_REQ");
        }

        std::string message = _m._buf;
        _m._mode = WRITE_RES;

        return message;
    }
    

private:
    Memory_Layout _m;
};


int main()
{
    // umask(0000);
    // SEMAPHORE
    sem_t *sem_ptr = sem_open(SEMAPHORE_NAME , O_CREAT | O_EXCL , 0777, 1);

    // SHARED MEMORY
    int fd = shm_open(SHARED_MEMORY_REGION_NAME, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
    if (fd == -1) {
        perror("SHM_OPEN error: ");
        return 1;
    }

    if (ftruncate(fd, sizeof(Memory_Layout)) == -1) {
        perror("FTRUNCATE error: ");
        return 1;
    }

    Memory_Layout *region_ptr = static_cast<Memory_Layout *>(mmap(
        NULL, sizeof(Memory_Layout), PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0
    ));

    region_ptr->_buf[0] = '\0';
    region_ptr->_message_length = 0;
    
    std::string message = "";
    int count = 0;
    while (count < 8000000 && message != "quit") {
        sem_wait(sem_ptr);
        if (region_ptr->_buf[0] == '0') {
            count++;
            sem_post(sem_ptr);
            continue;
        }

        char cmd = region_ptr->_buf[1];
        switch (cmd) {
        case 'D':
            const char *dir_path = &(region_ptr->_buf[2]);
            std::cout << "Project Directory: " <<  std::string(dir_path) << '\n';
        }

        sem_post(sem_ptr);

        std::cout << count << '\n';
        count++;
    }

    shm_unlink(SHARED_MEMORY_REGION_NAME);
    sem_unlink(SEMAPHORE_NAME);

    return 0;
}

