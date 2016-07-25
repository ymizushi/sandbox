package gomi

type Renderer struct {
}

func NewRenderer() *Renderer {
    renderer := Renderer {}
    return &renderer
}

func (renderer *Renderer) Render(path string, params map[string]string) string {
    return "hoge"
}
