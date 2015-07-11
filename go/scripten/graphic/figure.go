package graphic

import (
    "strconv"
)

type GraphicContext struct {
    contex string
}

func NewGraphicContext() *GraphicContext {
    return &GraphicContext{"hoge"}
}

func (gc *GraphicContext) DrawPoint(p *Point) {
}

type Color struct {
    R uint64
    G uint64
    B uint64
    A uint64
}

func NewColor(r uint64, g uint64, b uint64, a uint64) *Color {
    return &Color{r, g, b, a}
}

func (c *Color) Str() string {
    r_str := strconv.FormatUint(c.R, 10)
    g_str := strconv.FormatUint(c.G, 10)
    b_str := strconv.FormatUint(c.B, 10)
    a_str := strconv.FormatUint(c.A, 10)
    return r_str + g_str + b_str + a_str
}

type Point struct {
    X float64
    Y float64
    Z float64
}

func NewPoint(x float64, y float64, z float64) *Point {
    return &Point{x, y ,z}
}

func (p *Point) Draw(graphicContext *GraphicContext) {
    graphicContext.DrawPoint(p)
}
