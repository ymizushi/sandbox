package script

import (
    "strings"
)

// interface
type Exp interface {
    Eval() *Value
}

// Token
type Token struct {
    Type string
    Str string
}

func NewToken(t, s string) *Token {
    return &Token{t, s}
}

// Value
type Value struct {
    v interface{}
}

func NewValue(v interface{}) *Value {
    return &Value{v}
}

func (self *Value) Eval() *Value {
    return self
}

// Number
type Number struct {
    v interface{}
}

// PlusExp
type PlusExp struct {
    args *[]Exp
}

func (self *PlusExp) Eval() *Value {
    var result int = 0
    for _, exp := range (*self.args) {
        var value *Value = exp.Eval()
        result += value.v.(int)
    }
    return NewValue(result)
}

// func
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
