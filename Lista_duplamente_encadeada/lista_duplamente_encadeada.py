class Node():
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return self.dado


class ListaDuplamente():
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

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
            no.anterior = self.fim
            self.fim = no
        self.tamanho += 1

    def __setitem__(self, key, value):
        return self.adicionar_index(key, value)

    def __get_perc(self, posicao):
        if posicao <= self.tamanho / 2:
            perc = self.inicio
            contador = 0
            while contador < posicao - 1:
                perc = perc.proximo
                contador += 1
        else:
            perc = self.fim
            contador = self.tamanho - 1
            while contador > posicao - 1:
                perc = perc.anterior
                contador -= 1
        return perc

    def adicionar_index(self, posicao, dado):
        no = Node(dado)
        if posicao == 0:
            no = Node(dado)
            no.proximo = self.inicio
            self.inicio.anterior = no
            self.inicio = no
            self.tamanho += 1
            return True
        elif posicao >= self.tamanho:
            self.adicionar(dado)
            return True
        else:
            perc = self.__get_perc(posicao)
            no.proximo = perc.proximo
            no.anterior = perc
            perc .proximo = no
            no.proximo.anterior = no
        self.tamanho += 1
        return True

    def __getitem__(self, item):
        return self.get_valor(item)

    def get_valor(self, posicao):
        if self.tamanho == 0 or posicao > self.tamanho - 1:
            raise ("Índice não existe na lista!")
        perc = self.__get_perc(posicao + 1)
        return perc.dado

    def get_index(self, dado):
        i = 0
        f = self.tamanho - 1
        perc = self.inicio
        perc_f = self.fim
        while i != f:
            if perc.dado == dado:
                return i
            elif perc_f.dado == dado:
                return f
            perc = perc.proximo
            perc_f = perc_f.anterior
            i += 1
            f -= 1

    def remove_index(self, posicao):
        if posicao == 0:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            self.tamanho -= 1
            return True
        elif posicao == self.tamanho - 1:
            self.fim = self.fim.anterior
            self.fim.proximo = None
        else:
            perc = self.__get_perc(posicao)
            perc_c = perc.proximo.proximo
            perc.proximo = perc_c
            perc_c.anterior = perc
        self.tamanho -=1
        return True

    def remove_valor(self, dado):
        index = self.get_index(dado)
        self.remove_index(index)
        return True

    def get_lista_invertida(self):
        valor = "["
        valor += f"{self.fim.dado}"
        perc = self.fim
        while perc != self.inicio:
            perc = perc.anterior
            valor += f",{perc.dado}"
        valor += "]"
        return valor

    def inverter(self):
        contador = 0
        tamanho = self.tamanho
        while tamanho > contador:
            perc = self.fim
            self.adicionar_index(contador, perc.dado)
            self.fim = perc.anterior
            perc.anterior.proximo = None
            perc.anterior = None
            contador += 1
        self.tamanho -= contador

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