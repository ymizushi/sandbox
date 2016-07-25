package main 

import "./gomi"

func main() {
    server := gomi.NewServer("8080")
    server.Dispatch("/", func () (int, string) {
        renderer := gomi.NewRenderer()
        return 200, renderer.Render("index.html", map[string]string {"hoge":"1"})
    })
    server.Start()
}
