# Viz-Bugz

This is a drunken attempt at creating a tool that visualises your program's (virtual) memory usage. In my mind, it is meant to be a debugging tool but we'll see how far I get.

## Stuff I need to remember

1.Compilation command (via terminal) is 

**clang++ -std=c++11 -L/opt/homebrew/Cellar/llvm/21.1.3/lib -llldb -I/opt/homebrew/Cellar/llvm/21.1.3/include debug.cpp -o debug.out**

(Installed the llvm libraries via homebrew)

- Want to learn how to use CMake to make my life easier


2. The LLDB library's strucutre works around the **process** which consists of 1 or many **threads** which have 1 or many **frames** (function calls).

- Currently I am using lldb synchronously which is simpler
- Don't have to deal with event handling
- After a line of code runs in the (original) program process, the state changes are dealt with for me
- If we **set async to true**, then I am responsible for figuring out how to ensure that the **state of the process is accurately recorded**

3. Get Load Address vs Get Address
- Part of my "getting the address of variables"
- I think Get Address gets virtual address


4. Compilation Command for using boost was 
**clang++ -I/opt/homebrew/opt/boost/include -std=c++11 use_boost.cpp -o use_boost.out -L/opt/homebrew/opt/boost/lib -lboost_process -lboost_filesystem**