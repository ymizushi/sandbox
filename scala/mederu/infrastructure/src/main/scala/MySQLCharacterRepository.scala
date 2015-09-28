package mederu.infrastructure

import mederu.domain.CharacterRepository
import mederu.domain.Character
import mederu.domain.Work

class MySQLCharacterRepository extends CharacterRepository {
  def find(id: Long): Seq[Character] = Seq(Character(1, "エレン", Seq(Work(1, "進撃の巨人"))))
}

