#importando a biblioteca 
#Usada para  estabelecer conexao remota via rede
import Pyro4

@Pyro4.expose
class CalculaImc:
    def imc(self, peso, altura):
        resultadoImc = (peso / altura**2)
        print("\nO seu IMC ({:.1f}) \n".format(resultadoImc))
        return resultadoImc

daemon = Pyro4.Daemon()

print("Aguardando conexao...")
#(uri) e tipo uma url
uri = daemon.register(CalculaImc)

nameServer = Pyro4.locateNS()
nameServer.register('obj', uri)

daemon.requestLoop()