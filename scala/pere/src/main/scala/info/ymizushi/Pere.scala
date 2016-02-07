package info.ymizushi

import scala.concurrent.Future
import scala.util.{Failure, Success}
import scala.concurrent.ExecutionContext.Implicits.global
import Thread.sleep

object Pere {
  def main(args: Array[String]): Unit = {
    val commit = Commit(Tree(Seq(Blob("hoge"),Blob("piyo"), Tree(Seq(Blob("foo"))))))
    val f = Future[String] {
      sleep(100)
      println("hoge1")
      "hoge"
     }
    f.onComplete[Unit] {
      case Success(_) => println("hoge success")
      case Failure(_) => println("hoge failed")
    }
    println("hoge3")
    sleep(1000)
  }
}
