lazy val root = (project in file("."))
  .settings(
  name := "Hello",
  scalaVersion := "2.12.3",
  libraryDependencies += "org.scalafx" %% "scalafx" % "8.0.144-R12"
)

