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

func NewPoint(x int, y int) *Point {
    point := new(Point)
    point.X = x
    point.Y = y
    return point
}

type Color struct {
    R int
    G int
    B int
    A int
}

func NewColor(r int, g int, b int, a int) *Color {
    color := new(Color)
    color.R = r
    color.G = g
    color.B = b
    color.A = a
    return color
}

type Pixel struct {
    P Point
    C Color
}

func NewPixel(p Point, c Color) *Pixel {
    pixel := new(Pixel)
    pixel.P = p
    pixel.C = c
    return pixel
}

func main() {
    var image [10][10]Pixel
    for i, pixel_row := range image {
        for v, _ := range pixel_row {
            image[i][v] = NewPixel(NewPoint(i, v), NewColor())
            array[i].Height = 10
            fmt.Println(i, array[i])
        }
    }
}
