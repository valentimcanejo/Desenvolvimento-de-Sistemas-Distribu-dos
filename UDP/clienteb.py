# Usar biblioteca socket do python
import socket

# Define o objeto do socket e a família. Basicamente irá especificar oque o programa irá usar da biblioteca
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Faz a conexão entre o servidor e o endereco do cliente
servidor.connect((socket.gethostname(), 50000))


mensagemb = ''
nomeb = ''

nomeb = input("Digite seu apelido: ")
servidor.send(nomeb.encode())

# Estrutura de repetição do chat
while (mensagemb != 'sair'):
	
# Input do cliente para se comunicar
	mensagemb = input("chat: ")
# Manda a mensagem para o servidor
	servidor.send(mensagemb.encode())
	
