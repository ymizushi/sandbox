package gomi

import (
    "os"
    "bufio"
"io"
"log"
)

type Renderer struct {
}

func NewRenderer() *Renderer {
    renderer := Renderer {}
    return &renderer
}

func (renderer *Renderer) Render(path string, params map[string]string) string {
    fp, err := os.Open(path)
    if err != nil{
       log.Println(err)
       panic(err)
    }

    var output []byte
    reader := bufio.NewReaderSize(fp, 50)
    for {
       line, _, readError := reader.ReadLine()
       if readError == io.EOF {
           break
       }
       if readError != nil {
           log.Println(readError)
           panic(readError)
       }
       for _, v := range(line) {
           output = append(output, v)
       }
    }
    return string(output)
}
