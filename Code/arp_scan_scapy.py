#68:2f:67:91:74:29
#192.168.5.171

import scapy.all as scapy

IPS = []
for ip in range(170, 180):
    IPS.append("192.168.5." + str(ip))
    print(ip)
pacote_arp = scapy.Ether()/scapy.ARP(pdst=IPS, hwdst="68:2f:67:91:74:29")
ans, uans = scapy.sr(pacote_arp, inter=0.1, timeout=1)
print("IP\t\tMAC")
for pacote_recebido in ans:
    print(pacote_recebido[1].psrc, "\t", pacote_recebido[1].hwsrc)