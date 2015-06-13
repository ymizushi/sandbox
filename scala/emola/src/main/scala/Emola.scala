package info.ymizushi.emola

object Emola {
  def main(args: Array[String]) {
    println("hoge")
  }
}

case class Token(s: String)

object TokenReader {
  def read(tokens: String):List[Token] {

  }
}

object Parser {
  def parse(tokens: List[Token]): List[Expression]
}

trait Expression {
  def eval: Value
}

case class Value[A](v: A) extends Expression {
  def eval: Value = this.v
}

class Number extends Value

class String extends Value

case class Plus(numbers: List[Number]) extends Expression  {
  def eval: Value = this.numbers.sum
}

case class Minus(numbers: List[Number]) extends Expression {
  def eval: Value = this.numbers.reduceLeft(_ + _)
}

