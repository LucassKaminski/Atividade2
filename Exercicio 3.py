 # 3- Desenvolva um algoritmo que solicite ao usuário que digite um número inteiro e divida 10 pelo número digitado. Se o número digitado for 0, levante uma exceção embutida com uma mensagem de erro apropriada. Em seguida, imprima o resultado da divisão

def division(n):
    try:
        div = 10 / n
        return div
    except ZeroDivisionError:
        return 'Digite um número inteiro não nulo!'


print('Vamos dividir o número 10 por alguns números inteiros!')
while True:
    num = int(input('Digite um número inteiro não nulo: '))
    print(division(num))
    cont = str(input('Deseja continuar? Yy/Nn: ')).strip().lower()
    if cont in 'n':
        break

print('\n\nFIM DO PROGRAMA!')