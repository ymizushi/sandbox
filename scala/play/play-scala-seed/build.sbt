name := """play-scala-seed"""
organization := "info.ymizushi"

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion := "2.12.2"

libraryDependencies += guice
libraryDependencies += "org.scalatestplus.play" %% "scalatestplus-play" % "3.1.0" % Test

libraryDependencies ++= Seq(
  "com.typesafe.slick" %% "slick" % "3.2.1",
  "org.slf4j" % "slf4j-nop" % "1.6.4",
  "com.typesafe.slick" %% "slick-hikaricp" % "3.2.1"
)

// Adds additional packages into Twirl
//TwirlKeys.templateImports += "info.ymizushi.controllers._"

// Adds additional packages into conf/routes
// play.sbt.routes.RoutesKeys.routesImport += "info.ymizushi.binders._"
