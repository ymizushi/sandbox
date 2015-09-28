package mederu.domain

case class Work(id: Long, name: String)

trait WorkRepository {
  def find(id: Long): Seq[Work]
}
