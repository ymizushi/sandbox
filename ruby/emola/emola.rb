class Tokenizer
    def initialize text
        @text = text
    end

    def tokenize
        tokens = @text.split(" ").map {|s|
            s.delete(" ")
        }.map {|s|
            Token.new(s)
        }
    end
end

class TokenType
    START_BRACKET = "("
    END_BRACKET = ")"
    PLUS = "+"
    NUMBER = "number"
end

class Token
    attr :type

    def initialize s
        @s = s
        @type = self.get_type
    end

    def get_type
        if @s == "("
            TokenType::START_BRACKET
        elsif @s == ")"
            TokenType::END_BRACKET
        elsif @s.match(/^[0-9].*$/) 
            TokenType::NUMBER
        elsif @s == "+" 
            TokenType::PLUS
        else 
        end
    end
end

class Value
    def initialize v
        @v =v
    end

    def eval
        @v
    end
end

class Parser
    def parse tokens, node
        tokens.each_with_index { |token, index|
            case token.get_type()
            when TokenType::START_BRACKET then
                new_node = Node.new
                if node != nil 
                    node.add(new_node)
                end
                return self.parse(tokens[index+1, tokens.length], new_node)
            when TokenType::END_BRACKET then
                return node
            when TokenType::NUMBER then
                node.add(Value.new(token.s.to_i))
                return self.parse(tokens[index+1, tokens.length], node)
            when TokenType::PLUS then
                node.add(Value.new(token.s))
                return self.parse(tokens[index+1, tokens.length], node)
            else
            end
        }
    end
end

class Node
    def initialize
        @children = []
    end

    def add token
        @children.push(token)
    end

    def eval
        if @children[0].type == TokenType::PLUS
            return @children[1, @children.length].map {|token|
                token.eval
            }.reduce {|sum, n|
                sum + n
            }
        end
    end
end

text = "(+ 1 2 3 ( + 2 3 4 5 ) )"
tokens = Tokenizer.new(text).tokenize
node = Parser.new.parse(tokens, nil)
p node.eval
node.eval
