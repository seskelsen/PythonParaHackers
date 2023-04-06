import dns.resolver

# alvo = 'google.com' #alvo a ser pesquisado
alvo = input("Digite o alvo: ")  # alvo a ser pesquisado

try:
    result = dns.resolver.resolve(alvo, "A")  # realiza a consulta DNS
    for ipval in result:
        print("IPV4: ", ipval.to_text())
        ip_alvo = ipval.to_text()
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

try:
    result = dns.resolver.resolve(alvo, "CNAME")
    for cnameval in result:
        print("CNAME: ", cnameval.target)
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

try:
    result = dns.resolver.resolve(alvo, "AAAA")
    for val in result:
        print("AAAA: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

try:
    result = dns.resolver.resolve(ip_alvo + ".in-addr.arpa", "PTR")
    for val in result:
        print("PTR: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

# NS
try:
    result = dns.resolver.resolve(alvo, "NS")
    for val in result:
        print("NS: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

# MX
try:
    result = dns.resolver.resolve(alvo, "MX")
    for val in result:
        print("MX: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

# SOA
try:
    result = dns.resolver.resolve(alvo, "SOA")
    for val in result:
        print("SOA: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

# TXT
try:
    result = dns.resolver.resolve(alvo, "TXT")
    for val in result:
        print("TXT: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")

# SRV
try:
    result = dns.resolver.resolve(alvo, "SRV")
    for val in result:
        print("SRV: ", val.to_text())
except:
    pass

# ------------------------------------------------------------------------------------------------
print("--------------------------------------------")
