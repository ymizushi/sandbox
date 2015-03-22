package message {
  class Message(val content: String)
  
  class MyMessageQue {
    var que = List("start")
  
    def push(message: Message) {
      println(message.content)
    }
  }
}

import message.Message
import message.MyMessageQue

object MessageQue {
  def main(args: Array[String]) {
    val messageQue = new MyMessageQue()
    messageQue.push(new Message("hoge"))
    println("piyo")
  }
}
