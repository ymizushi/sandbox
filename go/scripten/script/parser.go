package script

import (
    "strings"
)

type Token struct {
    Str string
    Type string
}

type Exp interface {
    Eval() *Value
}

// Value
type Value struct {
    v interface{}
}

func (self *Value) Eval() *Value {
    return self
}


type Number struct {
    v interface{}
}

type PlusExp struct {
    op string
    args *[]Exp
}

func (self *PlusExp) Eval() *Value {
    var result int = 0
    for _, exp := range (*self.args) {
        var value *Value = exp.Eval()
        result += value.v.(int)
    }
    return &Value{result}
}

func Tokenize(str string) *[]Token {
    tokenStrArray := strings.Fields(str)
    tokenArray := make([]Token, len(tokenStrArray))
    for i, v := range tokenStrArray {
        tokenArray[i] = Token{v, ""}
    }
    return &tokenArray
}

// func Parse(tokens *[]Token) *[]Exp {
// }


// Eval(Parse(Tokenize("(def hoge 1)")))
