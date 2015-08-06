package main

import (
    "io"
    "os"
    "strings"
    "fmt"
)


type MyError struct {
    message string
}

func (self MyError) Error() string {
   return  self.message
}

type rot13Reader struct {
    r io.Reader
}

func (self rot13Reader) Read(p []byte) (int, error) {
    // alphabetMap := map[string]string{
    //    "a":"n",
    //    "b":"o",
    //    "c":"p",
    //    "d":"q",
    //    "e":"r",
    //    "f":"s",
    //    "g":"t",
    //    "h":"u",
    //    "i":"v",
    //    "j":"w",
    //    "k":"x",
    //    "l":"y",
    //    "m":"z",
    //    "n":"a",
    //    "o":"b",
    //    "p":"c",
    //    "q":"d",
    //    "r":"e",
    //    "s":"f",
    //    "t":"g",
    //    "u":"h",
    //    "v":"i",
    //    "w":"j",
    //    "x":"k",
    //    "y":"l",
    //    "z":"m",
    //    "A":"N",
    //    "B":"O",
    //    "C":"P",
    //    "D":"Q",
    //    "E":"R",
    //    "F":"S",
    //    "G":"T",
    //    "H":"U",
    //    "I":"V",
    //    "J":"W",
    //    "K":"X",
    //    "L":"Y",
    //    "M":"Z",
    //    "N":"A",
    //    "O":"B",
    //    "P":"C",
    //    "Q":"D",
    //    "R":"E",
    //    "S":"F",
    //    "T":"G",
    //    "U":"H",
    //    "V":"I",
    //    "W":"J",
    //    "X":"K",
    //    "Y":"L",
    //    "Z":"M",
    // }

    for i:=0;i<len(p);i=i+1 {
        p[i] = p[i] + 14
    }
    return self.r.Read(p)
}

func main() {
    s := strings.NewReader("Lbh penpxrq gur pbqr!")
    r := rot13Reader{s}
    result, err := io.Copy(os.Stdout, r)
    if err == nil {
        fmt.Println(result)
    } else {
        panic(err)

    }
}
