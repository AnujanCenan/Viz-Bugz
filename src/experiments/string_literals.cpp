// Getting the address of a string literal
#include <iostream>
#include <string.h>

void analyse_string_literal(const char *p) 
{

    std::size_t size = strlen(p) + 1;
    std::cout << size << '\n';

    void *address = (void *)(p);
    std::cout << address << '\n';

    std::cout << "----------------------\n";
    std::cout << "| ADDRESS: " << address << '\n';
    std::cout << "| VALUE: " << p << "\\0" << '\n';
    std::cout << "| SIZE: " << size << '\n';
    std::cout << "----------------------\n";

}

int main()
{
    const char* p1 = "Hello";
    analyse_string_literal(p1);
    // std::cout << (void *)(p1) << '\n';           // 0x1009ebf10
    
    const char* p2 { "Hello" };                  
    analyse_string_literal(p2);
    // std::cout << (void *)(p2) << '\n';           // 0x1009ebf10

    const char* p3 { "Hello" };
    analyse_string_literal(p3);
    // std::cout << (void *)(p3) << '\n';           // 0x1009ebf10


    return 0;
}