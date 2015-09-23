package mederu.infra.admin


import mederu.domain.admin.AdminUser
import mederu.domain.admin.AdminUserRepository
import mederu.domain.admin.AdminRole

class MySQLAdminUserRepository extends AdminUserRepository {
  def find(id: Long): AdminUser = AdminUser(id, "piyo", AdminRole.Administrator)
}
