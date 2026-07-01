"""
Classe node para árvore BST
@author Arthur Souza
Baseado no código em https://github.com/joaoarthurbm/eda-implementacoes/blob/master/java/src/bst/BST.java
"""

class Node():
    def __init__(self, dado = None, esquerdo = None, direito = None, pai = None):
        self.dado = dado
        self.esquerdo = esquerdo
        self.direito = direito
        self.pai = pai    

    def so_filho_esquerdo(self):
        return self.esquerdo is not None and self.direito is None

    def so_filho_direito(self):
        return self.esquerdo is None and self.direito is not None

    def e_folha(self):
        return self.esquerdo is None and self.direito is None