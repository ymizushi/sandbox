package mederu.infra.admin

import mederu.domain.admin.AdminUserRepository

object AdminUserRegistry {
  lazy val adminuserRepository: AdminUserRepository = new MySQLAdminUserRepository
}
