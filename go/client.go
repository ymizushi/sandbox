package main
import "net"
import "fmt"
import "bufio"

func main() {
    conn, err := net.Dial("tcp", "localhost:8000")
    if err != nil {
        fmt.Fprintf(conn, "error GET / HTTP/1.0\r\n\r\n")
    }
    fmt.Fprintf(conn, "GET / HTTP/1.0\r\n\r\n")
    status, err := bufio.NewReader(conn).ReadString('\n')
    fmt.Printf(status)
}
