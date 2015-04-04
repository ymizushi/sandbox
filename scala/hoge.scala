class Piyo {
  override def toString: String = {
    "piyo"
  }
  println()
  def +() {

  }

}

object Hoge {
  def main(args: Array[String]) {
    val piyo: Piyo = new Piyo
    println(piyo.toString)
    println(1.+(2))
    1.+(2).println
  }
}

