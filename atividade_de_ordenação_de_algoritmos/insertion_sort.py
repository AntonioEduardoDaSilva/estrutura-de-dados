#esse algoritmo organiza a lista por partes, como uma lista virtual dentro da lista.
#ele sai pegando listas dentro da lista e organizando.
#após organizar uma lista dentro da lista ele sai aumentando o tamanho da lista virtual.
#dentro da lista virtual ele compara o elemento atual com seus antecessores, caso o antecessores sejam maior, eles sairão sendo levados para o final da lista virtual.
#isso irá acontecer até a lista virtual ficar do tamanho da lista verdadeira e organizada.
lista = [3, 0, 1, 4, 9, 6, 2, 5, 7, 6, 8]
def insertion_sort(lista):
    i = 1
    #comparando o elemento com seu antecessor
    while i < len(lista):
        temp = lista[i]
        troca = False
        a = i - 1
        #verificando se o elemento atual é menor que seu antecessor, caso seja, seu antecessor será impurrado para frente, ou seja, trocará de posição.
        while a >= 0 and lista[a] > temp:
            lista[a + 1] = lista[a]
            troca = True
            a -= 1
        if troca:
            lista[a + 1] = temp
        i += 1
    return lista
b = insertion_sort(lista)
print(b)
