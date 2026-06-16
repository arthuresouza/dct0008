"""
Classe node para árvore AVL
@author Arthur Souza
Baseado no código em https://github.com/joaoarthurbm/eda-implementacoes/blob/master/java/src/avl/AVL.java
"""

class Node():
    def __init__(self, dado = None, esquerdo = None, direito = None, pai = None):
        self.dado = dado
        self.esquerdo = esquerdo
        self.direito = direito
        self.pai = pai
      
    def altura(self,node):
        if node == None:
            return -1
        else:
            return 1 + max(self.altura(node.esquerdo),self.altura(node.direito))

    def so_filho_esquerdo(self):
        return self.esquerdo is not None and self.direito is None

    def so_filho_direito(self):
        return self.esquerdo is None and self.direito is not None

    def e_folha(self):
        return self.esquerdo is None and self.direito is None
    
    def fb(self):
        altura_esquerdo = -1
        altura_direito = -1
        if self.esquerdo is not None:
            altura_esquerdo = self.altura(self.esquerdo)
        if self.direito is not None:
            altura_direito = self.altura(self.direito)
        return altura_esquerdo - altura_direito

    def pendendo_esquerda(self):
        return self.fb() >= 1

    def pendendo_direita(self):
        return self.fb() <= -1

    def esta_balanceado(self):
        fator_balanceamento = self.fb()
        return -1 <= fator_balanceamento <= 1

    def max(self,altura_esquerdo, altura_direito):
        return altura_esquerdo if altura_esquerdo >= altura_direito else altura_direito 