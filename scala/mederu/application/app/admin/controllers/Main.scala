package mederu.application.admin.controllers

import play.api.mvc._

import mederu.infra.admin.AdminUserRegistry


object Main extends Controller {
  def index = Action {
    val adminUserRepo = AdminUserRegistry.adminuserRepository
    val adminUser = adminUserRepo.find(10)
    Ok(views.html.index(adminUser.name))
  }
}
