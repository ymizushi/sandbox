class Tokenizer(val tokenString: String) {
    fun tokenize(): List<Token> {
        val stringList: List<String> = tokenString.split(" ")
        return stringList.map { s -> Token(s) }
    }
}

class Token(val s: String) {
    fun type(): TokenType {
        when (s) {
            "(" -> {
                return TokenType.BRACKET_START
            }
            ")" -> {
                return TokenType.BRACKET_END
            }
            "+" -> {
                return TokenType.PLUS
            }
            isNumber(s) -> {
                return TokenType.NUMBER
            }
        }
        return TokenType.NUMBER
    }

    fun eval(): Any {
        when (this.type()) {
            TokenType.NUMBER -> {
                return s.toInt()
            }
            else -> {
                return s
            }
        }
    }

    fun isNumber(s: String): String {
        try {
            s.toInt()
            return s
        } catch (e: java.lang.NumberFormatException) {
            return ""
        }
    }
}

enum class TokenType {
    BRACKET_START,
    PLUS,
    BRACKET_END,
    NUMBER,
}

class Node() {
    val children: MutableList<Node> = MutableList<Node>()
    fun add(node: Node) {
        children.add(node)
    }
}

class Parser {
    fun parse(tokenList: List<Token>, node: Node?): Node? {
        for ((index, token) in tokenList.withIndex()) {
            when(token.type()) {
                TokenType.BRACKET_START -> {
                    if (node == null) {
                        return this.parse(tokenList.subList(index+1, tokenList.size-1), node)
                    } else {
                        val newNode = Node()
                        node.add(newNode)
                        return this.parse(tokenList.subList(index+1, tokenList.size-1), newNode)
                    }
                }
                TokenType.BRACKET_END -> {
                    return node
                }
                else -> {
                    node.add(token)
                }
            }
        }
    }
}

fun main(args: Array<String>) {
    val input = "( + 1 2 3 )"
    val tokenizer = Tokenizer(input)
    val tokenList = tokenizer.tokenize()
    print(tokenList)
}
