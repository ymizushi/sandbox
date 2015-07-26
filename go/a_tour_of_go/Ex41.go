package main
// http://golang-jp.org/pkg/fmt/

import (
    "code.google.com/p/go-tour/wc"
    "strconv"
    "strings"
)

func WordCount(s string) map[string]int {
     m := make(map[string]int)
     fields := strings.Fields(s)
     for _,v := range(fields) {
         _, ok := m[v]
         if ok {
             m[v] += 1
         } else {
             m[v] = 1
         }
     }
    return m
}

func CharCount(s string) map[string]int {
     m := make(map[string]int)
     for _,v := range(s) {
         char := strconv.QuoteRuneToASCII(v)
         _, ok := m[char]
         if ok {
             m[char] += 1
         } else {
             m[char] = 1
         }
     }
    return m
}

func main() {
     wc.Test(WordCount)
}
