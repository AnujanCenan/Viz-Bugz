#include <iostream>

int a()
{
    return 5;
}

int b()
{
    return 6;
}

int c()
{
    return a() + b();
}

int d(int i)
{
    return c() + i;
}

int main()
{
    std::cout << d(9) << '\n';

    return 0;
}

