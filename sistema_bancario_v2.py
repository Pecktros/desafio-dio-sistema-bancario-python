# %%
import os
from datetime import datetime

def operacao_deposito(saldo, extrato):
    limpar_terminal()
    valor_deposito = float(input("Insira o valor a ser depositado: "))
    if valor_deposito <= 0: 
        print("O valor inserido é inválido.")

    else:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        saldo += valor_deposito
        extrato += f"R$ +{valor_deposito:.2f} - {data}\n"
        print(f"Deposito de R${valor_deposito:.2f} realizado com sucesso!")
    
    return saldo, extrato


def operacao_saque(*, saldo, extrato, limite, numero_saques, limite_saques):
    limpar_terminal()
    valor_saque = float(input("Insira o valor de saque: "))

    if valor_saque <= 0: 
        print("O valor inserido é inválido.")
    
    elif valor_saque > saldo: 
        print("Saldo não é suficiente.") 
    
    elif valor_saque > limite: 
        print("Valor máximo de R$500,00 excedido.")
    
    elif limite_saques <= numero_saques: 
        print("Quantidade de saques diários excedido.")

    else:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        saldo -= valor_saque
        extrato += f"R$ -{valor_saque:.2f} - {data}\n"
        numero_saques += 1
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
    
    return saldo, extrato


def operacao_extrato(saldo, /, *, extrato):
    limpar_terminal()
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if extrato == "": print("Não foram realizada movimentações.") 
    else: 
        print(f"""
============= EXTRATO =============
{extrato}\nSaldo: R${saldo} - {data}
===================================
""", end="")

    return saldo, extrato


def cadastrar_usuario (usuarios):
    limpar_terminal()
    filtro_usuario, cpf_usuario = filtrar_usuario(usuarios)

    if filtro_usuario:
        print("----- Usuário já cadastrado. -----")
        return usuarios
    
    else:
        nome_usuario = input("Informe o seu nome completo: ")
        data_nascimento_usuario = input("Informe sua data de nascimento (dd/mm/aa): ")
        endereco_usuario = input("Informe seu endereço (logradouro, nro - bairro - cidade/UF): ")

        usuarios.append({
            "nome_completo":nome_usuario, 
            "cpf":cpf_usuario,
            "data_nascimento":data_nascimento_usuario, 
            "endereco":endereco_usuario
            })
        
        print("Usuário cadastrado com sucesso.")
        return usuarios


def criar_conta(usuarios, contas_usuarios, agencia, numero_conta):
    limpar_terminal()

    filtro_usuario, cpf = filtrar_usuario(usuarios)

    if filtro_usuario:
        numero_conta += 1
        contas_usuarios.append({
            "agencia":agencia, 
            "numero_conta":numero_conta, 
            "usuario":filtro_usuario,
        })
        print("Conta criada com sucesso.")
        return contas_usuarios, numero_conta
    
    else:
        print("Usuário não cadastrado.")
        return contas_usuarios, numero_conta


def filtrar_usuario(usuarios):
    cpf_usuario = input("Informe o número do CPF (somente os números): ").split()
    usuario_filtrado = [usuarios for i in usuarios if i["cpf"] == cpf_usuario]
    if usuario_filtrado:
        return usuario_filtrado[0], cpf_usuario
    else:
        return None, cpf_usuario


def listar_usuarios(usuarios):
    limpar_terminal()
    for i in usuarios:
        nome = i["nome_completo"]
        cpf = i["cpf"]
        data_nascimento = i["data_nascimento"]
        endereco = i["endereco"]
        print(f"Nome: {nome}",
              f"CPF: {cpf}",
              f"Data de Nascimento: {data_nascimento}",
              f"Endereço: {endereco}\n", sep="\n")


def listar_contas(contas_usuarios):
    limpar_terminal()
    for i in contas_usuarios:
        nome = i["usuario"][0]["nome_completo"]
        cpf = i["usuario"][0]["cpf"]
        agencia = i["agencia"]
        numero_conta = i["numero_conta"]
        print(f"Nome: {nome}",
              f"CPF: {cpf}",
              f"Agência: {agencia}",
              f"Conta: {numero_conta}\n", sep="\n")


def limpar_terminal():
    os.system('cls' if os.name=='nt' else 'clear')


def main():
    menu_inicial = """
     ______BANCODIO_______
    |                     |  
    |     [1] Gerente     |
    |     [2] Cliente     |
    |     [0] Sair        |
    |_____________________|
    => """

    menu_gerente = """
     _____________BANCODIO_____________
    |                                  |
    |     [1] Cadastrar Usuário        |
    |     [2] Criar Conta Corrente     |
    |     [3] Lista de Usuários        | 
    |     [4] Lista de Contas          | 
    |     [0] Voltar                   |
    |__________________________________|
    => """

    menu_cliente = """
     _____________BANCODIO_____________
    |                                  |
    |     [1] Depositar                |      
    |     [2] Sacar                    |
    |     [3] Extrato                  |
    |     [0] Voltar                   |
    |__________________________________|
    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numero_conta = 0

    
    usuarios = []
    contas_usuarios = []

    opcoes_menu = ["1", "2"]
    opcoes_gerente = ["1", "2", "3", "4"]
    opcoes_usuario = ["1", "2", "3"]




    while True:
        try:
            limpar_terminal()
            opcao_menu = input(menu_inicial).strip()
            
            if opcao_menu == "0": break

            elif opcao_menu in opcoes_menu:

                while True:
                    if opcao_menu == "1":
                        limpar_terminal()
                        opcao_gerente = input(menu_gerente).strip()

                        if opcao_gerente == "0": break

                        elif opcao_gerente in opcoes_gerente:
                            if opcao_gerente == "1":
                                usuarios = cadastrar_usuario(usuarios)
                                
                            elif opcao_gerente == "2":
                                contas_usuarios, numero_conta = criar_conta(usuarios, contas_usuarios, AGENCIA, numero_conta)
                            
                            elif opcao_gerente == "3":
                                listar_usuarios(usuarios)

                            elif opcao_gerente == "4":
                                listar_contas(contas_usuarios)
                            
                            input("\n[Pressione Enter para continuar]")
                        
                        else: input("\nInsira uma operação válida. [Enter para continuar]")
                            

                    elif opcao_menu == "2":
                        limpar_terminal()
                        opcao_usuario = input(menu_cliente).strip()

                        if opcao_usuario == "0": break

                        elif opcao_usuario in opcoes_usuario:
                            
                            if opcao_usuario == "1":
                                saldo, extrato= operacao_deposito(saldo, extrato)
                            
                            elif opcao_usuario == "2":
                                saldo, extrato = operacao_saque(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

                            elif opcao_usuario == "3":
                                saldo, extrato = operacao_extrato(saldo, extrato=extrato)
            
                            input("\n[Enter para continuar]")
                        
                        else: input("\nInsira uma operação válida. [Enter para continuar]")
                        
            else: input("\nInsira uma operação válida. [Enter para continuar]")
                
        
        except ValueError:
            input("Erro no valor inserido.")
    

main()

a = {}



# %%
