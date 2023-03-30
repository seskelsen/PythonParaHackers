import socket

alvo = input("Digite o IP ou Host: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.settimeout(2)
sock.connect_ex((alvo, 22)) # Porta SSH
print("Porta SSH aberta")
print(sock.recv(2048))
sock.close()
