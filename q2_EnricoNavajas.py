import unittest
import threading

contas_usuarios = lambda: {"enrico": 1000.00}

senhas_usuarios = lambda: {"enrico": "123"}

verificar_usuario_existe = lambda nome_usuario: nome_usuario in contas_usuarios()

verificar_senha_usuario = lambda nome_usuario, senha: senha == senhas_usuarios().get(nome_usuario, None)

obter_valor_pagamento = lambda: float(input("Digite o valor do pagamento: "))

verificar_saldo_usuario = lambda nome_usuario, valor: contas_usuarios().get(nome_usuario, 0) >= valor

debitar_conta_usuario = lambda nome_usuario, valor: contas_usuarios().__setitem__(nome_usuario, contas_usuarios()[nome_usuario] - valor)

imprimir_recibo_pagamento = lambda nome_usuario, valor, saldo_final: print(f"\nRecibo de Pagamento:\nUsuário: {nome_usuario}\nValor: R$ {valor:.2f}\nSaldo Disponível: R$ {saldo_final:.2f}\n")

finalizar_transacao = lambda: print("\nTransação finalizada com sucesso!\n")

def processar_pagamento(nome_usuario, senha, valor_pagamento):
    if not verificar_usuario_existe(nome_usuario):
        print("\nUsuário não encontrado!")
        return

    if not verificar_senha_usuario(nome_usuario, senha):
        print("\nSenha incorreta!")
        return

    if not verificar_saldo_usuario(nome_usuario, valor_pagamento):
        print("\nSaldo insuficiente!")
        return

    saldo_inicial = contas_usuarios().get(nome_usuario, 0)
    debitar_conta_usuario(nome_usuario, valor_pagamento)
    saldo_final = saldo_inicial - valor_pagamento
    imprimir_recibo_pagamento(nome_usuario, valor_pagamento, saldo_final)
    finalizar_transacao()

class TestPagamento(unittest.TestCase):

    def test_usuario_inexistente(self):
        nome_usuario = "usuario_invalido"
        senha = "senha_incorreta"
        self.assertFalse(verificar_usuario_existe(nome_usuario))
        self.assertFalse(verificar_senha_usuario(nome_usuario, senha))

    def test_saldo_insuficiente(self):
        nome_usuario = "enrico"
        senha = "123"
        valor_pagamento = 1500.00
        self.assertTrue(verificar_usuario_existe(nome_usuario))
        self.assertTrue(verificar_senha_usuario(nome_usuario, senha))
        self.assertFalse(verificar_saldo_usuario(nome_usuario, valor_pagamento))

    def test_pagamento_sucesso(self):
        nome_usuario = "enrico"
        senha = "123"
        valor_pagamento = 500.00
        self.assertTrue(verificar_usuario_existe(nome_usuario))
        self.assertTrue(verificar_senha_usuario(nome_usuario, senha))
        self.assertTrue(verificar_saldo_usuario(nome_usuario, valor_pagamento))

    def test_stress_test(self):
        def realizar_transacao():
            processar_pagamento("enrico", "123", 100.00)

        threads = []
        num_threads = 1000

        for _ in range(num_threads):
            thread = threading.Thread(target=realizar_transacao)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    unittest.main()
