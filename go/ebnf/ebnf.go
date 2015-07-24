package main

import (
    "fmt"
    "golang.org/x/exp/ebnf"
    "io"
    "string"
)

var goodGrammars = []string{
    `Program = .`,

    `Program = foo .
     foo = "foo" .`,

    `Program = "a" | "b" "c" .`,

    `Program = "a" … "z" .`,

    `Program = Song .
     Song = { Note } .
     Note = Do | (Re | Mi | Fa | So | La) | Ti .
     Do = "c" .
     Re = "d" .
     Mi = "e" .
     Fa = "f" .
     So = "g" .
     La = "a" .
     Ti = ti .
     ti = "b" .`,
}


func main() {
    fmt.Println("hoge")
    ebnf.Parse("ebnf.ebnf", &bytes.Reader{"})
}

