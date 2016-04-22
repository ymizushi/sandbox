package mederu.application.controllers.works

import play.api.mvc._

import mederu.infrastructure.DIRegistry
import mederu.domain.WorkRepository

object Work extends Controller {
  def index(workId: Long) = Action {
    val workRepo: WorkRepository = DIRegistry.WorkRepository.apply
    Ok(views.html.admin_index("/works/<" + workRepo.find(workId).head + ">ページです"))
  }
}
