package main

import "code.google.com/p/go-tour/pic"

func Pic(dx, dy int) [][]uint8 {
    image := make([][]uint8, dy)
    for y := range(image) {
        row := make([]uint8, dx)
        for x := range(row) {
            row[x] = uint8(x+y)
        }
        image[y] = row
    }
    return image
}

func main() {
    pic.Show(Pic)
}
