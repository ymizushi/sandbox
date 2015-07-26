package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
    i := 0
    var fib_func func(int) int
    fib_func = func(n int) int {
        if n < 2 {
            return 1
        }
        return fib_func(n-2)+fib_func(n-1)
    }
    return func() int {
        i += 1
        return fib_func(i)
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}
