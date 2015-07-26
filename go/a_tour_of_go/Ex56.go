package main

import (
    "fmt"
    "strconv"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
    return "cannot Sqrt negative number:" + strconv.FormatFloat(float64(e), 'G', 'G', 64)
}

func Newton(z float64, x float64) float64 {
    result := z-((z*z-x)/(2*z))
    return result
}


func Sqrt(f float64) (float64, error) {
    if f < 0 {
        return f, ErrNegativeSqrt(f)
    }
    z := Newton(1.0, f)
    for i:=0;i<10;i++  {
        z = Newton(z, f)
    }
    return z, nil
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(Sqrt(-2))
}
