def somar():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)

def subtrair():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)

def multiplicar():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)

def dividir():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    else:
        print("Erro: Divisão por zero não é permitida.")

def menu():  
    while True:  
        print("\nMenu de Operações:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")  

        opcao = input("Escolha uma opção (0-4): ")

        if opcao == '1':
            somar()
        elif opcao == '2':
            subtrair()
        elif opcao == '3':
            multiplicar()
        elif opcao == '4':
            dividir()
        elif opcao == '0':  
            print("Saindo do programa.")
            break  
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()