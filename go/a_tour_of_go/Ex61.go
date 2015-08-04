package main

import (
    "io"
    "os"
    "strings"
)

type rot13Reader struct {
    r io.Reader
}

type MyError struct {
    message string
}

func (self MyError) Error() string {
   return  self.message
}

func (r rot13Reader) Read(p []byte) (n int, err error) {
    return 1, MyError{"hoge"}
}

func main() {
    s := strings.NewReader(
        "Lbh penpxrq gur pbqr!")
    r := rot13Reader{s}
    io.Copy(os.Stdout, &r)
}
