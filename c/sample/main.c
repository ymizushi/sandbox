#include <stdio.h>

int plus(int, int);
int exec_callback(int (*)(int,int));
void hello_world(void);
void hello_shift(void);

int
main(void)
{
    hello_world();
    hello_shift();
}

void hello_world() {
    char hello[] = "hello";
    char *world  = "world";
    printf("hello: %s\n", hello);
    printf("world: %s\n", hello);
}

void hello_shift() {
    int value = 0b10000000;
    printf("value: %d\n", value);
    printf("value: %d\n", value << 0);
    printf("value: %d\n", value << 1);
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
