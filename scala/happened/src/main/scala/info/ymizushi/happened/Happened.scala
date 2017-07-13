package info.ymizushi.happened

import info.ymizushi.happened.domain.user.{UserRepositoryComponent, UserServiceComponent}
import info.ymizushi.happened.infra.UserRepositoryInfra
import info.ymizushi.happened.domain.user.UserRepository

import scala.concurrent.Future


object Happened {

  object ComponentRegistry extends UserServiceComponent with UserRepositoryComponent {
    val userRepository = new UserRepository with UserRepositoryInfra
    val userService = new UserService
  }

  def main(args: Array[String]): Unit = {
    val users = ComponentRegistry.userRepository.find()
    println(users.map(_.name))
  }

}


class Practive {
  case class User(name: String)
  case class Project(user: User)

  def getUser(name: String): Either[String, User] =
    Either.cond(name=="hoge", User(name), "Error")

  def getProject(user: User): Either[String, Project] =
    Either.cond(user.name=="hoge", Project(user), "Error")

  def test(): Unit = {

  }

  def heavyProcess(i: Int): Future[Int] = Future {
    Thread.sleep(1000)
    println(s"process: $i")
    i * 2
  }

  def fuga(): Unit = {
    (1 to 3).map(heavyProcess).toList
  }

  implicit def stringToInt(s: String) =
    s.toInt

}

