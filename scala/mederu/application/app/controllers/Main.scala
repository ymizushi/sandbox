package mederu.application.controllers

import play.api.mvc._

import mederu.application.component.Common

object Main extends Controller {
  def index = Action {
    Ok(views.html.index(Common))
  }
}
