package main
 
import (
	"fmt"
	"io/ioutil"
	"os"
 
	"golang.org/x/term"
)
 
func main() {
	if hasPipeData() {
		data, _ := fromPIPE()
		fmt.Print(data)
	}
}
 
func fromPIPE() (string, error) {
	if hasPipeData() {
		b, err := ioutil.ReadAll(os.Stdin)
		if err != nil {
			return "", err
		}
		return string(b), nil
	}
	return "", nil
}
 
func hasPipeData() bool {
	return !term.IsTerminal(syscall.Stdin)
}
