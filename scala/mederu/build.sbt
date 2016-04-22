name := """mederu"""

version := "1.0-SNAPSHOT"

scalaVersion := "2.11.6"

lazy val root = (
  project in file(".")
  ).aggregate(
    application,
    domain,
    infrastructure
  ).enablePlugins(
    PlayScala
  )

lazy val application = Project(
  id = "application",
  base = file("application")
).dependsOn(
    domain,
    infrastructure
  ).enablePlugins(
    PlayScala
  )

lazy val domain = Project(id = "domain", base = file("domain")).settings(
    scalaSource in Compile := baseDirectory.value / "src" / "main" / "scala",
    scalaSource in Test := baseDirectory.value / "src" / "test" / "scala"
  )

lazy val infrastructure = Project(
  id = "infrastructure",
  base = file("infrastructure")
).dependsOn(domain).settings(
    scalaSource in Compile := baseDirectory.value / "src" / "main" / "scala",
    scalaSource in Test := baseDirectory.value / "src" / "test" / "scala"
  ).enablePlugins(
    PlayScala
  )


libraryDependencies ++= Seq(
  jdbc,
  cache,
  ws,
  evolutions,
  specs2 % Test
)

resolvers += "scalaz-bintray" at "http://dl.bintray.com/scalaz/releases"

routesGenerator := InjectedRoutesGenerator
