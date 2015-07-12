package main

import (
    "fmt"
    "./graphic"
    "image"
    "reflect"
    "azul3d.org/gfx.v1"
    "azul3d.org/gfx/window.v2"
    "azul3d.org/keyboard.v1"
    "azul3d.org/mouse.v1"
)

func gfxLoop(w window.Window, r gfx.Renderer) {
    go func() {
        events := make(chan window.Event, 256)
        w.Notify(events, window.AllEvents)
        for event := range events {
            fmt.Println("Event type:", reflect.TypeOf(event))
            fmt.Println(event)
        }
    }()

    for {
        r.Clear(image.Rect(0, 0, 0, 0), gfx.Color{1, 1, 1, 1})

        if w.Keyboard().Down(keyboard.Space) {
            r.Clear(image.Rect(0, 0, 100, 100), gfx.Color{1, 0, 0, 1})
        }

        if w.Mouse().Down(mouse.Left) {
            r.Clear(image.Rect(100, 100, 200, 200), gfx.Color{0, 0, 1, 1})
        }
        r.Render()
    }
}

func main() {
    fmt.Println("hoge")
    c := graphic.NewColor(1,2,3,4)
    fmt.Println(c.Str())
    window.Run(gfxLoop, nil)
}
