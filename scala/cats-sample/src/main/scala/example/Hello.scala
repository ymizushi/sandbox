package example

object Hello extends Greeting with App {
  println(greeting)
  import JsonWriterInstances._
  Json.toJson(Person("Dave", "dave@example.com"))
}

trait Greeting {
  lazy val greeting: String = "hello"
}


sealed trait Json
final case class JsObject(get: Map[String, Json]) extends Json

final case class JsString(get: String) extends Json

final case class JsNumber(get: Double) extends Json

final case object JsNull extends Json

trait JsonWriter[A] {
  def write(value: A): Json
}

final case class Person(name: String, email: String)

object JsonWriterInstances {
  implicit val stringWriter: JsonWriter[String] = new JsonWriter[String] {
    def write(value: String): Json = JsString(value)
  }

  implicit val personWriter: JsonWriter[Person] = new JsonWriter[Person] {
    def write(value: Person): Json = JsObject(Map(
      "name" -> JsString(value.name),
      "email" -> JsString(value.email))
    )
  }

}

object Json {
  def toJson[A](value: A)(implicit w: JsonWriter[A]): Json = 
    w.write(value)
}
