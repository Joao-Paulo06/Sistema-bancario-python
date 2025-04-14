class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.extrato = ""
        self.numero_saques = 0
        self.limite_saques = 3
        self.limite = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print(
            "Não foram realizadas movimentações." if not self.extrato else self.extrato
        )
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


class SistemaBancario:
    def __init__(self):
        self.contas = []

    def criar_conta(self, titular, saldo_inicial=0):
        nova_conta = ContaBancaria(titular, saldo_inicial)
        self.contas.append(nova_conta)
        print("Conta criada com sucesso!")

    def listar_contas(self):
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        print("\n======== Contas Cadastradas ========")
        for i, conta in enumerate(self.contas):
            print(f"{i+1}. Titular: {conta.titular}, Saldo: R$ {conta.saldo:.2f}")
        print("====================================")

    def selecionar_conta(self, titular):
        for conta in self.contas:
            if conta.titular.lower() == titular.lower():
                return conta
        print("Conta não encontrada.")
        return None


sistema = SistemaBancario()


sistema.criar_conta("João", 100)
sistema.criar_conta("Maria", 500)

while True:
    print("\n======== Menu Principal ========")
    print("[c] Criar nova conta")
    print("[l] Listar contas")
    print("[a] Acessar conta existente")
    print("[q] Sair")
    opcao_principal = input("=> ").lower()

    if opcao_principal == "c":
        titular = input("Informe o nome do titular: ")
        saldo_inicial = float(input("Informe o saldo inicial: "))
        sistema.criar_conta(titular, saldo_inicial)

    elif opcao_principal == "l":
        sistema.listar_contas()

    elif opcao_principal == "a":
        nome_titular = input("Informe o nome do titular da conta que deseja acessar: ")
        conta_atual = sistema.selecionar_conta(nome_titular)

        if conta_atual:
            menu_conta = """

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [v] Voltar ao menu principal
            [q] Sair

            => """

            while True:
                opcao_conta = input(menu_conta).lower()

                if opcao_conta == "d":
                    valor = float(input("Informe o valor do depósito: "))
                    conta_atual.depositar(valor)

                elif opcao_conta == "s":
                    valor = float(input("Informe o valor do saque: "))
                    conta_atual.sacar(valor)

                elif opcao_conta == "e":
                    conta_atual.exibir_extrato()

                elif opcao_conta == "v":
                    break

                elif opcao_conta == "q":
                    print("Saindo do sistema.")
                    exit()

                else:
                    print(
                        "Operação inválida, por favor selecione novamente a operação desejada."
                    )

    elif opcao_principal == "q":
        print("Saindo do sistema.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
