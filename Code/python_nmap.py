# -*- coding: utf-8 -*-
import nmap

nmap_scan = nmap.PortScanner()
#nmap_scan.scan ("8.8.8.8", "21-80")  #google
nmap_scan.scan ("44.228.249.3", "1-1000")  #vulnweb.com

for host in nmap_scan.all_hosts():
    print ("Host : %s (%s)" % (host, nmap_scan[host].hostname()))
    print ("State : %s" % nmap_scan[host].state())
    for proto in nmap_scan[host].all_protocols():
        print ("----------")
        print ("Protocol : %s" % proto)

        lport = nmap_scan[host][proto].keys()

        for port in lport:
            print ("port : %s\tstate : %s" % (port, nmap_scan[host][proto][port]['state']))
