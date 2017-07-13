object Main {
  def main(args: Array[String]): Unit = {
    println(sum(10))
  }

  def sum(n: Int): Int =  {
    if (n == 1) 
      1
    else
      n + sum(n-1)
  }

}

