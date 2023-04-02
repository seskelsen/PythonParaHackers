import socket

#alvo = input("Digite o IP ou Host: ")
alvo = "scanme.nmap.org" #nmapp.org também funciona
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.settimeout(2)
print("Verificando o alvo: " + alvo)
sock.connect_ex((alvo, 22)) # Porta SSH
print("Porta SSH aberta")
print(sock.recv(2048))
sock.close()
