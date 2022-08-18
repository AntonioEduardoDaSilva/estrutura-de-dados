class Node():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __str__(self):
        return self.dado

class ListaSimples():
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    #def adicionar(self, dado):
    #   no = Node(dado)
    #    if self.inicio is None:
    #        self.inicio = no
    #    else:
    #        perc = self.inicio
    #        while perc.proximo is not None:
    #            perc = perc.proximo
    #        perc.proximo = no
    #    self.tamanho += 1

    def tamanho_lista(self):
        return self.tamanho

    def __len__(self):
        return self.tamanho

    def adicionar(self, dado):
        no = Node(dado)
        if self.inicio is None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1

    def __setitem__(self, key, value):
        return self.adicionar_index(key, value)

    def adicionar_index(self, posicao, dado):
        no = Node(dado)
        if posicao == 0 :
            no = Node(dado)
            no.proximo = self.inicio
            self.inicio = no
            return True
        elif posicao >= self.tamanho:
            self.adicionar(dado)
            self.tamanho += 1
            return True
        else:
            perc = self.__get_perc(posicao - 1)
            no.proximo = perc.proximo
            perc.proximo = no
            self.tamanho += 1
        return True

    def __getitem__(self, item):
        return self.get_valor(item)

    def get_valor(self, posicao):
        if self.tamanho == 0 or posicao > self.tamanho - 1:
            raise ("Índice não existe na lista!")
        if posicao == 0:
            return self.inicio.dado
        if posicao == self.tamanho - 1:
            return self.fim.dado
        perc = self.__get_perc(posicao)
        return perc.dado

    def get_index(self, dado):
        perc = self.inicio
        i = 0
        while perc:
            if perc.dado == dado:
                return i
            perc = perc.proximo
            i += 1
        raise ValueError("{} não existe na lista!".format(dado))

    def remove_index(self, posicao):
        if posicao == 0:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return True
        else:
            perc = self.__get_perc(posicao - 1)
            atual = perc.proximo
            perc.proximo = atual.proximo
            self.tamanho -= 1
            return True

    def remove_valor(self, dado):
        index = self.get_index(dado)
        self.remove_index(index)
        return True

    def get_lista_invertida(self):
        valor = "["
        valor += f"{self.fim.dado}"
        contador = self.tamanho
        while contador != 1:
            contador -= 1
            perc = self.__get_perc_para_inverter(prev=True, posisao=contador)
            valor += f",{perc.dado}"
        valor += "]"
        return valor
    
    def __get_perc_para_inverter(self, prev=False, posisao=None):
        perc = self.inicio
        contador = 0
        if posisao > self.tamanho:
            raise Exception("Posição não existe na lista")
        if prev is False:
            while contador != posisao:
                perc = perc.proximo
                contador += 1
            return perc
        else:
            while contador != posisao - 1:
                perc = perc.proximo
                contador += 1
            return perc
    def __adicionar_index_inverter(self, posicao, dado):
        no = Node(dado)
        if posicao == 0 :
            no = Node(dado)
            no.proximo = self.inicio
            self.inicio = no
            return True
        elif posicao >= self.tamanho:
            self.adicionar(dado)
            return True
        else:
            perc = self.__get_perc(posicao - 1)
            no.proximo = perc.proximo
            perc.proximo = no
        return True

    def __remove_index_inverter(self, posicao):
        if posicao == 0:
            self.inicio = self.inicio.proximo
            return True
        else:
            perc = self.__get_perc(posicao - 1)
            atual = perc.proximo
            perc.proximo = atual.proximo
            return True

    def inverter(self):
        contador = 0
        tamanho = self.tamanho
        while tamanho > contador:
            perc = self.__get_perc(tamanho-1)
            perc.proximo = None
            self.__adicionar_index_inverter(contador, perc.dado)
            self.fim = perc
            contador += 1
        self.__remove_index_inverter(self.tamanho)



    def ordenar(self):
        tamanho = self.tamanho
        while tamanho > 0:
            contador = 0
            perc = self.inicio
            perc_ultimo = self.inicio.proximo
            while contador != tamanho - 1:
                if perc.dado > perc_ultimo.dado:
                    ord = perc.dado
                    perc.dado = perc_ultimo.dado
                    perc_ultimo.dado = ord
                contador += 1
                if perc_ultimo.proximo is not None:
                    perc = perc.proximo
                    perc_ultimo = perc_ultimo.proximo
            tamanho -= 1

    def __get_perc(self, posicao):
        if posicao < self.tamanho:
           perc = self.inicio
           for i in range(posicao):
               if perc:
                   perc = perc.proximo
           return perc

    def __str__(self):
        valor = "["
        if self.tamanho == 0:
            valor += "]"
            return valor

        perc = self.inicio
        while perc.proximo is not None:
            valor += "{},".format(perc.dado)
            perc = perc.proximo
        if perc is not None:
            valor += "{}]".format(perc.dado)
        else:
            valor += "]"
        return valor