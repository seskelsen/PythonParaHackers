import dns.resolver

dominio = input("Digite o dominio: ")
registros = ["A", "AAAA", "CNAME", "MX", "NS", "TXT"]

for registro in registros:
#    resultado = dns.resolver.query(dominio, registro, raise_on_no_answer=False)
    resultado = dns.resolver.resolve(dominio, registro, raise_on_no_answer=False)
    if resultado.rrset is not None:
#        print(registro + ": " + str(resultado.rrset))
        print(resultado.rrset)