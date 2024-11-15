name := "functional-web-app"
version := "0.0.1-SNAPSHOT"

scalaVersion := "2.13.1"
libraryDependencies += "org.typelevel" %% "cats-core" % "2.0.0"

addCompilerPlugin("org.typelevel" %% "kind-projector" % "0.11.0" cross CrossVersion.full)
val circeVersion = "0.14.1"

libraryDependencies ++= Seq(
  "io.circe" %% "circe-core",
  "io.circe" %% "circe-generic",
  "io.circe" %% "circe-parser"
).map(_ % circeVersion)
