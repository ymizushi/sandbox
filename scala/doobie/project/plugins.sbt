addSbtPlugin("org.scalameta" % "sbt-scalafmt" % "2.0.0")

addCompilerPlugin(
  "org.scalamacros" % "paradise" % "2.1.1" cross CrossVersion.full
)