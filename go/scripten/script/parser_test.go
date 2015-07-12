package script

import "testing"


func TestTokenizeToList(t *testing.T) {
    tokenList := TokenizeToList("( def hoge 1 )")
    first := tokenList.Front()
    if first.Value != "(" {
        t.Errorf("%sだよ", first.Value)
    }
    second := first.Next()
    if second.Value != "def" {
        t.Errorf("%sだよ", second.Value)
    }
    third := second.Next()
    if third.Value != "hoge" {
        t.Errorf("%sだよ", third.Value)
    }
    fourth := third.Next()
    if fourth.Value != "1" {
        t.Errorf("%sだよ", fourth.Value)
    }
}

func TestTokenize(t *testing.T) {
    tokenList := Tokenize("( def hoge 1 )")
    if tokenList[0].Str != "(" {
        t.Errorf("%sだよ", tokenList[0].Str)
    }

    if tokenList[1].Str != "def" {
        t.Errorf("%sだよ", tokenList[1].Str)
    }

    if tokenList[2].Str != "hoge" {
        t.Errorf("%sだよ", tokenList[2].Str)
    }
}
