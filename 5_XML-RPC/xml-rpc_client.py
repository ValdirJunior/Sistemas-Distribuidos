import xmlrpc.client
client = xmlrpc.client.ServerProxy('http://localhost:8000')
client.system.listMethods()
print(client.add( 3, 7 ))
print(client.calc_IMC('Fernanda', 1.55, 42))
