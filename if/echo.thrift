namespace py echoserver

struct EchoMessage {
  1: string message
}

struct EchoResponse {
  1: string response
}

service EchoServer {
  /* 
   * ping()
   *
   * just to make sure the server receives a connection and logs or something
   */
  void ping()

  /*
   * echo(EchoMessage message)
   *
   * Returns an EchoResponse
   */
  EchoResponse echo(1: EchoMessage message)
}
