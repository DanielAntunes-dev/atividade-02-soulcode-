def criar_saudacao(saudacao):
    def saudacao_com_nome(nome):
        return f"{saudacao}, {nome}!"
    return saudacao_com_nome

saudar = criar_saudacao("Olá")
print(saudar("Daniel")) 

