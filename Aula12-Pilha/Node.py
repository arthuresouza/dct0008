"""
File: node.py
Original Author: Ken Lambert (Fundamentals of Python Data Structure)
Adapted by: Arthur Souza
"""

class Node(object):
    """Representa um nó de uma lista ligada."""
    def __init__(self, data, next = None):
        """Instancia o Nó com o próximo apontando para Vazio."""
        self.data = data
        self.next = next
    

if __name__ == "__main__":
    # Nó vazio
    node1 = None
    # Nó com dados e link vazio
    node2 = Node("A", None)
    # Nó com dados e link para node2
    node3 = Node("B", node2)

    head = None
    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)
    # Print the contents of the structure
    while head != None:
        print(head.data)
        head = head.next