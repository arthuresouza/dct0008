"""
File: node.py
Original Author: Ken Lambert (Fundamentals of Python Data Structure)
Adapted by: Arthur Souza
"""
from Node import Node
class LinkedList():


    def __init__(self, head = None):
        self.head = head

    def __len__(self):
        tamanho = 0
        probe = self.head
        while probe != None:
            tamanho += 1
            probe = probe.next
        return tamanho

    def __str__(self):
        if self.isEmpty():
            return "Lista Vazia"
        
        resultado = ""
        probe = self.head
        while probe is not None:
            resultado += f"({probe.data})"
            # Se existir um próximo nó, coloca a seta
            if probe.next is not None:
                resultado += " -> "
            probe = probe.next
        return resultado

    def isEmpty(self):
        return self.head is None
    
    def travessia(self):
        probe = self.head
        while probe is not None:
            print(probe.data)
            probe = probe.next

    def search(self, targetItem):
        probe = self.head
        while probe is not None and targetItem != probe.data:
            probe = probe.next
        if probe is not None:
            return probe
        else:
            raise Exception("O item não está na lista.")

    def getItemAt(self, index):
        """Indice deve ser 0 <= index = n
            n = tamanho da lista """
        probe = self.head
        while index > 0:
            probe = probe.next
            index -= 1
        return probe.data
        
    def update(self, targetItem, newItem):
        probe = self.head
        while probe is not None and targetItem != probe.data:
            probe = probe.next
        if probe is not None:
            probe.data = newItem
            return True
        else:
            return False
        
    def updateAt(self, index, newItem):
        # Considere 0 <= index < n
        probe = self.head
        while index > 0:
            probe = probe.next
            index -= 1
        probe.data = newItem

    def insertAtFirst(self,newItem):
        self.head = Node(newItem,self.head)

    def insertAtLast(self,newItem):
        newNode = Node(newItem)
        if self.head is None:
            self.head = newNode
        else:
            probe = self.head
            while probe.next is not None:
                probe = probe.next
            probe.next = newNode
    
    def removeFirst(self):
        removedItem = self.head.data
        self.head = self.head.next
        return removedItem
    
    def removeLast(self):
        removedItem = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            probe = self.head
            while probe.next.next is not None:
                probe = probe.next
                removedItem = probe.next.data
                probe.next = None
        return removedItem
        
    def insertAt(self,newItem, index):
        if self.head is None or index <= 0:
            self.head = Node(newItem,self.head)
        else:
            # Search for node at position index - 1 or the last position
            probe = self.head
            while index > 1 and probe.next is not None:
                probe = probe.next
                index -= 1
                # Insert new node after node at position index - 1
            # or last position
            probe.next = Node(newItem, probe.next)

    def removeAt(self, index):
        # Assumes that the linked structure has at least one item
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
            return removedItem
        else:
            # Search for node at position index - 1 or
            # the next to last position
            probe = self.head
            while index > 1 and probe.next.next is not None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return removedItem