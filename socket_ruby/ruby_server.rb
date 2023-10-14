require 'socket'

class Server
  def initialize(port)
    @server = TCPServer.open(port)
  end

  def run
    loop do
      client = @server.accept
      puts "Client connected from #{client.peeraddr}"

      client.puts "Welcome to the server!"

      while line = client.gets
        puts "Client said: #{line}"
        client.puts "You said: #{line}"
      end

      client.close
    end
  end
end

server = Server.new(8888)
server.run