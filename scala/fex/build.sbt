lazy val root = (project in file("."))
  .settings(
    name := "Fex",
    scalaVersion := "2.12.4",
    resolvers += "maven-central" at "http://central.maven.org/maven2",
    libraryDependencies ++= Seq(
      "org.scalafx" %% "scalafx" % "8.0.144-R12",
      "org.jprocesses" % "jProcesses" % "1.6.4"
    )
)
