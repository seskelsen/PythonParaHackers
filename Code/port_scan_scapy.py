#from scapy.all import *
import scapy.all as scapy

alvo = input("Digite o alvo: ")
#portas = [21, 22, 23, 25, 53, 80, 106, 110, 143, 443, 465, 993, 995, 8080]
portas = []
for porta in range(1000):
    portas.append(porta)

pacote_ip_alvo = scapy.IP(dst=alvo)
pacote_tcp = scapy.TCP(dport=portas, flags="S")
pacote = pacote_ip_alvo/pacote_tcp
ans, uans = scapy.sr(pacote, inter=0.1, timeout=1)
print("Porta\tEstado")
for pacote_recebido in ans:
    print(pacote_recebido[1][scapy.IP].sport, \
          "\t", pacote_recebido[1][scapy.TCP].sprintf("%flags%"))
