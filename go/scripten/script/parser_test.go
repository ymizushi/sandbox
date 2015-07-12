package script

import "testing"


func TestTokenizer(t *testing.T) {
    tokenList := Tokenize("( def hoge 1 )")
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
