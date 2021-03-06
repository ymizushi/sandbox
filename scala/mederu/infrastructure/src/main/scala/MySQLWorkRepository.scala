package mederu.infrastructure

import mederu.domain.WorkRepository
import mederu.domain.Work

object MySQLWorkRepository {
  def apply: MySQLWorkRepository = new MySQLWorkRepository
}

class MySQLWorkRepository extends WorkRepository {
  def find(id: Long): Seq[Work] = Seq(Work(1, "進撃の巨人"))
}
