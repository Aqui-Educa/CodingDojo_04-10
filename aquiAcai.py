##

valor_kg = 37.00

p = 9.25
m = 18.50
g = 27.75

adicional = int(input("Deseja quantos adicionais? "))

def tamanho():
    
    pass

def preco(tamanho, adicional):
    preco = tamanho + (adicional*2.50)
    return preco

print(preco(p, adicional))