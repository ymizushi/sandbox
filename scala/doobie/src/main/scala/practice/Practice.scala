import doobie._
import doobie.implicits._
import cats.effect.IO
import scala.concurrent.ExecutionContext
import cats.effect._
import cats.implicits._
import doobie._
import doobie.implicits._
import doobie.h2._
import cats.effect.unsafe.implicits.global

case class Country(code: String, name: String, population: Long)

object  Practice {
    def main(args: Array[String]) = {
        println("hoge")
        H2App.run(Nil)
    }
}

object H2App extends IOApp {
  val transactor: Resource[IO, H2Transactor[IO]] =
    for {
      ce <- ExecutionContexts.fixedThreadPool[IO](32) 
      xa <- H2Transactor.newH2Transactor[IO](
              "jdbc:h2:mem:test;DB_CLOSE_DELAY=-1", 
              "sa", 
              "",
              ce,
            )
    } yield xa

  def run(args: List[String]): IO[ExitCode] =
    transactor.use { xa =>
      for {
        n <- sql"select 42".query[Int].unique.transact(xa)
        _ <- IO(println(n))
      } yield ExitCode.Success
    }
}