def travessia(head):
    probe = head
    while probe != None:
        print(probe.data)
        probe = probe.next

def busca(head, targetItem):
    probe = head
    while probe != None and targetItem != probe.data:
        probe = probe.next
    if probe != None:
        return probe
    else:
       raise Exception("O item não está na lista.")

def buscaIndex(head, index):
    """Indice deve ser 0 <= index = n
        n = tamanho da lista """
    probe = head
    while index > 0:
        probe = probe.next
        index -= 1
    return probe.data
    
def atualizar(head, targetItem, newItem):
    probe = head
    while probe != None and targetItem != probe.data:
        probe = probe.next
    if probe != None:
        probe.data = newItem
        return True
    else:
        return False
    
def atualizarIndex(head, index, newItem):
    # Considere 0 <= index < n
    probe = head
    while index > 0:
        probe = probe.next
        index -= 1
    probe.data = newItem