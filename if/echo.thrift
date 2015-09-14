namespace py echoserver

struct EchoMessage {
  1: string message
}

struct EchoResponse {
  1: string response
}

struct NumbersToAdd {
  1: i64 firstNumber,
  2: i64 secondNumber
}

struct NumberSum {
  1: i64 sum
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

  /*
   * add(NumbersTooAdd numbers)
   *
   * Returns an EchoResponse
   */
  NumberSum add(1: NumbersToAdd numbers)
}
