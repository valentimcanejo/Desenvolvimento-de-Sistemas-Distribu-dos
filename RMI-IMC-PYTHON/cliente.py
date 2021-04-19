#importando biclioteca usada na conexao remota
import Pyro4

#definido o conexao local
nameServer = Pyro4.locateNS()
uri = nameServer.lookup('obj')
server = Pyro4.Proxy(uri)

#solicitar dados ao Usuario!
while (True):
    nome = input("Digite seu nome: ")
    print('\nDigite os numeros usando ponto no formato Flutuante (1.1)!\n')

    numero1 = float(input("Qual e seu peso? (kg): "))
    numero2 = float(input("Qual e sua altura? (m): "))
    print("\n")

    print("########################################")

    print('Seu nome é : ',nome)
    print("Seu IMC é de  ({:.1f})".format(server.imc(numero1,numero2)))
    ##condicao
    pessoa = (server.imc(numero1, numero2))

    if pessoa < 16:
        print("Magreza grave\n")
    elif pessoa < 17:
        print("Magreza moderada\n")
    elif pessoa < 18.5:
        print("Magreza leve\n")
    elif pessoa < 25:
        print("Saudavel\n")
    elif pessoa < 30:
        print("Sobrepeso\n")
    elif pessoa < 35:
        print("Obesidade Grau I\n")
    elif pessoa < 40:
        print("Obesidade Grau II (severa)\n")
    else:
        print("Obesidade Grau III (morbida)\n")
