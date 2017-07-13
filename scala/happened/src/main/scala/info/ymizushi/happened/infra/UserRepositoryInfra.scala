package info.ymizushi.happened.infra

import info.ymizushi.happened.domain.user.UserRepository
import info.ymizushi.happened.domain.user.User

trait UserRepositoryInfra extends UserRepository {
  override def find(): List[User] = {
    List(User("hoge"))
  }
}

