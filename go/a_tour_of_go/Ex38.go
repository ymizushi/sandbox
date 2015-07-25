package main

import (
	"fmt"
	"log"
	"net/http"
)

type String string

func (self String) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s", self)
}

type Struct struct {
	Greeting string
	Punct    string
	Who      string
}

func (self *Struct) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s, %s, %s", self.Greeting, self.Punct, self.Who)
}

func main() {
	log.Println("Stated server...")
	http.Handle("/", String("index page."))
	http.Handle("/string", String("I'm a frayed knot."))
	http.Handle("/struct", &Struct{"Hello", ":", "Gophers!"})

	e := http.ListenAndServe("localhost:4000", nil)

	if e != nil {
		log.Panic(e)
	}
}
