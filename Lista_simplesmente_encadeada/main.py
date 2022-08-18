from Lista_encadeada.lista_simplismente_encadeada import ListaSimples

lista = ListaSimples()
print("Lista:",)
print(lista)
print("Tamanho da lista:",lista.tamanho_lista())
print("========================================")
lista.adicionar(10)
lista.adicionar(20)
lista.adicionar(50)
lista.adicionar(59)
lista.adicionar(89)
print("Lista após os valores adicionados:")
print(lista)
print("Tamanho da lista:",len(lista))
print("========================================")
lista.adicionar_index(0, 60)
lista.adicionar_index(3, 33)
lista.adicionar_index(3, 100)
lista.adicionar_index(5, 60)
lista.adicionar_index(23, 90)
lista[2] = 1
print("Lista após os valores adicionados:")
print(lista)
print("Tamanho da lista:",lista.tamanho_lista())
print("========================================")
print("Valor que está no índice indicado:",lista[0])
print("Valor que está no índice indicado:",lista.get_valor(5))
print("========================================")
print("Índice do valor indicado:",lista.get_index(50))
print("========================================")
lista.remove_valor(60)
lista.remove_valor(100)

print("Lista após os valores removidos:")
print(lista)
print("Tamanho da lista:",lista.tamanho_lista())
print("========================================")
lista.remove_index(6)
print("Lista após os Indices removidos:")
print(lista)
print("Tamanho da lista:",lista.tamanho_lista())
print("========================================")
lista.ordenar()
print("Lista ordenada:")
print(lista)
print("Tamanho da lista:",lista.tamanho_lista())
print("========================================")
lista.inverter()
print("Lista invertida:")
print(lista)
print("Tamanho da lista:",lista.tamanho_lista())
print("========================================")
print("get_lista_invertida(). Essa função apenas printa a lista invertida:")
print(lista.get_lista_invertida())
print("Lista Normal:")
print(lista)