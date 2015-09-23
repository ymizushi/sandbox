package mederu.domain.admin

trait AdminRole

object AdminRole {
  object Administrator extends AdminRole
  object Editor extends AdminRole
  object Viewer extends AdminRole
}

