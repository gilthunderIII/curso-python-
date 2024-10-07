menu = """
    [1] Extrato
    [2] Deposito
    [3] Saque
    [4] Sair
==> """

saldo  = 0 
limite  = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3 

while True :
    opcao = int(input(menu))
    
    if opcao == 1 : 
        print(F"\n=== Extrato =====")
        print("Sem movimentações."  if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================")
    
    elif opcao == 2 :
        valor =  float(input("Informe o valora a ser depositado: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Deposisto de R$ {valor:.2f}\n")
        else:
            print("valor infalido!")

    elif opcao == 3:
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo:
            print("Voce nao tem saldo suficiente! ")
        
        elif valor > limite:
            print("O valor do saque excede o limite")
        
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1 
            print(f"Saque de R$ {valor:.2f}\nrealisado com sucesso! ")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Número máximo de saques diários atingido.")
        else:
            print("Valor invalido!")
    
    elif opcao == 4:
        print("saindo ....")
        break
    else:
        print("Opção inválida! Tente novamente.")