import socket
dominio = input("Digite o dominio: ")
with open("code/bruteforcedns.txt", "r") as arquivo:
    bruteforce = arquivo.readlines()

for nome in bruteforce:
    DNS = nome.strip("\n") + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass