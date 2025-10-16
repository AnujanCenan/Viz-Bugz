from multiprocessing import shared_memory

def main():
    key = "myregion"
    
    shm = shared_memory.SharedMemory(key, create=False)

    initial_data = shm.buf[:27].tobytes().decode()
    print(f"Initial data from C++: {initial_data}")

    new_message = "*"
    encoded_message = new_message.encode('utf-8')
    shm.buf[:len(encoded_message)] = encoded_message

    initial_data = shm.buf[:27].tobytes().decode()
    print(f"Initial data from C++: {initial_data}")
    shm.unlink()

if __name__ == "__main__":
    main()