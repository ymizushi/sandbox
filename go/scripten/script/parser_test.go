package script

import "testing"

func Assert(result, expects interface{}, t *testing.T) {
    if result != expects {
        t.Errorf("asset failed: result: %s; expects: %s;", result, expects)
    }
}

func TestTokenize(t *testing.T) {
    tokenList := Tokenize("( def hoge 1 )")
    Assert((*tokenList)[0].Str, "(", t)
    Assert((*tokenList)[1].Str, "def", t)
    Assert((*tokenList)[2].Str, "hoge", t)
}

func TestEval(t *testing.T) {
    Assert(NewValue(1).v, 1, t)
    Assert(NewValue("hoge").v, "hoge", t)

    value := NewValue("hoge")
    Assert(value.Eval(), value, t)
}

func TestPlusExp(t *testing.T) {
    var args []Exp = make([]Exp, 3)
    args[0] = &Value{1}
    args[1] = &Value{2}
    args[2] = &Value{3}
    plusExp := &PlusExp{"+", &args}
    result := plusExp.Eval()
    Assert(result.v, 6, t)
}

