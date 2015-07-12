package script

import (
    "strings"
)

type TokenReader struct {
}

func Tokenize(str string) []string {
    return strings.Fields(str)
}

type Token struct {
    Str string
}

type Expression struct {
}

type Value struct {
}

type Parser interface {
    Parse() Value
}

type Evalable interface {
    Eval() Value
}

