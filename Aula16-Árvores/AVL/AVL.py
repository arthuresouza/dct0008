from collections import deque
from Node import Node

class AVL:
    
    def __init__(self, raiz = None):
        self.raiz = raiz
        self.tamanho = 0 

    def esta_vazia(self):
        return self.raiz is None

    # Implementação iterativa da adição
    def inserir(self, dado):
        """
        Implementação iterativa da adição de um elemento em uma árvore AVL.
        :param dado: o valor a ser adicionado na árvore.
        """
        if self.esta_vazia():
            self.raiz = Node(dado)
            self.tamanho += 1
            return
        
        sonda = self.raiz
        
        while sonda is not None:
            if dado < sonda.dado:
                if sonda.esquerdo is None:
                    novo_esquerdo = Node(dado)
                    sonda.esquerdo = novo_esquerdo
                    novo_esquerdo.pai = sonda
                    
                    desbalanceado = self.esta_balanceado(novo_esquerdo)
                    if desbalanceado is not None:
                        self.rotacionar(desbalanceado)
                    
                    self.tamanho += 1
                    return
                
                sonda = sonda.esquerdo
            else:
                if sonda.direito is None:
                    novo_direito = Node(dado)
                    sonda.direito = novo_direito
                    novo_direito.pai = sonda
                    
                    desbalanceado = self.esta_balanceado(novo_direito)
                    if desbalanceado is not None:
                        self.rotacionar(desbalanceado)
                    
                    self.tamanho += 1
                    return
                
                sonda = sonda.direito

    # Checa do node passado até a raíz da árvore se existe um desbalanceamento.
    def esta_balanceado(self, node:Node):
        """
        Checa do node passado até a raíz da árvore (pai = None) se existe um desbalanceamento.
        :param node: node de onde se começa a checagem
        :return: o node desbalanceado ou None caso a árvore esteja balanceada
        """
        sonda = node        
        while sonda is not None:
            if not sonda.esta_balanceado():
                return sonda            
            sonda = sonda.pai            
        return None

    # Implementação recursiva do método de adição.
    def inserir_recursivo(self, dado):
        """
        Implementação recursiva do método de adição.
        :param element: elemento a ser adicionado.
        """
        if self.esta_vazia():
            self.raiz = Node(dado)
        else:
            self.aux_inserir_recursivo(self.raiz, dado)
            
        self.tamanho += 1
    
    # Método para auxiliar na implementação recursiva do método de adição.
    def aux_inserir_recursivo(self, node:Node, dado):
        """
        Método para auxiliar na implementação recursiva do método de adição.
        :param node: a raíz da árvore.
        :param element: elemento a ser adicionado.
        """
        if dado < node.dado:
            if node.esquerdo is None:
                novo_esquerdo = Node(dado)
                node.esquerdo = novo_esquerdo
                novo_esquerdo.pai = node
                self.rebalancear(node)
                return
            self.aux_inserir_recursivo(node.esquerdo, dado)
            self.rebalancear(node)
        else:
            if node.direito is None:
                novo_direito = Node(dado)
                node.direito = novo_direito
                novo_direito.pai = node
                self.rebalancear(node)
                return            
            self.aux_inserir_recursivo(node.direito, dado)
            self.rebalancear(node)

    def rebalancear(self, node:Node):
        fb = node.fb()
        if abs(fb) > 1:
            self.rotacionar(node)

    # Escolhe e executa o melhor caso de rotação
    def rotacionar(self, desbalanceado:Node):
        """
        Escolhe e executa o melhor caso de rotação a se fazer analisando
        o nó do qual a rotação deve partir.
        
        :param unbalanced: nó do qual a rotação deve partir
        """
        x = desbalanceado
        
        if x.pendendo_esquerda():
            y = x.esquerdo
            
            if y is not None and y.esquerdo is not None:
                self.rotacao_direita(x) # Caso LL (Rotação Simples à Direita)
            else:
                self.rotacao_esquerda(y) # Caso LR (Rotação Dupla: Esquerda em y, Direita em x)
                self.rotacao_direita(x)
        else: # pendendo para direita
            y = x.direito
            
            if y is not None and y.direito is not None:
                self.rotacao_esquerda(x) # Caso RR (Rotação Simples à Esquerda)
            else:
                self.rotacao_direita(y) # Caso RL (Rotação Dupla: Direita em y, Esquerda em x)
                self.rotacao_esquerda(x)

    # Rotaciona o nó à direita.
    def rotacao_direita(self, node:Node):
        """
        Rotaciona o nó à direita        
        :param node: nó a partir de onde a rotação ocorre
        """
        nova_raiz = node.esquerdo
        
        # Ajusta o pai do new_root
        nova_raiz.pai = node.pai
        
        # O filho direito de new_root se torna o filho esquerdo de node
        node.esquerdo = nova_raiz.direito
        if node.esquerdo is not None:
            node.esquedo.pai = node
            
        # node se torna o filho direito de new_root
        nova_raiz.direito = node
        node.pai = nova_raiz
        
        # Ajusta o filho do antigo pai de node
        if nova_raiz.pai is not None:
            if nova_raiz.pai.esquerdo == node:
                nova_raiz.pai.esquerdo = nova_raiz
            else:
                nova_raiz.pai.direito = nova_raiz
        else:
            self.raiz = nova_raiz # new_root é a nova raiz da AVL

    # Rotaciona o nó à esquerda.
    def rotacao_esquerda(self, node:Node):
        """
        Rotaciona o nó à esquerda.
        :param node: nó a partir de onde a rotação ocorre
        """
        nova_raiz = node.direito
        
        # Ajusta o pai do new_root
        nova_raiz.pai = node.pai
        
        # O filho esquerdo de new_root se torna o filho direito de node
        node.direito = nova_raiz.esquerdo
        if node.direito is not None:
            node.direito.pai = node
            
        # node se torna o filho esquerdo de new_root
        nova_raiz.esquerdo = node
        node.pai = nova_raiz
        
        # Ajusta o filho do antigo pai de node
        if nova_raiz.pai is not None:
            if nova_raiz.pai.direito == node:
                nova_raiz.pai.direito = nova_raiz
            else:
                nova_raiz.pai.esquerdo = nova_raiz
        else:
            self.raiz = nova_raiz # new_root é a nova raiz da AVL
 
    def em_ordem(self):
       """Percurso em Ordem."""
       lyst = list()
       def recurse(node:Node):
           if node != None:
               recurse(node.esquerdo)
               lyst.append(node.dado)
               recurse(node.direito)
       recurse(self.raiz)
       return lyst

    # Retorna o tamanho da árvore.
    def tamanho(self):
        """
        :return: o tamanho da árvore.
        """
        return self.tamanho

# Exemplo de uso (opcional, para testes):
avl = AVL()
avl.inserir(10)
avl.inserir_recursivo(20)
avl.inserir(5)
avl.inserir_recursivo(30)
avl.inserir(15)
avl.inserir(13)
print(avl.em_ordem()) # Deve imprimir a árvore balanceada
