# Usar biblioteca socket do python
import socket

# Define o objeto do socket e a família. Basicamente irá especificar oque o programa irá usar da biblioteca
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# O bind irá associar o socket a minha porta e ao meu host
servidor.bind((socket.gethostname(), 50000))
# O listen irá dizer a biblioteca que queremos enfileirar no máximo 10 requisições de conexão
servidor.listen(10)


# Faço o servidor aceitar as conexões dois endereços, no caso dois usuários de um chat	
conexao, endereco = servidor.accept()
conexaob, enderecob = servidor.accept()
# O programa irá printar os endereços de cada usuário
print(f"Endereço {endereco} aceito")
print(f"Endereço {enderecob} aceito")

while 1:

# Mensagem enviada pelo cliente A, com tamanho de 1000
    mensagem = conexao.recv(1000)
    print(f"{endereco}\n")
    print(mensagem.decode())
# Mensagem enviada pelo cliente B, com tamanho de 1000
    mensagemb = conexaob.recv(1000)
    print(f"{enderecob}\n")
    print(mensagemb.decode())
