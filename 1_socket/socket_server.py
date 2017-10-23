import socket

host = '127.0.0.1'
port = 3031
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = ((host,port))
server.bind(orig)
server.listen(1)

while True:
    con, client = server.accept()

    print (str(client), ' conectado')
    msg = 'Conectado!'
    con.send(msg.encode('ascii'));

    while True:
        msg = con.recv(1024)
        if not msg: break
        print (client, msg.decode('ascii'))
    print (str(client), ' conexao finalizada')

    con.close()
