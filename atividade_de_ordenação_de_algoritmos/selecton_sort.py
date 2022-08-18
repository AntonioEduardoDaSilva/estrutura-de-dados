#esse algoritmo verifica dentro da lista qual é o menor elemento, e quando confirma qual é, coloca-o em sua posição.
# após isso, faz a mesma coisa com todos os outros elementos, mas sempre deixando de fora os que já foram verificados e colocados na posição correta.
lista = [9, 4, 2, 0, 1, 3, 6, 5, 8, 7]
def selection_sort(lista):
    i = 0
    while i < len(lista) - 1:
        menor = i
        b = i + 1
        #confirmação de qual é o menor elemento
        while b < len(lista):
            if lista[b] < lista[menor]:
                menor = b
            b += 1
        #verificando se será preciso realizar a troca, para colocar o menor valor na sua posição dentro da lista
        if menor != i:
            troc = lista[i]
            lista[i] = lista[menor]
            lista[menor] = troc
        i += 1
    return lista
#retorna a lista organizada
q = selection_sort(lista)
print(q)
