package info.ymizushi

case class Blob(path: String) extends Element {
  override def toString: String = "(Blob: " + path + ")"
}
