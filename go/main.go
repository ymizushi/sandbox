package main
import "fmt"

type A struct {
    a int
    b string
}

type B struct {
    A
}

func (self A) hoge() {
    fmt.Println(self.a)
}

type C interface {
    D() int
}

func main() {
    a := A {a:1, b:"sato"}
    a.hoge()

    b := B{}
    b.hoge()
}
