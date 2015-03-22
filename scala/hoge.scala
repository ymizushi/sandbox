import java.util.{Date, Locale}
import java.text.DateFormat
import java.text.DateFormat._

object Timer {
  def oncePerSecond(callback: () => Unit) {
    callback()
  }
  
  def timeFlies()  {
    println("time flies like an arrow...")
  }

  def add(x: Integer): Integer =  {
    x + x
  }
  
  def main(args: Array[String]) {
    // oncePerSecond(timeFlies)
    // println(add(20))
  }
}
