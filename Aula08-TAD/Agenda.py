
"""
Módulo Agenda
Representa um sistema simples para armazenamento de contatos [nome, email, telefone]
em Arquivo
"""

import CRUDContatos

class Contato():
    """
    Classe Contato representa o TAD Contato composto por
    nome, email e telefone, todos do tipo str
    """        
    def __init__(self,nome = "", email = "", telefone = ""):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return str({"nome": self.nome, "email": self.email, "telefone": self.telefone})
    
    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    
    def setEmail(self, email):
        self.email = email
    def getNome(self):
        return self.email
    

    def setNome(self, telefone):
        self.telefone = telefone
    def getNome(self):
        return self.telefone    

class Contatos():
    
    """
    Classe Contatos representa uma lista de Contatos
    """
    def __init__(self):
        self.items = list()
        self.arquivo_contatos = CRUDContatos.RepContatos()

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)
    
    def getAll(self):
        self.arquivo_contatos.ler_contatos(self)
        return self.items
    
    def salvarContatos(self):
        self.arquivo_contatos.salva_contatos(self)

    def addContato(self,contato):
        self.items.append(contato)        
               
    def getContatobyNome(self,nome):
        self.getAll()
        for contato in self.items:
            if(nome == contato.getNome()):
                return contato
    
    def getContatobyEmail(self,email):
        self.getAll()
        for contato in self.items:
            if(email == contato.getEmail()):
                return contato          
