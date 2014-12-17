#include <stdio.h>

int plus(int, int);
int exec_callback(int (*)(int,int));

int
main(void)
{
    int (*funcpointer)(int,int) = plus;
// exec_callback(&funcpointer);
    printf("hoge%d\n", funcpointer(5,3));
}


int
plus(int x,int y)
{
    return x + y;
}


int
exec_callback(int (*funcpointer)(int,int))
{
    return funcpointer(5,3);
}
