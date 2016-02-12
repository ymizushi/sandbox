package info.ymizushi.emola

object Emola {
  def main(args: Array[String]) =
    println("hoge")
}

case class Token(s: String)

trait TokenReader {
  def read(tokenStr: String): Seq[Token]
}

trait Parser[A] {
  def parse(tokens: Seq[Token]): Seq[Expression[A]]
}

trait Expression[A] {
  def eval: A
}

case class Value[A](v: A)

class Number(v: Int) extends Value {
  def plus(v: Number): Number =
    new Number(this.v) 

}

class Str(s: String) extends Value

class Plus(numbers: Seq[Number]) extends Expression[Number]  {
  def eval: Number = this.numbers.foldLeft(new Number(0))(_ plus _)
}

// case class Minus(numbers: List[Number]) extends Expression {
//   def eval: Value = this.numbers.reduceLeft(_ + _)
// }
// 
