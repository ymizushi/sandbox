package main

import (
    // "fmt"
    // "./graphic"

    "go/build"
    "image"
    _ "image/png"
    // "reflect"
    "path/filepath"
    "azul3d.org/gfx.v1"
    "azul3d.org/gfx/window.v2"
    "azul3d.org/keyboard.v1"
    // "azul3d.org/mouse.v1"
    "azul3d.org/lmath.v1"
    "log"
    "os"
)

var examplesDir string
var camNear float64 = 0.01
var camFar float64 = 1000.0

func absPath(relPath string) string {
    if len(examplesDir) == 0 {
        // Find assets directory.
        for _, path := range filepath.SplitList(build.Default.GOPATH) {
            path = filepath.Join(path, "src/azul3d.org/examples.v1")
            if _, err := os.Stat(path); err == nil {
                examplesDir = path
                break
            }
        }
    }
    return filepath.Join(examplesDir, relPath)
}

func createShader() *gfx.Shader {
    var glslVert = []byte(`
        #version 120
        
        attribute vec3 Vertex;
        attribute vec2 TexCoord0;
        
        uniform mat4 MVP;
        
        varying vec2 tc0;
        
        void main()
        {
            tc0 = TexCoord0;
            gl_Position = MVP * vec4(Vertex, 1.0);
        }
    `)

    var glslFrag = []byte(`
        #version 120
        
        varying vec2 tc0;
        
        uniform sampler2D Texture0;
        uniform bool BinaryAlpha;
        
        void main()
        {
            gl_FragColor = texture2D(Texture0, tc0);
            if(BinaryAlpha && gl_FragColor.a < 0.5) {
                discard;
            }
        }
    `)

    shader := gfx.NewShader("SimpleShader")
    shader.GLSLVert = glslVert
    shader.GLSLFrag = glslFrag
    return shader
}

func createCamera(r gfx.Renderer) *gfx.Camera {
    camera := gfx.NewCamera()
    camera.SetOrtho(r.Bounds(), camNear, camFar)
    // Move the camera back two units away from the card.
    camera.SetPos(lmath.Vec3{0, -2, 0})
    return camera
}

func loadPicture() image.Image {
    f, err := os.Open(absPath("assets/textures/texture_coords_1024x1024.png"))
    if err != nil {
        log.Fatal(err)
    }

    img, _, err := image.Decode(f)
    if err != nil {
        log.Fatal(err)
    }
    return img
}

func createTexture(img image.Image) *gfx.Texture {
    tex := gfx.NewTexture()
    tex.Source = img
    tex.MinFilter = gfx.LinearMipmapLinear
    tex.MagFilter = gfx.Linear
    tex.Format = gfx.DXT1RGBA
    return tex
}

func createCardMesh() *gfx.Mesh {
    cardMesh := gfx.NewMesh()
    cardMesh.Vertices = []gfx.Vec3{
        // Bottom-left triangle.
        {-1, 0, -1},
        {1, 0, -1},
        {-1, 0, 1},

        // Top-right triangle.
        {-1, 0, 1},
        {1, 0, -1},
        {1, 0, 1},
    }
    cardMesh.TexCoords = []gfx.TexCoordSet{
        {
            Slice: []gfx.TexCoord{
                {0, 1},
                {1, 1},
                {0, 0},

                {0, 0},
                {1, 1},
                {1, 0},
            },
        },
    }
    return cardMesh
}

func createCard(shader *gfx.Shader, tex *gfx.Texture, cardMesh *gfx.Mesh) *gfx.Object {
    card := gfx.NewObject()
    card.AlphaMode = gfx.AlphaToCoverage
    card.Shader = shader
    card.Textures = []*gfx.Texture{tex}
    card.Meshes = []*gfx.Mesh{cardMesh}
    return card
}

func gfxLoop(w window.Window, r gfx.Renderer) {
    camera := createCamera(r)
    shader := createShader()
    img := loadPicture()

    tex := createTexture(img)

    cardMesh := createCardMesh()
    card := createCard(shader, tex, cardMesh)

    go func() {
        events := make(chan window.Event, 256)
        // Have the window notify our channel whenever events occur.
        w.Notify(events, window.FramebufferResizedEvents|window.KeyboardTypedEvents)
        for e := range events {
            switch ev := e.(type) {
            case window.FramebufferResized:
                // Update the camera's projection matrix for the new width and
                // height.
                camera.Lock()
                camera.SetOrtho(r.Bounds(), camNear, camFar)
                camera.Unlock()

            case keyboard.TypedEvent:
                if ev.Rune == 'm' || ev.Rune == 'M' {
                    // Toggle mipmapping on the texture.
                    tex.Lock()
                    if tex.MinFilter == gfx.LinearMipmapLinear {
                        tex.MinFilter = gfx.Linear
                    } else {
                        tex.MinFilter = gfx.LinearMipmapLinear
                    }
                    tex.Unlock()
                }
            }
        }
    }()

    for {
        // Center the card in the window.
        b := r.Bounds()
        card.SetPos(lmath.Vec3{float64(b.Dx()) / 2.0, 0, float64(b.Dy()) / 2.0})

        // Scale the card to fit the window.
        s := float64(b.Dy()) / 2.0 // Card is two units wide, so divide by two.
        card.SetScale(lmath.Vec3{s, s, s})

        // Clear the entire area (empty rectangle means "the whole area").
        r.Clear(image.Rect(0, 0, 0, 0), gfx.Color{1, 1, 1, 1})
        r.ClearDepth(image.Rect(0, 0, 0, 0), 1.0)

        // Draw the textured card.
        r.Draw(image.Rect(0, 0, 0, 0), card, camera)

        // Render the whole frame.
        r.Render()
    }

    // for {
    //     r.Clear(image.Rect(0, 0, 0, 0), gfx.Color{1, 1, 1, 1})

    //     if w.Keyboard().Down(keyboard.Space) {
    //         r.Clear(image.Rect(0, 0, 100, 100), gfx.Color{1, 0, 0, 1})
    //     }

    //     if w.Mouse().Down(mouse.Left) {
    //         r.Clear(image.Rect(100, 100, 200, 200), gfx.Color{0, 0, 1, 1})
    //     }
    //     r.Render()
    // }
}

func makeProps() *window.Props{
    var props *window.Props = window.NewProps()
    // props.SetFullscreen(true)
    props.SetTitle("scripten")
    return props
}

func main() {
    window.Run(gfxLoop, makeProps())
}
