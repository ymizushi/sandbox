import doobie._
import doobie.implicits._
import cats.effect.IO
import scala.concurrent.ExecutionContext

import cats.effect.unsafe.implicits.global

case class Country(code: String, name: String, population: Long)

object  Practice {
    def main(args: Array[String]) = {
        println("hoge")

        val xa = Transactor.fromDriverManager[IO](
          "org.postgresql.Driver", "jdbc:postgresql:world", "postgres", ""
        )

        def find(n: String): ConnectionIO[Option[Country]] =
          sql"select code, name, population from country where name = $n".query[Country].option
        find("France").transact(xa).unsafeRunSync()

        import cats.effect._
import cats.implicits._
import doobie._
import doobie.implicits._
import doobie.h2._

object H2App extends IOApp {

  // Resource yielding a transactor configured with a bounded connect EC and an unbounded
  // transaction EC. Everything will be closed and shut down cleanly after use.
  val transactor: Resource[IO, H2Transactor[IO]] =
    for {
      ce <- ExecutionContexts.fixedThreadPool[IO](32) // our connect EC
      xa <- H2Transactor.newH2Transactor[IO](
              "jdbc:h2:mem:test;DB_CLOSE_DELAY=-1", // connect URL
              "sa",                                   // username
              "",                                     // password
              ce,                                     // await connection here
            )
    } yield xa


  def run(args: List[String]): IO[ExitCode] =
    transactor.use { xa =>

      // Construct and run your server here!
      for {
        n <- sql"select 42".query[Int].unique.transact(xa)
        _ <- IO(println(n))
      } yield ExitCode.Success

    }

}
    }
}