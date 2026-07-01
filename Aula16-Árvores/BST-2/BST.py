"""
Classe BST para árvore BST
@author Arthur Souza
Baseado no código em https://github.com/joaoarthurbm/eda-implementacoes/blob/master/java/src/bst/BST.java
"""
from Node import Node
from collections import deque

from collections import deque

class BST:
    def __init__(self, raiz = None):
        self.raiz = raiz
        self.tamanho = 0
        
    def esta_vazia(self) -> bool:
        return self.raiz is None
        
    def inserir(self, element: int) -> None:
        """
        Implementação iterativa da adição de um elemento em uma árvore binária de pesquisa.
        :param element: o valor a ser adicionado na árvore.
        """
        self.tamanho += 1
        if self.esta_vazia():
            self.raiz = Node(element)
        else:
            aux = self.raiz
            
            while aux is not None:
                if element < aux.dado:
                    if aux.esquerdo is None:
                        new_node = Node(element)
                        aux.esquerdo = new_node
                        new_node.pai = aux
                        return
                    aux = aux.esquerdo
                else:
                    if aux.direito is None:
                        new_node = Node(element)
                        aux.direito = new_node
                        new_node.pai = aux
                        return
                    aux = aux.direito

    def min(self):
        """
        Retorna o nó que contém o valor mínimo da árvore. Implementação recursiva.
        :return: o nó contendo o valor mínimo da árvore ou None se a árvore estiver vazia.
        """
        if self.esta_vazia():
            return None
        return self._min(self.raiz)
        
    def _min(self, node):
        """
        Retorna o nó que contém o valor mínimo da árvore cuja raiz é passada como parâmetro. Implementação recursiva.
        :param node: a raiz da árvore.
        :return: o nó contendo o valor mínimo da árvore ou None se a árvore estiver vazia.
        """
        if node.esquerdo is None:
            return node
        else:
            return self._min(node.esquerdo)

    def max(self):
        """
        Retorna o nó que contém o valor máximo da árvore. Implementação iterativa.
        :return: o nó contendo o valor máximo da árvore ou None se a árvore estiver vazia.
        """
        if self.esta_vazia():
            return None
            
        node = self.raiz
        while node.direito is not None:
            node = node.direito
            
        return node
        
    def _max(self, node):
        """
        Retorna o nó que contém o valor máximo da árvore cuja raiz é passada como parâmetro. Implementação recursiva.
        :param node: raiz da árvore.
        :return: o nó contendo o valor máximo da árvore ou None se a árvore estiver vazia.
        """
        if node.direito is None:
            return node
        else:
            return self._max(node.direito)
            
    def predecessor(self, node):
        """
        Retorna o nó cujo valor é predecessor (anterior na listagem em ordem) do valor passado como parâmetro. 
        :param node: O nó para o qual deseja-se identificar o predecessor.
        :return: O nó contendo o predecessor do valor passado como parâmetro. 
                 O método retorna None caso não haja predecessor.
        """
        if node is None:
            return None
            
        if node.esquerdo is not None:
            return self._max(node.esquerdo)
        else:
            aux = node.pai
            
            while aux is not None and aux.dado > node.dado:
                aux = aux.pai
                
            return aux

    def sucessor(self, node):
        """
        Retorna o nó cujo valor é sucessor do valor passado como parâmetro. 
        :param node: O nó para o qual deseja-se identificar o sucessor.
        :return: O nó contendo o sucessor do valor passado como parâmetro. 
                 O método retorna None caso não haja sucessor.
        """
        if node is None:
            return None
            
        if node.direito is not None:
            return self._min(node.direito)
        else:
            aux = node.pai
            
            while aux is not None and aux.dado < node.dado:
                aux = aux.pai
                
            return aux

    def inserir_recursivo(self, element: int) -> None:
        """
        Implementação recursiva do método de adição.
        :param element: elemento a ser adicionado.
        """
        if self.esta_vazia():
            self.raiz = Node(element)
        else:
            aux = self.raiz
            self.aux_inserir_recursivo(aux, element)
        self.tamanho += 1
        
    def _aux_inserir_recursivo(self, node, element: int) -> None:
        """
        Método para auxiliar na implementação recursiva do método de adição.
        :param node: a raiz da árvore.
        :param element: elemento a ser adicionado.
        """
        if element < node.dado:
            if node.esquerdo is None:
                new_node = Node(element)
                node.esquerdo = new_node
                new_node.pai = node
                return
            self.aux_inserir_recursivo(node.esquerdo, element)
        else:
            if node.direito is None:
                new_node = Node(element)
                node.direito = new_node
                new_node.pai = node
                return
            self.aux_inserir_recursivo(node.direito, element)

    def remover(self, value: int) -> None:
        """
        Remove o nó com o valor passado como parâmetro.
        :param value: O valor a ser removido.
        """
        to_remove = self.busca(value)
        if to_remove is not None:
            self._aux_remover(to_remove)
            self.tamanho -= 1

    def _aux_remover(self, to_remove: Node) -> None:
        """
        Método privado auxiliar para gerenciar a remoção do nó.
        :param to_remove: O nó a ser removido.
        """
        # Primeiro caso: o nó é uma folha.
        if to_remove.e_folha():
            if to_remove == self.raiz:
                self.raiz = None
            else:
                if to_remove.dado < to_remove.pai.dado:
                    to_remove.pai.esquerdo = None
                else:
                    to_remove.pai.direito = None
                    
        # Segundo caso: o nó tem apenas o filho esquerdo ou apenas o filho direito
        elif to_remove.so_filho_esquerdo():
            if to_remove == self.raiz:
                self.raiz = to_remove.esquerdo
                self.raiz.pai = None
            else:
                to_remove.esquerdo.pai = to_remove.pai
                if to_remove.dado < to_remove.pai.dado:
                    to_remove.pai.esquerdo = to_remove.esquerdo
                else:
                    to_remove.pai.direito = to_remove.esquerdo
                    
        elif to_remove.so_filho_direito():
            if to_remove == self.raiz:
                self.raiz = to_remove.direito
                self.raiz.pai = None
            else:
                to_remove.direito.pai = to_remove.pai
                if to_remove.dado < to_remove.pai.dado:
                    to_remove.pai.esquerdo = to_remove.direito
                else:
                    to_remove.pai.direito = to_remove.direito
                    
        # Terceiro caso: o nó tem dois filhos
        else:
            sucessor_node = self.sucessor(to_remove)
            to_remove.dado = sucessor_node.dado
            self._aux_remover(sucessor_node)

    def busca(self, element: int):
        """
        Busca o nó cujo valor é igual ao passado como parâmetro. Essa é a implementação 
        iterativa clássica da busca binária em uma árvore binária de pesquisa.
        :param element: O elemento a ser procurado.
        :return: O nó contendo o elemento procurado. O método retorna None caso
                 o elemento não esteja presente na árvore.
        """
        aux = self.raiz
        
        while aux is not None:   
            if aux.dado == element: 
                return aux
            elif element < aux.dado: 
                aux = aux.esquerdo
            else: 
                aux = aux.direito
                
        return None

    def busca_recursiva(self, element: int):
        """
        Busca o nó cujo valor é igual ao passado como parâmetro. Essa é a implementação 
        recursiva clássica da busca binária em uma árvore binária de pesquisa.
        :param element: O elemento a ser procurado.
        :return: O nó contendo o elemento procurado. O método retorna None caso
                 o elemento não esteja presente na árvore.
        """
        return self._aux_busca_recursiva(self.raiz, element)
        
    def _aux_busca_recursiva(self, node, element: int):
        """
        Busca o nó cujo valor é igual ao passado como parâmetro na sub-árvore cuja raiz é node.
        :param node: a raiz da árvore.
        :param element: O elemento a ser procurado.
        :return: O nó contendo o elemento procurado. O método retorna None caso
                 o elemento não esteja presente na árvore.
        """
        if node is None: 
            return None
        if element == node.dado: 
            return node
        if element < node.dado: 
            return self._aux_busca_recursiva(node.esquerdo, element)
        else: 
            return self._aux_busca_recursiva(node.direito, element)

    def altura(self) -> int:
        """
        Retorna a altura da árvore.
        """
        return self._aux_altura(self.raiz)
        
    def _aux_altura(self, node) -> int:
        """
        Método para auxiliar a recursão. Retorna a altura da árvore cuja raiz é passada como parâmetro.
        """
        if node is None: 
            return -1
        else: 
            return 1 + max(self._aux_altura(node.esquerdo), self._aux_altura(node.direito))

    def pre_order(self) -> None:
        """
        Percorre a árvore em pré-ordem.
        """
        self._aux_pre_order(self.raiz)

    def _aux_pre_order(self, node) -> None:
        if node is not None:
            print(node.dado)
            self._aux_pre_order(node.esquerdo)
            self._aux_pre_order(node.direito)

    def in_order(self) -> None:
        """
        Percorre a árvore em-ordem.
        """
        self._aux_in_order(self.raiz)

    def _aux_in_order(self, node) -> None:
        if node is not None:
            self._aux_in_order(node.esquerdo)
            print(node.dado)
            self._aux_in_order(node.direito)

    def pos_order(self) -> None:
        """
        Percorre a árvore em pós-ordem.
        """
        self._aux_pos_order(self.raiz)

    def _aux_pos_order(self, node) -> None:
        if node is not None:
            self._aux_pos_order(node.esquerdo)
            self._aux_pos_order(node.direito)
            print(node.dado)
            
    def in_level(self) -> list:
        """
        Percorre a árvore em largura. 
        :return: Uma lista com os elementos percorridos em largura.
        """
        res_list = []
        queue = deque()
        
        if not self.esta_vazia():
            queue.append(self.raiz)
            while queue:
                current = queue.popleft()
                res_list.append(current.dado)
                
                if current.esquerdo is not None: 
                    queue.append(current.esquerdo)
                if current.direito is not None: 
                    queue.append(current.direito)   
        return res_list

    def tamanho(self) -> int:
        """
        :return: o tamanho da árvore.
        """
        return self.tamanho
    
if __name__ == "__main__":
    bst = BST()
    print("Inserindo elementos na BST [10, 5, 15, 3, 7, 12, 18]")
    bst.inserir(10)
    bst.inserir(5)
    bst.inserir(15)
    bst.inserir(3)
    bst.inserir(7)
    bst.inserir(12)
    bst.inserir(18)

    print("Travessia em Ordem:")
    bst.in_order()

    print("\nTravessia em Pré-Ordem:")
    bst.pre_order()

    print("\nTravessia em Pós-Ordem:")
    bst.pos_order()

    print("\nTravessia em Nível:")
    print(bst.in_level())

    print("\nValor mínimo na BST:", bst.min().dado)
    print("Valor máximo na BST:", bst.max().dado)

    remover = bst.busca(5)
    if remover:
        bst.remover(remover.dado)
        print("\nTravessia em ordem após remover 5:")
        bst.in_order()