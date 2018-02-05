class SuperElement

class Element extends SuperElement

class SubElement extends Element


object Common {
  def main(args: Array[String]) = {
    val cov: Covariant[Element] = new Covariant[SubElement]
    val contra: Contravariant[Element] = new Contravariant[SuperElement]
  }
}
