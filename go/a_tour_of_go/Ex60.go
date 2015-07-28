package main

import (
    "code.google.com/p/go-tour/pic"
    "image"
    "image/color"
)

type Image struct {
    X int
    Y int
    Width int
    Height int
}

func  (self Image) ColorModel() color.Model {
    mfunc := func (color color.Color) color.Color { return color }
    color := color.ModelFunc(mfunc)
    return color
}

func (self Image) Bounds() image.Rectangle {
    return image.Rectangle{image.Point{self.X, self.Y}, image.Point{self.X+self.Width, self.Y+self.Height}}
}

func (self Image) At(x, y int) color.Color {
    return color.RGBA{uint8(x), uint8(y), uint8(x), uint8(y)}
}

func main() {
    m := Image{10, 20, 100, 200}
    pic.ShowImage(m)
}
