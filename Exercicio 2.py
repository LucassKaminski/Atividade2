# Desenvolva um algoritmo que solicite ao usuário que digite uma string e verifique se a string contém apenas letras maiúsculas. Se a string contiver letras minúsculas, levante uma exceção embutida com uma mensagem de erro apropriada. Em seguida, imprima uma mensagem informando que a string contém apenas letras maiúsculas.
class LetraMinusculaError(Exception):
    pass

continuar = True
while continuar:
    try: 
        palavra = str(input('Digite uma palavra somente com letras maiúsculas: '))
        for letra in palavra:
            if letra != letra.upper():
                raise LetraMinusculaError
        print(f'Você digitou: {palavra}')
        cont = str(input('Deseja continuar?: (Yy/Nn)'))
        if cont in 'Nn':
            continuar = False
    except(LetraMinusculaError):
        print('A palavra digitada contém Letras Minúsculas')
    except(TypeError):
        print('Digite somente caracteres válidos')

print('\n\nFim do Programa!')