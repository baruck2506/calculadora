import operacoes
import time

def calculadora():
    print("Calculadora Simples")

    while True:
        print("Selecione uma operação:")
        print("1.Soma")
        print("2.Subtração")
        print("3.Multiplicação")
        print("4.Divisão")
        print("5.Sair")

        opcao = input(">>>")
        
        opcoes = ["1", "2", "3", "4", "5"]
        while opcao not in opcoes:
            opcao = input(">>>")
        
        if opcao == "5":
            print("encerrando calculadora...")
            time.sleep(2)
            break


        num1 = float(input("digite o primeiro numero:"))
        num2 = float(input("digite o segundo numero:"))

        if opcao == "1":
            print("Resultado: ", operacoes.soma(num1, num2))
            input("aperte enter para prosseguir")
        elif opcao == "2":
            print("Resultado: ", operacoes.subtracao(num1, num2))
            input("aperte enter para prosseguir")
        
        elif opcao == "3":
            print("Resultado: ", operacoes.multiplicacao(num1, num2))
            input("aperte enter para prosseguir")

        elif opcao == "4":
            print("Resultado: ", operacoes.divisao(num1, num2))
            input("aperte enter para prosseguir")

        else:
            print("opção invalida, tente novamente")

calculadora()

