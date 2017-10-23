from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    
with SimpleXMLRPCServer(("localhost", 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    
    def add( x, y ):
        return x + y
    server.register_function( add )

    def calc_IMC(nome, altura, peso):
        imc = peso / altura ** 2
        return("%s o seu imc é %.2f" % (nome, imc))
    server.register_function( calc_IMC )

    server.serve_forever()
