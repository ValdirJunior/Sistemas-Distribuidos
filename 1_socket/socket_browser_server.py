import socket

#host = socket.gethostname()
host = '127.0.0.1'
port = 3032

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = ((host,port))
server.bind(orig)
server.listen(1)


while True:
    con, client = server.accept()
    con.recv(1024)
    con.send(str('HTTP/1.0 200 OK\n').encode('ascii'))
    con.send(str('Content-Type: text/html\n').encode('ascii'))
    con.send(str('\n').encode('ascii'))
    con.send(str("""
        <html>
        <body>
        <h1>Hello World!</h1>
        <p>Univem 2017</p>
        </body>
        </html>
    """).encode('ascii'))
    con.close()

server.close()
