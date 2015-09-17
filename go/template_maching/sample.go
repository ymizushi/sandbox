package main

import (
    "fmt"
    // "github.com/nfnt/resize"
    "image"
    _ "image/jpeg"
    "os"
)

func main() {
    file, err := os.Open("image.jpg")
    defer file.Close()
    if err != nil {
        fmt.Println(err)
        return
    }
    img, _, err := image.Decode(file)
    if err != nil {
        fmt.Println(err)
        return
    }

    // resize for performance
    // img = resize.Resize(36, 0, img, resize.Lanczos3)

    printRastor(img)
    hist := getHistgram(img)

    max := 0
    // find most appered color
    for _, val := range hist {
        if val > max {
            max = val
        }
    }
    r, g, b := int2rgb(max)
    colorCode := "#" + dec2hex(r, 2) + dec2hex(g, 2) + dec2hex(b, 2)

    // most appered color in image
    println(colorCode)
}

func printRastor(img image.Image) {
    rect := img.Bounds()
    counter := 0
    for i := 0; i < rect.Max.Y; i++ {
        for j := 0; j < rect.Max.X; j++ {
            r, g, b, _ := img.At(j, i).RGBA()
            fmt.Println("%s:%s:%s", r, g, b)
            counter += 1
        }
    }
    fmt.Println("counter: ", counter)

}

func getHistgram(img image.Image) []int {
    hist := make([]int, 1000000)

    // get bounds
    rect := img.Bounds()
    // color reduction
    for i := 0; i < rect.Max.Y; i++ {
        for j := 0; j < rect.Max.X; j++ {
            r, g, b, _ := img.At(j, i).RGBA()
            i := rgb2int(int(r), int(g), int(b))
            hist[i]++
        }
    }
    return hist
}

func dec2hex(n, beam int) string {
    hex := ""
    str := "0123456789abcdef"
    for i := 0; i < beam; i++ {
        m := n & 0xf
        hex = string(str[m]) + hex
        n -= m
        n >>= 4
    }
    return hex
}

func rgb2int(r, g, b int) int {
    return (((r >> 5) << 6) | ((g >> 5) << 3) | ((b >> 5) << 0))
}

func int2rgb(i int) (r, g, b int) {
    return ((i >> 6 & 0x7) << 5) + 16, ((i >> 3 & 0x7) << 5) + 16, ((i >> 0 & 0x7) << 5) + 16
}
