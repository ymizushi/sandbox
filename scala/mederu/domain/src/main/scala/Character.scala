package mederu.domain

case class Character(id: Long, name: String, work: Seq[Work])

trait CharacterRepository {
  def find(id: Long): Seq[Character]
}
