package mederu.application.controllers.works

import play.api.mvc._

object ListWorks extends Controller {
  def index = Action {
    Ok(views.html.list_works("/works ページです"))
  }
}
