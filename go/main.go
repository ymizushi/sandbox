package main

import "github.com/go-martini/martini"

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "satoshun sugoi"
  })
  m.Run()
}
