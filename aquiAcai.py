##

valor_kg = 37.00

p = 9.25
m = 18.50
g = 27.75

tamanho = str(input("Informe o tamanho desejado? ")).lower()
adicional = int(input("Deseja quantos adicionais? "))

def verificarTamanho(tamanho):
    while tamanho in ['p', 'm', 'g']:
        if tamanho == 'p':
            tamanho = p
            return tamanho            
    
        elif tamanho == 'm':
            tamanho = m
            return tamanho            
        
        elif tamanho == 'g':
            tamanho = g     
            return tamanho

        else:
            print('Infome se P, M ou G: ')
            tamanho = str(input("Informe o tamanho desejado? ")).lower()
            continue 

  

verificarTamanho(tamanho)
def preco(tamanho, adicional):

    preco = tamanho + (adicional * 2.50)
    return preco

print(verificarTamanho(tamanho))
print(preco(tamanho, adicional))