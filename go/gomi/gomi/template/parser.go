package main

type Parser interface {
    Parse(c byte, params map[string]string) bool
}

type State struct {
    State StateType
    Vars []byte
}

const (
    INIT = iota
    START_BRACKET
    CONTENT
    END_BRACKET
    GOAL
)

const (
    START_BRACKET_CHARACTER = 123
    END_BRACKET_CHARACTER = 125
)

func (s *State) Parse(c byte, params map[string]string) ([]byte, error) {
    switch c {
        case START_BRACKET_CHARACTER:
            // 
    }
    return nil, nil
}

func main() {

}
