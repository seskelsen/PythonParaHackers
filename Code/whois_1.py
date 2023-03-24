import whois

#todo 1. obter o dominio na linha de comando
dominio = input('Digite o dominio: ')
consulta_whois = whois.whois(dominio)

#print(domain.fone)
print(consulta_whois.text)

