class Node():
    def __init__(self, dado):
        self.dado = dado
        self.direita = None
        self.esquerda = None
        self.nivel = 0
        self.altura = 0

    def is_folha(self):
        if self.direita is None and self.esquerda is None:
            return True
        return False

    def __str__(self):
        return str(self.dado)

class Arvore():

    def __init__(self):
        self.raiz = None
        self.__tamanho = 0
        self.caunt = 0

    #def adicionar(self, dado):
    #   no = Node(dado)
    #    if self.raiz is None:
    #        self.raiz = no
    #        self.__tamanho += 1
    #        self.__nivel = 1
    #    else:
    #        perc = self.raiz
    #        while True:
    #            if no.dado <= perc.dado:
    #                if perc.esquerda == None:
    #                    perc.esquerda = no
    #                    break
    #                else:
    #                    perc = perc.esquerda
    #            else:
    #                if perc.direita == None:
    #                    perc.direita = no
    #                    break
    #                else:
    #                    perc = perc.direita
    #        self.__tamanho += 1

    def add(self,dado):
        no = Node(dado)
        if self.raiz is None:
            self.raiz = no
            self.__tamanho += 1
        else:
            perc = self.raiz
            self.__add_recursivo(no, perc)
            self.__tamanho += 1
            #if self.caunt > self.raiz.altura:
            #   self.raiz.altura = self.caunt
            self.caunt = 0
    def __add_recursivo(self, no, perc):
        self.caunt += 1
        if no.dado < perc.dado:
            if perc.esquerda == None:
                perc.esquerda = no
            else:
                self.__add_recursivo(no, perc.esquerda)
                no.altura = self.caunt - 1
        else:
            if perc.direita == None:
                perc.direita = no
            else:
                self.__add_recursivo(no, perc.direita)
        no.nivel = self.caunt
        if perc == self.raiz:
            if self.caunt > self.raiz.altura:
                self.raiz.altura = self.caunt
        else:
            if self.caunt > perc.altura:
                perc.altura = self.caunt - perc.nivel

    def get_altura(self, valor=None):
        if valor is None:
            return self.raiz.altura
        no = self.is_get_dado(valor)
        if no is not None:
            return no.altura
        else:
            return None

    def get_nivel(self, valor=None):
        if valor is None:
            return self.raiz.nivel
        no = self.is_get_dado(valor)
        if no is not None:
            return no.nivel
        else:
            return None

    def remove_valor(self, valor, no=None):
        if no == None:
            no = self.raiz
        if no is None:
            return no
        if valor < no.dado:
            no.esquerda = self.remove_valor(valor, no.esquerda)
        elif valor > no.dado:
            no.direita = self.remove_valor(valor, no.direita)
        else:
            self.__tamanho -= 1
            if no.is_folha:
                return None
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                if no.esquerda is not None and no.direita is not None:
                    novo_no = self.sucessor(no)
                    no.dado = novo_no
                    no = self.remove_valor(novo_no, no)
        return no
            


    def sucessor(self, valor=None):
        if valor is None:
            perc = self.raiz
            if perc.direita is not None:
                return self.__get_sucessor(perc.direita)
        else:
            perc = self.is_get_dado(valor)
            if perc.direita is not None:
                return self.__get_sucessor(perc.direita)

    def __get_sucessor(self, perc):
        while perc.esquerda is not None:
            perc = perc.esquerda
        return perc

    def predecessor(self, valor=None):
        if valor is None:
            perc = self.raiz
            if perc.esquerda is not None:
                return self.__get_predecessor(perc.esquerda)
        else:
            perc = self.is_get_dado(valor)
            if perc.esquerda is not None:
                return self.__get_sucessor(perc.esquerda)

    def __get_predecessor(self, perc):
        while perc.direita is not None:
            perc = perc.direita
        return perc

    def is_get_dado(self, dado):
       if self.__tamanho == 0:
           return None
       return self.__get_index_recurcivo(dado, self.raiz)

    def __get_index_recurcivo(self,dado, perc):
        if dado == perc.dado:
            return perc
        else:
            if dado < perc.dado and perc.esquerda is not None:
                return self.__get_index_recurcivo(dado, perc.esquerda)
            else:
                if perc.direita is not None:
                    return self.__get_index_recurcivo(dado, perc.direita)

    def tamanho(self):
        return self.__tamanho

