package info.ymizushi.happened.domain.user

case class User(name: String)

trait UserRepository {
  def find(): List[User]
}

trait UserRepositoryComponent {
  val userRepository: UserRepository
}
