import socket

host = input("Digite o alvo: ")
portas = [21, 22, 23, 25, 53, 80, 110, 143, 443, 587, 993, 995, 3306, 8080, 465, 8443, 106, 465]
#for porta in portas:
for porta in range(1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    sock.settimeout(1)  # Define o timeout
    resultado = sock.connect_ex((host, porta))  # Conecta ao alvo
    sock.close()
    if resultado == 0:
        print("Porta aberta: " + str(porta))