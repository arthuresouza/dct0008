"""
File: arrays.py
An Array is like a list, but the client can use
only [], len, iter, and str.
To instantiate, use <variable> = Array(<capacity>, <optional fill value>)
The fill value is None by default.
Original Author: Ken Lambert (Fundamentals of Python Data Structure)
Adapted by: Arthur Souza
"""
class Array():

    DEFAULT_CAPACITY = 5
    
    """Represents an array."""
    def __init__(self, capacity = DEFAULT_CAPACITY, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        for count in range(capacity):
            self.items.append(fillValue)
    
    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)
        
    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)
    
    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)
    
    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]
    
    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem

    def increaseSize(self):
        """Aumenta o tamanho do Array"""
        if(self.logicalSize == len(self.items)):
            temp = Array(len(self.items) * 2) # Cria um novo array
        for i in range(self.logicalSize): # percorre o array
            temp [i] = self.items[i] # copia os dados
        self.items = temp.items # atualiza a variável do array antigo.
    
    def decreaseSize(self):
        if self.logicalSize <= len(self.items) // 4 and len(self.items) >= self.DEFAULT_CAPACITY * 2:
            temp = Array(len(self.items) // 2) # Cria um novo array menor
            for i in range(self.logicalSize): # percorre o array
                temp [i] = self.items[i] # copia os dados
            self.items = temp.items # atualiza a variável do array antigo.

    def insertAt(self,newItem,targetIndex):
        # Se necessário aumente o tamanho físico do Array
        if(self.logicalSize == len(self.items)):
            self.increaseSize();
        # Desloque os itens para abrir o espaço
        for i in range(self.logicalSize, targetIndex, -1):
            self.items[i] = self.items[i - 1]
        # Insira o item e aumente o tamanho físico
        self.items[targetIndex] = newItem
        self.logicalSize += 1

    def removeAt(self,targetIndex):
        # Desloque os itens em uma posição
        for i in range(targetIndex, self.logicalSize - 1):
            self.items[i] = self.items[i + 1]
        # Decremente o tamanho lógico
        self.logicalSize -= 1
        # Diminua o tamanho array
        self.decreaseSize()