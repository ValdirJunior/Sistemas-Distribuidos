import socket
import threading

host = '127.0.0.1'
port = 3031

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = ((host,port))
server.bind(orig)
server.listen(1)

def connection(con, client):
    print (str(client), ' conectado')
    msg = 'Conectado!'
    con.send(msg.encode('ascii'));

    while True:
        try:
            msg = con.recv(1024)
            if msg:
                print(str(client), msg.decode('ascii'))
            else:
                raise error(str(client), ' desconectado')
        except:
            print (str(client), ' conexao finalizada')
            con.close()
            return False

while True:
    con, client = server.accept()
    threading.Thread(target = connection,args = (con,client)).start()

server.close()
