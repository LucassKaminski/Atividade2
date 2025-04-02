class NumeroImparError(Exception):
    pass
 

def verifica_par():
    try:
        num = int(input('Digite um número Par: '))
        if num % 2 != 0:
            raise NumeroImparError()
        print(f'O número {num} é PAR')
    except NumeroImparError:
        print('O número é ímpar, Digite um número par')
    except(ValueError):
        print('Inválido, Digite um número inteiro: ')


continuar = True
while continuar:
    if __name__ == '__main__':
        verifica_par()
        cont = str(input('Deseja continuar? (Yy/Nn): '))
        if cont in 'Nn':
            continuar = False
