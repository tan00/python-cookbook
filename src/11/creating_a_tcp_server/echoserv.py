from socketserver import BaseRequestHandler, TCPServer
import functools

BLOCKSIZE = 2
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:            
            msg = self.request.recv(BLOCKSIZE)
            if not msg:
                break
            
            self.request.send(msg)

   
class EchoHandler2(BaseRequestHandler):
    def handle(self):
        size = BLOCKSIZE
        func_recv = functools.partial( self.request.recv, size)
        print('Got connection from', self.client_address)
        for msg in iter( func_recv , b''):            
            self.request.send(msg)       

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler2)
    print('Echo server running on port 20000')
    serv.serve_forever()
