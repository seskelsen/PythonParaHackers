import socket

dominio = input("Digite o dominio: ")
brute = [
    "ns1",
    "ns2",
    "ns3",
    "ns4",
    "www",
    "ftp",
    "intranet",
    "mail",
    "smtp",
    "pop",
    "pop3",
    "imap",
    "webmail",
]

for nome in brute:
    DNS = nome + "." + dominio
    try:
        print(DNS + ": " + socket.gethostbyname(nome + "." + dominio))
    except socket.gaierror:
        pass
