##

valor_kg = 37.00

p = 9.25
m = 18.50
g = 27.75

tamanho = str(input("Informe o tamanho desejado? ")).lower()
adicional = int(input("Deseja quantos adicionais? "))

def verificarTamanho(tamanho):
    while tamanho not in ['p', 'm', 'g']:
        
   else:
       if tamanho == 'p':
            tamanho = p
        
        if tamanho == 'm':
            tamanho = m
        
        if tamanho == 'g':
            tamanho = g
            
        return tamanho
    #     print('Infome se P, M ou G: ')
    #     tamanho = str(input("Informe o tamanho desejado? ")).lower()
    # else:
    #     pass

def preco(tamanho, adicional):
    preco = tamanho + (adicional*2.50)
    return preco

print(verificarTamanho(tamanho))
print(preco(tamanho, adicional))