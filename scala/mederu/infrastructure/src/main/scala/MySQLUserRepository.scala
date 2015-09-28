package mederu.infrastructure

import mederu.domain.UserRepository
import mederu.domain.User

object MySQLUserRepository {
  def apply: MySQLUserRepository = new MySQLUserRepository
}

class MySQLUserRepository extends UserRepository {
  def find(id: Long): Seq[User] = Seq(User(1, "yuta_mizushima", "yuta_mizushim.png"))
}
