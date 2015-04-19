#include <stdio.h>

int fib(int n)
{
    if (n == 0 || n == 1 || n== 2) {
        return 1;
    } else {
        return fib(n-2) + fib(n-1);
    }
}

int main(int argc, char const* argv[])
{
    printf("%d", fib(7));
    return 1;
}

