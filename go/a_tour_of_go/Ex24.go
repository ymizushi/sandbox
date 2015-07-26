package main

import (
    "fmt"
    "math"
)

func Newton(z float64, x float64) float64 {
    result := z-((z*z-x)/(2*z))
    return result
}

func Sqrt(x float64) float64 {
    z := Newton(1.0, x)
    for i:=0;i<10;i++  {
        z = Newton(z, x)
        fmt.Println(z)
    }
    return z
}


func main() {
    fmt.Println("my impl:")
    fmt.Println(Sqrt(3))
    fmt.Println("old impl:")
    fmt.Println(math.Sqrt(3))
}
