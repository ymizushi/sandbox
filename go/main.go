package main

import (
    "encoding/json"
    // "fmt"
    "log"
    "os/exec"
    "bytes"
    "strings"
    "github.com/go-martini/martini"
)

type Task struct {
    Content string
}

func receiveCommand(command string) string {
    var jsonBlob = []byte(command)
    var task Task
    err := json.Unmarshal(jsonBlob, &task)
    if err != nil {
        return "false"
    }
    return task.Content
}

func execCommand(command string, c chan string) {
    cmd := exec.Command(command)
    cmd.Stdin = strings.NewReader("some input")
    var out bytes.Buffer
    cmd.Stdout = &out
    err1 := cmd.Run()
    if err1 != nil {
        log.Fatal(err1)
    }
    c <- out.String()
}

func main() {
    c := make(chan string)

    m := martini.Classic()
    m.Get("/:command", func(params martini.Params) string {
        go execCommand(params["command"], c)
        return <- c
    })
    m.Post("/post", func(params martini.Params) string {
        return "failed"
    })
    m.Run()
}
