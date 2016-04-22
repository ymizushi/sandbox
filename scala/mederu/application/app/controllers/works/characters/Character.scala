package mederu.application.controllers.works.characters

import play.api.mvc._

object Character extends Controller {
  def index(workId: Long, characterId: Long) = Action { implicit request =>
    Ok(views.html.character("/works/<作品名>/characters/<キャラクター名>ページです"))
  }
}
