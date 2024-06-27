LIMITE_SAQUES = 3

print("****** Seja Bem Vindo ao Banco ******")

def menu():
    menu = """
+++++++++-Menu-+++++++++

[d]  Depositar
[s]  Sacar
[e]  Extrato
[u]  Criar Usuario
[c]  Criar Conta
[l]  Listar Contas
[q]  Sair


=> """

    resposta = input(menu)
    return resposta



def deposito(saldo, extrato,/):
    valor_deposito = float(input("Quanto você deseja depositar? "))

    saldo += valor_deposito

    extrato += f" Deposito R${valor_deposito:.2f} |"

    print(f"Seu deposito foi executado, seu saldo atual é de R$ {saldo:.2f}.")

    return saldo, extrato

def saque(*,numero_saques, saldo, extrato):
    if numero_saques < LIMITE_SAQUES:
        valor_saque = float(input("Qual você deseja sacar? "))
        if(valor_saque > 500):
            print("!!!O valor desejado supera o seu limite de R$ 500.00.!!!")
        else:
            saldo -= valor_saque
            print(f"Seu saque foi executado, seu saldo atual é de R$ {saldo:.2f}.")

            extrato += f" Saque R${valor_saque:.2f} |"
        numero_saques += 1 
    else:
        print("!!!Você já atingiu o seu limite de saques diários!!!")

    return numero_saques, saldo, extrato

def emissao_extrato(saldo,/,*, extrato):
    print(f"##Seu saldo é de {saldo:.2f}##")
    print(f"Seu extrato -> {extrato}")

def criar_usuários(usuarios):
    cpf = input("Qual o cpf do usuário? ")

    if not verifica_cpf(cpf,usuarios):
        print(f"!!!O cpf {cpf} já foi registrado anteriormente!!!")
    else:
        nome = input("Qual é o seu nome? ")
        data_nascimento = input("Qual é a sua data de nascimento? (dd-mm-aaaa) ")
        endereco = input("Qual o seu endereço? (Logradouro, nro - bairro - cidade/sigla estado) ")

        usuarios.append({"nome":nome, "cpf": cpf,"data de nascimento": data_nascimento ,"endereço": endereco})

        print(f"O usuário {nome} foi criado")

    return usuarios

def criar_conta(contas,usuarios, numero_contas):
    
    numero_contas = numero_contas + 1
    cpf = input("Qual o cpf do usuário?")

    if verifica_cpf(cpf, usuarios):
        print(f"!!!Não existe usuário com o cpf {cpf}!!!")
    else:
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                contas.append({"agencia": "0001", "numero_conta": numero_contas,"usuario": usuario})
        print(f"Foi criada a conta de numero: {contas[numero_contas-1]["numero_conta"]}, na agência 0001, para o portador do cpf:{cpf}")
            
    return contas, numero_contas
def verifica_cpf(cpf,usuarios):
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return False
    return True

def listar_contas(contas):
    for conta in contas:
        linha = f"""
Agência:  {conta["agencia"]}
C/C:  {conta["numero_conta"]}
Titular:  {conta["numero_conta"]}
"""
        print(linha)

def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_contas = 0
    usuarios=[]
    contas=[]
    
    while True:

        opcao = menu()

        if opcao == "d":
            [saldo, extrato] = deposito(saldo, extrato)
            print("=================================")
        elif opcao == "s":
            [numero_saques, saldo, extrato]= saque(numero_saques=numero_saques, saldo=saldo, extrato=extrato)
            print("=================================")
        elif opcao == "e":
            emissao_extrato(saldo, extrato=extrato)
            print("=================================")
        elif opcao == "u":
            usuarios = criar_usuários(usuarios)
            print("=================================")
        elif opcao == "c":
            [contas, numero_contas] = criar_conta(contas, usuarios, numero_contas)
            print("=================================")
        elif opcao == "l":
            listar_contas(contas)
            print("=================================")
        elif opcao == "q":
            break

        else:
            print("!!!Operação inválida, por favor selecione novamente a operação desejada.!!!")
            print("=================================")

if __name__ == "__main__":
    main()
