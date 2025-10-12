#include <iostream>
#include <lldb/API/SBDebugger.h>
#include <lldb/API/SBTarget.h>
#include <lldb/API/SBProcess.h>
#include <lldb/API/SBThread.h>
#include <lldb/API/SBFrame.h>
#include <lldb/API/SBValue.h>
#include <lldb/API/SBListener.h>
#include <lldb/API/SBLineEntry.h>
#include <lldb/API/SBEvent.h>
#include <lldb/lldb-defines.h>
#include <lldb/API/SBDefines.h>
#include <lldb/API/SBDeclaration.h>
#include <unistd.h>
#include <vector>

constexpr int TIMEOUT = 5;
void printVar(lldb::SBValue v)
{

    std::cout << "------------------------\n";
    std::cout << "Name: " << v.GetName() << '\n';
    std::cout << "Type: " << v.GetType().GetName() << '\n';
    std::cout << "Value: " << v.GetValue() << '\n';
    std::cout << "Byte Size: " << v.GetByteSize() << '\n';
    std::cout << "Address: " << v.GetLoadAddress() << '\n';        // might be a problem
    std::cout << "Declaration Line: " << v.GetDeclaration().GetLine() << '\n';
    std::cout << "------------------------\n\n";

}

void RunDebugger()
{
    lldb::SBDebugger::Initialize();
    lldb::SBDebugger debugger = lldb::SBDebugger::Create();
    lldb::SBError error;
    lldb::SBTarget target = debugger.CreateTargetWithFileAndArch("/Users/unswaccount/Documents/PersonalProjects/Viz-Bugz/src/experiments/LLDB_python_api/a.out", LLDB_ARCH_DEFAULT);

    if (!target.IsValid()) {
        throw std::runtime_error("Target is invalid");
    }

    debugger.SetAsync(false);

    const char* file_path = "/Users/unswaccount/Documents/PersonalProjects/Viz-Bugz/src/experiments/LLDB_python_api/hello_word.cpp";
    lldb::SBFileSpec file_spec = lldb::SBFileSpec(file_path);
    target.BreakpointCreateByLocation(file_spec, 6, 0);
    target.BreakpointCreateByName("main");

    char buffer[4096];
    lldb::SBProcess process = target.LaunchSimple(nullptr, nullptr, getcwd(buffer, 4096));

    if (!process) {
        throw std::runtime_error("Process is invalid");
    }


    if (process.GetState() == lldb::eStateStopped) {
        lldb::SBThread thread = process.GetSelectedThread();

        while (true) {
            lldb::SBEvent event;
            
            if (process.IsValid()) {
                
                thread = process.GetSelectedThread();
                lldb::SBFrame frame = thread.GetSelectedFrame();

                if (!frame.IsValid()) {
                    break;
                }
                const lldb::SBValueList values = frame.GetVariables(true, true, true, false);
                auto line = frame.GetLineEntry();
                std::cout << "LINE NUMBER = " << line.GetLine() << '\n';
                for (int i = 0; i < values.GetSize(); ++i) {
                    const auto& v = values.GetValueAtIndex(i);
                    printVar(v);
                }




                if (process.GetState() == lldb::eStateExited) {
                    break;
                }
                if (line.GetLine() == 14) {
                    thread.StepInto();
                } else {
                    thread.StepOver();
                }
                if (thread.GetNumFrames() == 1) {
                    process.Continue();
                }

                std::cout << "Moved to line " << frame.GetLineEntry().GetLine() << '\n';
                std::cout << "Current process state = " << process.GetState() << '\n';   
            } else {
                break;
            }
        }
    }

    lldb::SBDebugger::Terminate();
}

int main()
{
    RunDebugger();
    return 0;
}