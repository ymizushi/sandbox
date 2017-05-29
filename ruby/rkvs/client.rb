class Mkvs 
    require "socket"

    def initialize 
        # gs = TCPServer.open(0)
        # addr = gs.addr
        # addr.shift
        # printf("server is on %s\n", addr.join(":"))
        # 
        # while true
        #   Thread.start(gs.accept) do |s|       # save to dynamic variable
        #     print(s, " is accepted\n")
        #     while s.gets
        #       s.write($_)
        #     end
        #     print(s, " is gone\n")
        #     s.close
        #   end
        # end
    end

end

class MkvsClient
    attr_accessor :url
    def connect url
        puts url
    end

    def initialize url="tcp://localhost:8090"
        @url = url
        @db = {}
        @session = connect url
    end

    def print
        puts @name
    end

    def get key
        @db[key]
    end

    def save key ,value
        @db[key] = value
    end
end

def post
    result = {:status => 200}
    yield result
end

if __FILE__ == $0
   client = MkvsClient.new
   client.save :hoge, "piyo"
   post do |result|
     p result
   end

  def method_proc
    proc = Proc.new { 
        return p "proc"
    }
    proc.call
    p "method_proc"
  end

  method_proc
  closure = lambda do |x| p x; return "hoge"; p "end" end
  closure.call(2)
end
