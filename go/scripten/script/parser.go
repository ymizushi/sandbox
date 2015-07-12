package script

import (
    "strings"
    "container/list"
)

type TokenReader struct {
}

func Tokenize(str string) *list.List {
    tokenStrArray := strings.Fields(str)
    list := list.New()
    for _, v := range tokenStrArray {
        list.PushBack(v)
    }
    return list
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
