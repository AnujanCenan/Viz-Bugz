// Documentation: https://www.boost.org/doc/libs/1_89_0/libs/process/doc/html/index.html#quickstart
// Example programs: https://github.com/boostorg/process/tree/develop/example
#include <boost/process.hpp>
#include <boost/asio.hpp>

#include <iostream>
#include <string>
#include <vector>


int main()
{
    // std::string executable = "make";             // OPTION 1 - use make
    std::string executable = "clang++";             // OPTION 2 - use the raw compuler
    auto e = boost::process::environment::find_executable(executable);

    std::string build_command = "ls";    
    boost::asio::io_context ctx;
    boost::asio::readable_pipe rp{ctx};

    std::string output;

    // boost::process::process proc(ctx, e, {}, boost::process::process_start_dir("./programs_to_build"));      // OPTION 1 - use make
    
    std::vector<std::string> args = {"-g", "simple_program.cpp", "-o", "a.out"};
    boost::process::process proc(ctx, e, args, boost::process::process_start_dir("./programs_to_build"));         // OPTION 2 - use a raw compiler
    
    boost::system::error_code ec;
    boost::asio::read(rp, boost::asio::dynamic_buffer(output), ec);

    proc.wait();
    return 0;
}