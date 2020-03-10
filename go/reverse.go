package main

import "fmt"

func reverse(r string) string {
    var bl = []byte{}
    for i :=  range r {
        bl = append(bl, r[len(r)-1-i])
    }
    return string(bl)
}

func main() {
    fmt.Printf(reverse("hoge"))
}
