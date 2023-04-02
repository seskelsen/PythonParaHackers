from scapy.all import *
import sys

alvo = input("Digite o alvo: ")
portas = [21, 22, 23, 25, 53, 80, 106, 110, 143, 443, 465, 993, 995, 8080]
pacote_ip_alvo = IP(dst=alvo)
pacote_tcp = TCP(dport=portas, flags="S")
pacote = pacote_ip_alvo/pacote_tcp
ans, uans = sr(pacote, inter=0.1, timeout=1)
print("Porta\tEstado")
for pacote_recebido in ans:
    print(pacote_recebido[1][IP].sport, \
          "\t", pacote_recebido[1][TCP].sprintf("%flags%"))
