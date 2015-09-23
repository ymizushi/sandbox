package mederu.domain.admin

trait AdminUserRepository {
  def find(id: Long): AdminUser
}
