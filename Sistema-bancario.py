class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, agencia, numero_conta, titular):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        print("Método sacar na classe base ContaBancaria não implementado.")
        return False

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimentacao in self.extrato:
                print(movimentacao)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class ContaCorrente(ContaBancaria):
    def __init__(self, agencia, numero_conta, titular, limite=500, limite_saques=3):
        super().__init__(agencia, numero_conta, titular)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

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
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print("Saque realizado com sucesso.")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

class SistemaBancario:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.AGENCIA = "0001"
        self.numero_conta_atual = 1

    def criar_cliente(self, nome, cpf, data_nascimento, endereco):
        if any(cliente.cpf == cpf for cliente in self.clientes):
            print("Erro: CPF já cadastrado.")
            return None
        novo_cliente = Cliente(nome, cpf, data_nascimento, endereco)
        self.clientes.append(novo_cliente)
        print("Cliente criado com sucesso!")
        return novo_cliente

    def buscar_cliente(self, cpf):
        return next((cliente for cliente in self.clientes if cliente.cpf == cpf), None)

    def criar_conta(self, titular):
        if titular not in self.clientes:
            print("Erro: Titular não encontrado.")
            return None
        nova_conta = ContaCorrente(self.AGENCIA, self.numero_conta_atual, titular)
        self.contas.append(nova_conta)
        print(f"Conta corrente criada com sucesso! Agência: {nova_conta.agencia}, Número da Conta: {nova_conta.numero_conta}")
        self.numero_conta_atual += 1
        return nova_conta

    def listar_contas(self):
        print("\n======== Contas Cadastradas ========")
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        for conta in self.contas:
            print(f"Agência: {conta.agencia}")
            print(f"Número da Conta: {conta.numero_conta}")
            print(f"Titular: {conta.titular.nome}")
            print(f"Saldo: R$ {conta.saldo:.2f}")
            print("=" * 30)

    def selecionar_conta(self, numero_conta):
        return next((conta for conta in self.contas if conta.numero_conta == numero_conta), None)

def main():
    sistema = SistemaBancario()

    while True:
        menu = """

        [nu] Novo usuário
        [nc] Nova conta
        [lc] Listar contas
        [ac] Acessar conta
        [q] Sair

        => """
        opcao_principal = input(menu)

        if opcao_principal == "nu":
            nome = input("Informe o nome completo: ")
            cpf = input("Informe o CPF do usuário (somente números): ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço completo (rua, número - bairro - cidade/sigla estado): ")
            sistema.criar_cliente(nome, cpf, data_nascimento, endereco)

        elif opcao_principal == "nc":
            cpf_titular = input("Informe o CPF do titular da conta: ")
            titular = sistema.buscar_cliente(cpf_titular)
            if titular:
                sistema.criar_conta(titular)
            else:
                print("Titular não encontrado.")

        elif opcao_principal == "lc":
            sistema.listar_contas()

        elif opcao_principal == "ac":
            numero_conta = int(input("Informe o número da conta para acessar: "))
            conta_atual = sistema.selecionar_conta(numero_conta)
            if conta_atual:
                while True:
                    menu_conta = """

                    [d] Depositar
                    [s] Sacar
                    [e] Extrato
                    [v] Voltar ao menu principal
                    [q] Sair

                    => """
                    opcao_conta = input(menu_conta)

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
                        print("Operação inválida, por favor selecione novamente a operação desejada.")
            else:
                print("Conta não encontrada.")

        elif opcao_principal == "q":
            print("Saindo do sistema.")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()