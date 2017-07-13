package info.ymizushi.happened.domain.user

case class Error(name: String)

trait UserServiceComponent {
  this: UserRepositoryComponent =>
  val userService: UserService

  class UserService {
    def find(): List[User] = {
      userRepository.find()
    }
  }
}
