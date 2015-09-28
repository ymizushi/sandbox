package mederu.domain

case class User(id: Long, name: String, imageUrl: String)

trait UserRepository {
  def find(id: Long): Seq[User]
}

