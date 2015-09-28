package mederu.infrastructure

import mederu.infrastructure.admin.MySQLAdminUserRepository

import mederu.domain.admin.AdminUserRepository
import mederu.domain.CharacterRepository
import mederu.domain.WorkRepository

import mederu.domain.UserRepository

object DIRegistry {
  lazy val adminUserRepository: AdminUserRepository = new MySQLAdminUserRepository
  lazy val userRepository: UserRepository = new MySQLUserRepository
  lazy val characterRepository: CharacterRepository = new MySQLCharacterRepository
  lazy val workRepository: WorkRepository = new MySQLWorkRepository
}

