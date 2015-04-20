case class Commit(tree: Tree) extends Element{
  override def toString: String  = "(Commit: " + tree.toString + ")"
}

case class Tree(children: Seq[Element]) extends Element {
  override def toString: String  = "(Tree: " + children.map(_.toString).fold("")((z:String, n:String) => z+n) + ")"
}

case class Blob(path: String) extends Element {
  override def toString: String = "(Blob: " + path + ")"
}

trait Element {
  override def toString: String = "Element"
}

trait Hoge {
  def bar = toString
}

class ConcreateHoge extends Hoge with Element

object Pere {
  def main(args: Array[String]): Unit = {
    val commit = Commit(Tree(Seq(Blob("hoge"),Blob("piyo"), Tree(Seq(Blob("foo"))))))
    println(commit.toString)
  }
}
