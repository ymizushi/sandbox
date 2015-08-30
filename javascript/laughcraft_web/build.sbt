name := "laughcraft_backend"

version := "0.0.1"

libraryDependencies ++= Seq(
  jdbc,
  anorm,
  cache
)     

play.Project.playScalaSettings
