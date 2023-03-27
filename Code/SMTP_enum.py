import socket

usuarios = ["contato", "admin", "root", "webmaster", "suporte", "info", 
            "administrador", "administracao", "administrativo", "suporte", 
            "webmaster", "comercial", "financeiro", "contabilidade", "rh", 
            "marketing", "vendas", "compras", "diretoria", "gerencia", "geral", 
            "gerente", "diretor", "diretora", "preside"]

alvo = input("Digite o alvo: ")

for usuario in usuarios:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria o socket
    try:
        sock.connect((alvo, 25))
        sock.recv(1024)  # Recebe a resposta do servidor
        sock.send("VRFY " + usuario + "\n")
        smtp_resultado = sock.recv(1024)  # Recebe a resposta do servidor
        sock.close()
        if "252" in smtp_resultado:
            print("Usuario encontrado: " + usuario)
        elif "550" in smtp_resultado:
            print("Usuario nao encontrado: " + usuario)
        elif "503" in smtp_resultado:
            print("Servidor requer autenticação")
            break
        elif "500" in smtp_resultado:
            print("Comando não reconhecido pelo servidor")
            break
        else:
            print("Resposta do servidor: " + smtp_resultado)
            break
    except:
        print("Erro ao conectar ao servidor SMTP")
        break
