from echoserver.echoserver import EchoServer, ttypes

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging
logger = logging.getLogger('EchoServerLogger')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

class EchoServerHandler(object):
    def __init__(self):
        self.log = logger

    def ping(self):
        self.log.info('pong!')

    def echo(self, echomessage):
        response = ttypes.EchoResponse(echomessage.message)
        self.log.info('Received %s : returning %s' % (echomessage, response))
        return response

    def add(self, numbers):
        _sum = numbers.firstNumber + numbers.secondNumber
        response = ttypes.NumberSum(_sum)
        self.log.info('Received %s : returning %s' % (numbers, response))
        return response

if __name__ == '__main__':
    handler = EchoServerHandler()
    processor = EchoServer.Processor(handler)
    transport = TSocket.TServerSocket(None, 23456)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(
        processor, transport, tfactory, pfactory)

    logger.warn('Starting server...')
    server.serve()
    logger.warn('Done!')
