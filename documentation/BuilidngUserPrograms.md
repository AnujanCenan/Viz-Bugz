# Building User Programs in the Backend - Boost

## Context
A huge part of the debugger tool is giving the user the ability to give the application a C/C++ file to debug.

Usually, a user would use some build command - a compiler command (gcc, g++, clang, clang++ for example) or make or cmake - to build their program before running it.

What we want is for the usre to pass their build command to us (via the python frontend). From there, the frontend should pass the build command to the C++ backend. From there, the C++ backend should be able to run the build command and start the debugging process on the resulting executable.

## Introducing Boost
Boost is a C++ library which is able to essentially handle this goal for us. In essence, it should be able to take in the user's **current working directory** and their **build command** (with file paths that are relative to their current working directory). With these inputs boost should produce the executable

We specifically look at the boost.process library:
Documentation: https://www.boost.org/doc/libs/1_89_0/libs/process/doc/html/index.html