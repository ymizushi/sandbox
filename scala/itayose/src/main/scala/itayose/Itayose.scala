package itayose

case class Board (val orders: List[Order]) {
  def addOrder(order: Order): Board  = {
    Board(order :: orders) 
  }

  def itayose: Board =  {
    this
  }

  def groupByPrice: 
}

object BoardTable {
  def apply: BoardTable = {
    new BoardTable(HashMap)
  }
}

class BoardTable(private val table: Map) {

}

case class Order private (val tradingType: TradingType, val price: Price, val numberOfStock: NumberOfStock)

sealed trait Price 
case object Nariyuki extends Price 
sealed case class NumberOfPrice(num: Int) extends Price 
case class NumberOfStock(private val num: Int)

sealed trait TradingType
case object Buying extends TradingType
case object Selling extends TradingType 

object Itayose extends App {
  val board = Board(List.empty)
  board
    .addOrder(Order(Selling, Nariyuki, NumberOfStock(10)))
    .addOrder(Order(Buying, NumberOfPrice(100), NumberOfStock(10)))
    .addOrder(Order(Buying, NumberOfPrice(100), NumberOfStock(10)))
    .addOrder(Order(Selling, NumberOfPrice(100), NumberOfStock(10)))
  board.itayose
}
