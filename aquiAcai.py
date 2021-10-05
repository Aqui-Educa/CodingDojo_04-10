##

valor_kg = 37.00

p = 9.25
m = 18.50
g = 27.75

tamanho = str(input("Informe o tamanho desejado? "))
adicional = int(input("Deseja quantos adicionais? "))

def verificarTamanho(tamanho):
    while tamanho not in ["p", "m", "g"]:
        print('Infome se P, M ou G: ')
        tamanho = str(input("Informe o tamanho desejado? "))
        return

def preco(tamanho, adicional):
    preco = tamanho + (adicional*2.50)
    return preco

print(preco(p, adicional))