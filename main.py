from calculadora import soma, subtracao, multiplicacao, divisao

def menu():
    options = ['Somar', 'Subtrair', 'Dividir', 
               'Multiplicar', 'Sair']

    print("\nCALCULADORA")

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    option = int(input('Selecione uma opção: '))
    return option

option = menu()

while option > 0 and option < 6:

    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    if option == 1:
        resultado = soma(numero1, numero2)
        print(f"{resultado:.2f}")

        option = menu()

    elif option == 2:
        resultado = subtracao(numero1, numero2)
        print(f"{resultado:.2f}")

        option = menu()

    elif option == 3:
        resultado = divisao(numero1, numero2)
        print(f"{resultado:.2f}")

        option = menu()

    elif option == 4:
        resultado = multiplicacao(numero1, numero2)
        print(f"{resultado:.2f}")

        option = menu()

    else:
        print("Encerrando calculadora")
        break