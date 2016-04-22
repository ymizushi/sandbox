package mederu.application.controllers.works.characters

import play.api.mvc._

object ListCharacters extends Controller {
  def index(workId: Long) = Action {
    Ok(views.html.list_characters("/works/<作品名>/charactersページです"))
  }
}
