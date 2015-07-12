package graphic

import (
    "strconv"
    "azul3d.org/gfx.v1"
)

type GraphicContext struct {
    context gfx.Renderer
}

func NewGraphicContext(r gfx.Renderer) *GraphicContext {
    return &GraphicContext{r}
}

func (gc *GraphicContext) DrawPoint(p *Point) {
    fmt.Println("DrawPoint")
}

func (gc *GraphicContext) DrawRect(r *Rect) {
    fmt.Println("DrawRect")
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


type Size struct {
    Width  float64
    Height float64
}

func (s *Size) NewSize(width float64, height float64) *Size {
    return &Size{width, height}
}

type Rect struct {
    start *Point
    size *Size
}

func (s *Size) NewRect(point *Point, size *Size) *Rect {
    return &Rect{point, size}
}

func (r *Rect) Draw(graphicContext *GraphicContext) {
    graphicContext.DrawRect(r)
}
