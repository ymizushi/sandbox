package template


interface Parser {
}

type State struct {
    State int
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

func (p *Parser) Parse(c byte, params map[string]string) []byte {
    swtich c {
        case START_BRACKET_CHARACTER:
    }

}
