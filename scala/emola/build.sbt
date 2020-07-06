lazy val root = (project in file(".")).
  settings(
    name := "Emola",
    version := "1.0",
    scalaVersion := "2.13.*"
  )

libraryDependencies ++= Seq("org.specs2" %% "specs2-core" % "3.6.1" % "test")

resolvers += "scalaz-bintray" at "http://dl.bintray.com/scalaz/releases"

scalacOptions in Test ++= Seq("-Yrangepos")

scalacOptions += "-Ypartial-unification"

libraryDependencies += "org.typelevel" %% "cats-core" % "2.1.1"
