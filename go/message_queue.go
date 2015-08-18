package main

import (
    "fmt"
    "log"
    "net/http"
    "time"
)

type Message struct {
    URL string
}

func main() {
    log.Println("Stated server...")

    ch := make(chan Message)
    http.HandleFunc("/add", func (w http.ResponseWriter, r *http.Request) {
        time.Sleep(5000 * time.Millisecond)
        ch <- Message{r.URL.RawQuery}
    })

    go func() {
        for {
            fmt.Printf("%s", (<-ch).URL)
        }
    }()

    e := http.ListenAndServe("localhost:4000", nil)

    if e != nil {
        log.Panic(e)
    }
}
