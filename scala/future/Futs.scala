import scala.concurrent.{Future, Await}
import scala.concurrent.duration._

import scala.concurrent.ExecutionContext.Implicits.global

object Futs {
  def main(args: Array[String]): Unit =  {
    Await.result(requestToTwitter.flatMap { os =>
      requestToFacebook.flatMap { _ =>
        requestToGoogle
      }
    }, 10.second)

    Await.result(
      (for {
        _ <- requestToTwitter
        _ <- requestToFacebook
      } yield requestToGoogle), 2.second)

    Unit
  }

  def requestToTwitter: Future[Option[String]] = Future {
    println("request to twitter")
    Thread.sleep(1000)
    Some("hoge")
  }

  def requestToFacebook: Future[Option[Int]] = Future {
    println("request to Facebook")
    Some(10)
  }

  def requestToGoogle: Future[List[Int]] = Future {
    println("request to goole")
    List(1,2,3,4)
  }
}








