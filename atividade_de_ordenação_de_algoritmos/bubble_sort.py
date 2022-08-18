#esse algoritmo vai percorrer toda a lista, levando os elementos de maior valor para a direita e consequentimente os menores para a esquerda.
lista = [5, 3, 1, 7, 9, 0, 2, 4, 6, 8]
def bubble_sort(lista):
    final = len(lista)
    while final > 0:
        i = 0
        #percorrendo a lista de 0 até o final
        while i < final - 1:
            if lista[i] > lista[i + 1]:
                #se o elemento atual for maior que o proximo será realizada a troca de posição entre eles
                tempo = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = tempo
            i += 1
        final -= 1
    return lista
#retornará a lista ordenada
p = bubble_sort(lista)
print(p)
