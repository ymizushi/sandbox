package mederu.infrastructure

import mederu.infrastructure.admin.MySQLAdminUserRepository

object DIRegistry {
  lazy val AdminUserRepository = MySQLAdminUserRepository
  lazy val UserRepository = MySQLUserRepository
  lazy val CharacterRepository = MySQLCharacterRepository
  lazy val workRepository = MySQLWorkRepository
}

