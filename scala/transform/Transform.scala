object Transformer {
  def main(args: Array[String]) = {
    println("hoge")
  }
}

trait EitherF[A, B] {
  def right(f: Future[B]): EitherF[A, B]
  def left(f: Future[A]): EitherF[A, B]
  def map[C](f: B => C): EitherF[A, C]
  def flatMap[C](f: B => EitherF[A, C]): EitherF[A, C]
}

class EitherF[A, B](value: Future[Either[A, B]]) extends EitherF[A, B] {
  def right(f: Future[B]): EitherF[A, B] = {

  }
  
  def left(f: Future[A]): EitherF[A, B] = {
  }

  def map[C](f: B => C): EitherF[A, C] = {
    value.flatMap(e => Future.successful(e.map(f)))
  }

  def flatMap[C](f: B => EitherF[A, C]): EitherF[A, C] = {
    value.flatMap(e => Future.successful(e.map(f)))
  }
}

case class UserID(value: Long)

case class Error(value: String)

trait UserRepository {
  def find(id: UserId): EitherF[Error, Int]]
}

class UserRepositoryImpl {
  def find(id: UserId): EitherT[Future, Error, Int] = {
  }
}

