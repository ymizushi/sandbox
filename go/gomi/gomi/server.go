package gomi

import "net/http"
import "fmt"

type Server struct {
    port string
}

func NewServer(port string) *Server {
    server := Server {}
    server.port = port
    return &server
}

func (server *Server) Dispatch(str string, fn func() (int, string) ) {
    http.HandleFunc(str, func (w http.ResponseWriter, r *http.Request) {
        _, content := fn()
      fmt.Fprintf(w, content)
  })
}

func (server *Server) Start() {
    fmt.Printf("server is runnnin on port:%v...\n", server.port)
    http.ListenAndServe(":" + server.port, nil)
}

