# vim: set tabstop=4 shiftwidth=4 softtabstop=4

from echoserver.echoserver import EchoServer, ttypes
import sys

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def connect():
    try:
        socket = TSocket.TSocket('localhost', 23456)
        transport = TTransport.TBufferedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = EchoServer.Client(protocol)
        if client:
            transport.open()
            return client
        raise Exception('Client did not create!')
    except Thrift.TException as tx:
        print("OHNO!! %s" % tx.message)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception('You need to give me two numbers as arguments!')

    client = connect()
    client.echo(ttypes.EchoMessage('Hello World!!'))

    numbers = ttypes.NumbersToAdd(firstNumber=int(sys.argv[1]), secondNumber=int(sys.argv[2]))
    number_sum = client.add(numbers)
    print(number_sum)

