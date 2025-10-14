

import Node

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
        str = ""
        probe = self.head
        while probe != None:
            str += f"({probe.data})"
            if(probe.next.next != None):
                str += "->"
            probe = probe.next
        return str

    def isEmpty(self):
        return self.head == None
    
    def travessia(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    def search(self, targetItem):
        probe = self.head
        while probe != None and targetItem != probe.data:
            probe = probe.next
        if probe != None:
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
        while probe != None and targetItem != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = newItem
            return True
        else:
            return False
        
    def updateAt(self, index, newItem):
        # Considere 0 <= index < n
        probe = self
        while index > 0:
            probe = probe.next
            index -= 1
        probe.data = newItem

    def insertAtFirst(self,newItem):
        self.head == Node(newItem,self.head)

    def insertAtLast(self,newItem):
        newNode = Node(newItem)
        if self.head is None:
            head = newNode
        else:
            probe = self.head
            while probe.next != None:
                probe = probe.next
                probe.next = newNode
    
    def removeFirst(self):
        removedItem = head.data
        head = head.next
        return removedItem
    
    def removeLast(self):
        removedItem = head.data
        if self.head.next is None:
            head = None
        else:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
                removedItem = probe.next.data
                probe.next = None
        return removedItem
        
    def insertAt(self,newItem):
        if self.head is None or index <= 0:
            self.head = Node(newItem,self.head)
        else:
            # Search for node at position index - 1 or the last position
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
                # Insert new node after node at position index - 1
            # or last position
            probe.next = Node(newItem, probe.next)

    def removeAt(self):
        # Assumes that the linked structure has at least one item
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
            return removedItem
        else:
            # Search for node at position index - 1 or
            # the next to last position
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return removedItem