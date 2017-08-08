from multiprocessing.connection import Listener
import traceback

AUTHKEY = b'123456'

def handler(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            handler(client)
        except Exception:
            traceback.print_exc()

echo_server(('', 25000), authkey = AUTHKEY)
