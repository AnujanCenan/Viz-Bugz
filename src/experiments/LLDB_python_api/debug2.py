#!/usr/bin/env python3

import lldb
import os

def disassemble_instructions(insts):
    for i in insts:
        print(i)


# Set the path to the executable to debug
exe = "./a.out"

# Create a new debugger instance
debugger = lldb.SBDebugger.Create()

# When we step or continue, don't return from the function until the process
# stops. Otherwise we would have to handle the process events ourselves which, while doable is
# a little tricky.  We do this by setting the async mode to false.
debugger.SetAsync(False)

# Create a target from a file and arch
print("Creating a target for '%s'" % exe)

target = debugger.CreateTargetWithFileAndArch(exe, lldb.LLDB_ARCH_DEFAULT)


if target:
    # If the target is valid set a breakpoint at main
    main_bp = target.BreakpointCreateByName(
        "main", target.GetExecutable().GetFilename()
    )

    print(main_bp)

    # Launch the process. Since we specified synchronous mode, we won't return
    # from this function until we hit the breakpoint at main
    process = target.LaunchSimple(None, None, os.getcwd())

    # Make sure the launch went ok
    if process:
        # Print some simple process info
        state = process.GetState()
        print(process)
        if state == lldb.eStateStopped:
            # Get the first thread
            thread = process.GetThreadAtIndex(0)
            if thread:
                # Print some simple thread info
                print(thread)
                # Get the first frame

                frame = thread.GetFrameAtIndex(0)
                if frame:
                    # Print some simple frame info
                    var_list = frame.GetVariables(True, True, True, True)
                    for v in var_list:
                        print(v)
                thread.StepOver()

                frame = thread.GetFrameAtIndex(0)
                if frame:
                    # Print some simple frame info
                    var_list = frame.GetVariables(True, True, True, True)
                    for v in var_list:
                        print(v)
                thread.StepOver()

                frame = thread.GetFrameAtIndex(0)
                if frame:
                    # Print some simple frame info
                    var_list = frame.GetVariables(True, True, True, True)
                    for v in var_list:
                        print(v)
                thread.StepOver()

                frame = thread.GetFrameAtIndex(0)
                if frame:
                    # Print some simple frame info
                    var_list = frame.GetVariables(True, True, True, True)
                    for v in var_list:
                        print(v.GetDeclaration().GetLine())
                        print(v.GetName())
                        print(v.GetValue())
                        print(v.GetTypeName())
                        print(v.GetLoadAddress())
                        print(f"0x{v.GetLoadAddress():x} - HEX")
                        print(v.GetSummary()) # better for complex types
                        print(v)
                thread.StepOver()