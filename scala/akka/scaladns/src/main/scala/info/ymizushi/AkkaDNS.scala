import java.net.InetSocketAddress

import akka.actor.{ActorSystem, Props, ActorLogging, Actor}
import akka.io.{IO, Tcp}

class Handler extends Actor with ActorLogging {
  import Tcp._

  def receive = {
    case Received(data) => {
      println(data)
      sender() ! Write(data)
    }
    case PeerClosed => context stop self
  }
}

/**
 * クライアントの接続を受け入れるサーバー
 */
class Server(bindAddress: InetSocketAddress) extends Actor with ActorLogging {
  import Tcp._
  import context.system

  IO(Tcp) ! Bind(self, bindAddress)

  def receive = {
    case Bound(localAddress) =>
      log.info("bound on {}...", localAddress)

    case Connected(remote, local) =>
      log.info("accepted peer: {}", remote)
      val handler = context.actorOf(Props[Handler])
      sender() ! Register(handler)

    case CommandFailed(_: Bind) =>
      log.error("bind failed")
      context stop self
  }
}

object AkkDNS {
  def main(args: Array[String]): Unit = {
    val system = ActorSystem("AkkaDNS")
    val bindAddress = new InetSocketAddress("localhost", 12345)
    system.actorOf(Props(classOf[Server], bindAddress))
  }
}
