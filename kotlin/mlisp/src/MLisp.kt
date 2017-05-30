class Tokenizer(val tokenString: String) {
    fun tokenize(): List<Token> {
        val stringList: List<String> = tokenString.split(" ")
        return stringList.map { s -> Token(s) }
    }
}

enum class TokenType {
    BRACKET_START,
    PLUS,
    BRACKET_END,
    NUMBER,
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

//    fun <T>toValue(): Value {
//        when (this.type()) {
//            TokenType.NUMBER -> {
//                return Value<String>(s)
//            }
//            else -> {
//                return Value<String>(s)
//            }
//        }
//    }

    fun isNumber(s: String): String {
        try {
            s.toInt()
            return s
        } catch (e: java.lang.NumberFormatException) {
            return ""
        }
    }
}

interface Value
class NumberValue(v: Int): Value
class StringValue(v: String): Value

interface Node {
    fun eval(): Value
}


abstract class Tree : Node {
    val children = mutableListOf<Node>()

    fun addChildren(node: Node) {
        children.add(node)
    }
}

class PlusTree: Tree() {
    fun eval(): Value {
    }

}


class Parser {
    fun parse(tokenList: List<Token>, node: Node?): Node? {
        for ((index, token) in tokenList.withIndex()) {
            when (token.type()) {
                TokenType.BRACKET_START -> {
                    if (node == null) {
                        return this.parse(tokenList.subList(index + 1, tokenList.size - 1), Tree())
                    } else {
                        val newNode = Tree()
                        node.addChildren(newNode)
                        return this.parse(tokenList.subList(index + 1, tokenList.size - 1), newNode)
                    }
                }
                TokenType.BRACKET_END -> {
                    return node
                }
                else -> {
                    node?.addChildren(token)
                }
            }
        }
        return node
    }
}

fun main(args: Array<String>) {
    val input = "( + 1 2 3 )"
    val tokenizer = Tokenizer(input)
    val tokenList = tokenizer.tokenize()
    val node = Parser().parse(tokenList, null)
    print(node.eval())
}
