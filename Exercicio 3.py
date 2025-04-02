 # 3- Desenvolva um algoritmo que solicite ao usuário que digite um número inteiro e divida 10 pelo número digitado. Se o número digitado for 0, levante uma exceção embutida com uma mensagem de erro apropriada. Em seguida, imprima o resultado da divisão

class TenDivisionError(Exception):
    pass

def ten_division():
    try:
        n = int(input('Digite um número Não Múltiplo de 10'))
        if  n % 10 == 0:
            raise TenDivisionError
        print(f'Número aprovado!: {n}')
    except(TenDivisionError):
        print(f'Número Digitado é Divisível por 10: {n}')
    except(ValueError):
        print('Digite um número inteiro válido')

continuar = True
while continuar:
    ten_division()
    cont = str(input('Deseja Continuar? (Yy/Nn): ')).strip().lower()
    if cont in 'n':
        continuar = False

print('\n\nFim do Programa!')