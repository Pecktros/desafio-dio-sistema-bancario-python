# %%
import os

def operacao_deposito(saldo, extrato):
    limpar_terminal()
    valor_deposito = float(input("Insira o valor a ser depositado: "))
    if valor_deposito <= 0: 
        print("O valor inserido é inválido.")

    else:
        saldo += valor_deposito
        extrato += f"R$ +{valor_deposito:.2f}\n"
        print(f"Deposito de R${valor_deposito:.2f} realizado com sucesso!")
    
    return saldo, extrato



def operacao_saque(saldo, extrato):
    limpar_terminal()
    global LIMITE_SAQUES
    global numero_saques
    valor_saque = float(input("Insira o valor de saque: "))

    if valor_saque <= 0: 
        print("O valor inserido é inválido.")
    
    elif valor_saque > saldo: 
        print("Saldo não é suficiente.") 
    
    elif valor_saque > limite: 
        print("Valor máximo de R$500,00 excedido.")
    
    elif LIMITE_SAQUES <= numero_saques: 
        print("Quantidade de saques diários excedido.")

    else:
        saldo -= valor_saque
        extrato += f"R$ -{valor_saque:.2f}\n"
        numero_saques += 1
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
    
    return saldo, extrato



def operacao_extrato(saldo, extrato):
    limpar_terminal()

    if extrato == "": print("Não foram realizada movimentações.") 
    else: 
        # print(f"{extrato}\nSaldo: R${saldo}")
        print(f"""
======= EXTRATO =======
{extrato}\nSaldo: R${saldo}
=======================
""", end="")

    return saldo, extrato



def limpar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')



menu = """
 ______BANCO DIO______
|                     |
|    [1] Depositar    |
|    [2] Sacar        |      
|    [3] Extrato      |
|    [0] Sair         |
|_____________________|
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
opcoes = {"1":operacao_deposito, 
          "2":operacao_saque, 
          "3":operacao_extrato
          }


while True:
    try:
        limpar_terminal()
        opcao = input(menu).strip()
        if opcao == "0": break

        elif opcao in opcoes: 
            saldo, extrato = opcoes[opcao](saldo, extrato)
            input("\n[Enter para continuar]")
            
        else: input("Insira uma operação válida.")
    
    except ValueError:
        input("Erro no valor inserido.")
    





# %%
