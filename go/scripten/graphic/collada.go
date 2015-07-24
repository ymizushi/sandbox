package main

import (
    "log"
    "fmt"
    "encoding/xml"
    "os"
)

func main() {
    readFile, err := os.Open("untitled.dae")
    if err != nil {
        fmt.Println(userFile, err)
        return
    }
    defer readFile

    buf := make([]byte, 1024)
    for {
        n, _ := readFile.Read(buf)
        if 0 == n {
            break
        }
        os.Stdout.Write(buf[:n])
    }



    str := `
    <?xml version="1.0" encoding="UTF-8"?>
    <Nicovideo>
        <thumb>
            <title>動画タイトル</title>
            <length>12:59</length>
        </thumb>
    </Nicovideo>
    `

    nicoXml := Nicovideo{Thumb{"", ""}}
    err := xml.Unmarshal([]byte(str), &nicoXml)

    if err != nil {
        log.Fatal(err)
        return
    }

    fmt.Println(nicoXml)
    fmt.Println("title: " + nicoXml.Thumb.Title)
    fmt.Println("length: " + nicoXml.Thumb.Length)
}

type Nicovideo struct {
    Thumb Thumb `xml:"thumb"`
}

type Thumb struct {
    Title string `xml:"title"`
    Length string `xml:"length"`
}
