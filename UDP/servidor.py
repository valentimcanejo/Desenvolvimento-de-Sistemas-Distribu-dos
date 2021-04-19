# Usar biblioteca socket do python
import socket

# Define o objeto do socket e a família. Basicamente irá especificar oque o programa irá usar da biblioteca socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# O bind irá associar o socket a minha porta e ao meu host
servidor.bind((socket.gethostname(), 50000))

# Irei citar as duas variáveis para serem usadas, o nome do primeiro e do segundo cliente, recebendo do servidor
nome = servidor.recvfrom(1000)
nomeb = servidor.recvfrom(1000)


while 1:

	# Variável criada para receber as mensagens dos cliente A e mostrar na tela
    r = servidor.recvfrom(1000)
    print(f"{nome}\n")
    print("%s"%(r[0]))
    
    # Variável criada para receber as mensagens dos cliente B e mostrar na tela
    j = servidor.recvfrom(1000)
    print(f"{nomeb}\n")
    print("%s"%(j[0]))