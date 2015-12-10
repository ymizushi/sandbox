package main

import "fmt"

type Size struct {
    Width int
    Height int
}

type Point struct {
    X int
    Y int
}

type Color struct {
    R int
    G int
    B int
    A int
}

type Pixel struct {
    P Point
    C Color
}

func main() {
    array := make([]Size, 10)
    for i, v := range array {
        array[i].Width = 10
        array[i].Height = 10
        fmt.Println(i, array[i)
    }
}
