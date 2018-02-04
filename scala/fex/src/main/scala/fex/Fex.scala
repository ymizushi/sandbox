package info.ymizushi.fex

import scalafx.Includes._
import scalafx.application.JFXApp
import scalafx.application.JFXApp.PrimaryStage
import scalafx.event.ActionEvent
import scalafx.scene.Scene
import scalafx.scene.control.{Label, Menu, MenuBar, MenuItem, SeparatorMenuItem}
import scalafx.scene.layout.{BorderPane, VBox}
import scalafx.scene.paint.Color
import collection.JavaConversions._

import org.jutils.jprocesses.JProcesses

object Fex extends JFXApp {

  val menu = new Menu("File") {
    items = List(
      new MenuItem("Open") {
        onAction = (ae: ActionEvent) => history.children += new Label("Selected item `Open`")
      },
      new SeparatorMenuItem,
      new MenuItem("Close") {
        onAction = (ae: ActionEvent) => history.children += new Label("Selected item `Close`")
      }
    )

    onShowing = handle {
     printEvent("on showing")
     printProcessList
    }
    onShown = handle {printEvent("on shown")}
    onHiding = handle {printEvent("on hiding")}
    onHidden = handle {printEvent("on hidden")}
  }

  val history = new VBox()

  val menuBar = new MenuBar {
    useSystemMenuBar = true
    minWidth = 100
    menus.add(menu)
  }

  stage = new PrimaryStage {
    title = "Fex"
    width = 300
    height = 225
    scene = new Scene {
      fill = Color.LightGray
      root = new BorderPane {
        top = menuBar
        bottom = history
      }
    }
  }

  def printEvent(eventStr: String)() {
    history.children += new Label(eventStr)
  }

  def printProcessList(): Unit = {
    val l = JProcesses.getProcessList()
    l.map { processInfo =>
      println("Process Name: " + processInfo.getName())
    }
  }
}
