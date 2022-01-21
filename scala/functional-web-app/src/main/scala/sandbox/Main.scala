package sandbox

import io.circe.Encoder
import io.circe.`export`.Exported
import io.circe.syntax.EncoderOps
import io.circe.generic.auto.exportEncoder

object Main extends App {
  case class Parts(s: Seq[String])
  val encoder: Exported[Encoder.AsObject[Parts]] = exportEncoder[Parts]
  val circuit = Parts(List("a", "b", "c", "d"))
  println(circuit.asJson)
}
