from SOAPpy import SOAPProxy
client = SOAPProxy('http://localhost/6_soap/server.php', 'http://localhost/6_soap/')
print client.getMessage('Valdir')
client.idade(21)
client.getIMCMessage()
print client.getIMC(75, 1.81)
