require 'socket'

class Client
  def initialize(host, port)
    @socket = TCPSocket.open(host, port)
  end

  def send(message)
    @socket.puts(message)
  end

  def receive
    @socket.gets
  end

  def close
    @socket.close
  end
end

host = '172.18.18.95'
port = '8888'

client = Client.new('localhost', 8080)
client.send('Hello, world!')
puts client.receive
client.close