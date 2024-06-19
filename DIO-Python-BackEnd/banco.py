menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Quanto você deseja depositar?"))

        saldo += deposito

        extrato += f" Deposito R${deposito:.2f} |"

        print(f"Seu deposito foi executado, seu saldo atual é de R$ {saldo:.2f}.")
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Qual você deseja sacar?"))
            if(saque > 500):
                print("O valor desejado supera o seu limite de R$ 500.00.")
            else:
                saldo -= saque
                print(f"Seu saque foi executado, seu saldo atual é de R$ {saldo:.2f}.")

                extrato += f" Saque R${saque:.2f} |"
            numero_saques += 1 
        else:
            print("Você já atingiu o seu limite de saques diários")
    elif opcao == "e":
        print(extrato)
            
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")