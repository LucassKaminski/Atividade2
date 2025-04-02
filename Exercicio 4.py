"""4 - Desenvolva um algoritmo que solicite ao usuário que digite duas strings e verifique se as strings têm o mesmo comprimento. Se as strings tiverem comprimentos diferentes, levante uma exceção personalizada com uma mensagem de erro apropriada. Em seguida, imprima uma mensagem informando que as strings têm o
mesmo comprimento."""
class DifferentLenString(Exception):
    def __init__(self, message="As palavras possuem tamanhos diferentes!"):
        super().__init__(message)

def verifica_string(str1, str2):
    if len(str1) != len(str2):
        raise DifferentLenString()
    print("As palavras digitadas possuem o mesmo tamanho!")

try:
    palavra1 = input("Digite uma palavra: ")
    palavra2 = input("Digite outra palavra: ")
    verifica_string(palavra1, palavra2)
except DifferentLenString as e:
    print(e)

print("\n\nFim do Programa!")
