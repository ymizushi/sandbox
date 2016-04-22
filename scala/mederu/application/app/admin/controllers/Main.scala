package mederu.application.admin.controllers

import play.api.mvc._

import mederu.infrastructure.DIRegistry

object Main extends Controller {
  def index = Action {
    val adminUserRepo = DIRegistry.AdminUserRepository()
    val adminUser = adminUserRepo.find(10)
    Ok(views.html.admin_index(adminUser.name))
  }
}
