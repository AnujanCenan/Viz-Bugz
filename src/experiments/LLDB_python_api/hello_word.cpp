#include <iostream>
int f()
{
    int a = 1;
    return 6;
}
int main()
{

    int x = 3;
    int y = 4;
    int z =  x * y;

    int g = f();

    int t = f() + 3 - 6;

    std::cout << x << y << z << '\n';
    
    return 0;
}