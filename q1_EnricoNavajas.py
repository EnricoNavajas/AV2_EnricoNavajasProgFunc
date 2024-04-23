contas_usuarios = lambda: {
    "enrico": 1000.00
}

senhas_usuarios = lambda: {
    "enrico": "123",
}

verificar_usuario_existe = lambda nome_usuario: nome_usuario in contas_usuarios()

verificar_senha_usuario = lambda nome_usuario, senha: senha == senhas_usuarios()[nome_usuario]

obter_valor_pagamento = lambda: float(input("Digite o valor do pagamento: "))

verificar_saldo_usuario = lambda nome_usuario, valor: contas_usuarios()[nome_usuario] >= valor

debitar_conta_usuario = lambda nome_usuario, valor: contas_usuarios().__setitem__(nome_usuario, contas_usuarios()[nome_usuario] - valor)

imprimir_recibo_pagamento = lambda nome_usuario, valor, saldo_final: print(f"\nRecibo de Pagamento:\nUsuário: {nome_usuario}\nValor: R$ {valor:.2f}\nSaldo Disponível: R$ {saldo_final:.2f}\n")

finalizar_transacao = lambda: print("\nTransação finalizada com sucesso!\n")

def processar_pagamento():
    nome_usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if not verificar_usuario_existe(nome_usuario):
        print("\nUsuário não encontrado!")
        return

    if not verificar_senha_usuario(nome_usuario, senha):
        print("\nSenha incorreta!")
        return

    valor_pagamento = obter_valor_pagamento()

    if not verificar_saldo_usuario(nome_usuario, valor_pagamento):
        print("\nSaldo insuficiente!")
        return

    saldo_inicial = contas_usuarios()[nome_usuario]
    debitar_conta_usuario(nome_usuario, valor_pagamento)
    saldo_final = saldo_inicial - valor_pagamento
    imprimir_recibo_pagamento(nome_usuario, valor_pagamento, saldo_final)
    finalizar_transacao()

processar_pagamento()
