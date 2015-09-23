package mederu.infra.admin


import mederu.domain.admin.AdminUser
import mederu.domain.admin.AdminUserRepository

class MySQLAdminUserRepository extends AdminUserRepository {
  def find(id: Long): AdminUser = AdminUser(id, "hoge")
}
