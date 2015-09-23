name := """mederu"""

version := "1.0-SNAPSHOT"

//lazy val root = (project in file(".")).enablePlugins(PlayScala)


// このプロジェクトはapplication、domain、infrastructureの集合である
lazy val root = (
  project in file(".")
  ).aggregate(
    application,
    domain,
    infrastructure
  )

// アプリケーション層
// アプリケーション層はドメイン層・インフラ層に依存し、Playアプリケーションである
lazy val application = Project(
  id = "application",
  base = file("application")
).dependsOn(
    domain,
    infrastructure
  ).enablePlugins(
    PlayScala
  )

// ドメイン層
// ドメイン層はインフラ層に依存
lazy val domain = Project(
  id = "domain",
  base = file("domain")
).dependsOn(
    infrastructure
  ).settings(
    scalaSource in Compile := baseDirectory.value / "src" / "main" / "scala",
    scalaSource in Test := baseDirectory.value / "src" / "test" / "scala"
  )

// インフラ層
lazy val infrastructure = Project(
  id = "infrastructure",
  base = file("infrastructure")
).settings(
    scalaSource in Compile := baseDirectory.value / "src" / "main" / "scala",
    scalaSource in Test := baseDirectory.value / "src" / "test" / "scala"
  )

scalaVersion := "2.11.6"

libraryDependencies ++= Seq(
  jdbc,
  cache,
  ws,
  specs2 % Test
)

resolvers += "scalaz-bintray" at "http://dl.bintray.com/scalaz/releases"

// Play provides two styles of routers, one expects its actions to be injected, the
// other, legacy style, accesses its actions statically.
routesGenerator := InjectedRoutesGenerator
