package script

import (
    "strings"
    "container/list"
)

func TokenizeToList(str string) *list.List {
    tokenStrArray := strings.Fields(str)
    list := list.New()
    for _, v := range tokenStrArray {
        list.PushBack(v)
    }
    return list
}

type Token struct {
    Str string
    Type string
}

func Tokenize(str string) []Token {
    tokenStrArray := strings.Fields(str)
    tokenArray := make([]Token, len(tokenStrArray))
    for i, v := range tokenStrArray {
        tokenArray[i] = Token{v, ""}
    }
    return tokenArray
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
