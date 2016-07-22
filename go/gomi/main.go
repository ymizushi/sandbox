package main 

import "./gomi"

func main() {
    server := gomi.NewServer("8080")
    server.Dispatch("/", func () (int, string) {
        return 200, "resultsuccess"
    })
    server.Start()
}
