package script

import (
    "testing"
)

func TestTokenizer(t *testing.T) {
    hoge := Tokenize("( def hoge 1 )")
    if hoge[0] != "(" {
        t.Errorf("(じゃないよ")
    }
    if hoge[1] != "def" {
        t.Errorf("defじゃないよ")
    }
    if hoge[2] != "hoge" {
        t.Errorf("hogeじゃないよ")
    }
    if hoge[3] != "1" {
        t.Errorf("1じゃないよ")
    }
}
