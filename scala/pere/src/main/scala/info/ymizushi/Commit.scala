package info.ymizushi

/**
  * Created by yuta_mizushima on 2016/02/05.
  */
case class Commit(tree: Tree) extends Element{
  override def toString: String  = "(Commit: " + tree.toString + ")"
}
