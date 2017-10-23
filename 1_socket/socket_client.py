import socket

host = '127.0.0.1'
port = 3031
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, port)
tcp.connect(dest)

servermsg = tcp.recv(1024)
print(servermsg.decode('ascii'))

print ('CTRL+x -> SAIR\n')
msg = input()

while msg != '\x18':
    tcp.send(msg.encode('ascii'))
    msg = input()
tcp.close()
