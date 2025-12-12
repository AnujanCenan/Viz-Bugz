# Gracefully Releasing Resources on Frontend Shutdown


## Introduction

An important aspect of the application is to gracefully clean up all (memory) resources used by the app during shutdown. Two major resources are 
1. the shared memory segment used for communication between the C++ 
backend and Python Tkinter frontend. 
2. the semaphore used for synchronisation to prevent data races

Know that the C++ backend program is responsible for creating these resources and the Python frontend purely uses them. The C++ program is also chosen to be in charge of releasing these resources during shutdown. However, from the user's perspective, they can only trigger a shutdown via the frontend (e.g. closing the Tkinter window). So depending on the method of shutdown, there requires a specific method of detecting the shutdown in the Tkinter application, before being able to communicate to the C++ program to release the memory resources.


## Aside: Communicating Shutdown to the C++ Backend

The following Python quit() function was written to communicate to the C++ backend to commence clean up and shutdown.

```
def close_app():
    '''
    Detects the frontend being quit, and sends the corresponding message to the
    C++ backend
    '''
    print("Quitting...")
    message = quit_message()
    send_message(message)
```

Note: look through /src/tkinter_frontend/main.py and the quit_message() function in /src/tkinter_frontend/generate_message.py for fuller understanding of the inner workings of the close_app() function.

## Shutdown Method 1: Closing the Window
Suppose the user presses the (red) X button to close the Tkinter window. From there, simply the Tkinter's window.mainloop() will terminate. Therefore, in the line beneath the main loop, we can simply call the close_app() function.

```
window.mainloop()

close_app()
```

## Shutdown Method 2: Ctrl + C
