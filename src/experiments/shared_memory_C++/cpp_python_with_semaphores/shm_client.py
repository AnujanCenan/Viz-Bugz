from multiprocessing import shared_memory
import posix_ipc

def main():
    shm_key = "my_fancy_region"
    sem_key = "/my_sem"

    sem = posix_ipc.Semaphore(sem_key)

    shm = shared_memory.SharedMemory(shm_key, create=False, track=False)

    while (True):
        sem.acquire()
        initial_data = shm.buf[:40].tobytes().decode()
        print(f"Initial data from C++: {initial_data}")

        input_mes = input() + '\0'      # null terminator makes it easier for C++ to read the string
        encoded_message = input_mes.encode('utf-8')
        shm.buf[:len(encoded_message)] = encoded_message
        sem.release()

        if (input_mes == "quit" + '\0'): break

    
    # shm.unlink()          # make C++ program responsible for freeing things since 
                            # it is the owner of the shared memory and the semaphore
    # sem.unlink()

if __name__ == "__main__":
    main()


