package script

import "testing"

func TestTokenize(t *testing.T) {
    tokenList := Tokenize("( def hoge 1 )")
    if (*tokenList)[0].Str != "(" {
        t.Errorf("%sだよ", (*tokenList)[0].Str)
    }

    if (*tokenList)[1].Str != "def" {
        t.Errorf("%sだよ", (*tokenList)[1].Str)
    }

    if (*tokenList)[2].Str != "hoge" {
        t.Errorf("%sだよ", (*tokenList)[2].Str)
    }
}

func TestEval(t *testing.T) {
}

