package info.ymizushi

/**
  * Created by yuta_mizushima on 2016/02/05.
  */
case class Tree(children: Seq[Element]) extends Element {
  override def toString: String  = "(Tree: " + children.map(_.toString).fold("")((z:String, n:String) => z+n) + ")"
}
