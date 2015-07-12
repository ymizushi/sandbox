package script

import (
    "strings"
    "container/list"
)

type TokenReader struct {
}

func Tokenize(str string) []Token {
    tokenStrArray = strings.Fields(str)
    list := list.New()
    for i, v range tokenStrArray {

    }
    return 
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

