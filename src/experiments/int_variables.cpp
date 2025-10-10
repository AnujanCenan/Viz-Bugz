#include <iostream>

void analyse_int(int *p)
{

    std::cout << "------------------------\n";
    std::cout << "ADDRESS: " << p << '\n';
    try {
        if (p) {
            std::cout << "VALUE: " << *p << '\n';
        } else  {
            std::cout << "NULL\n";
        }
    } catch (std::exception e) {
        std::cout << e.what() << '\n';
    }
}

int main()
{
    int a;      // uninitialised
    analyse_int(&a);
    int b = 3; // given a value
    analyse_int(&b);

    int *c = nullptr;
    analyse_int(c);


    return 0;
}