package mederu.infrastructure.admin

import mederu.domain.admin.AdminUser
import mederu.domain.admin.AdminUserRepository
import mederu.domain.admin.AdminRole


object MySQLAdminUserRepository {
  def apply: MySQLAdminUserRepository = new MySQLAdminUserRepository
}

class MySQLAdminUserRepository extends AdminUserRepository {
  def find(id: Long): AdminUser = AdminUser(id, "piyo", AdminRole.Administrator)
}
