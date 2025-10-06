"""
CRUD Contatos permite o armazenamento da Agenda em Arquivo txt
"""

import Agenda
import ast

CRUD_AGENDA = "./Aula08-TAD/crud-agenda.txt"

class RepContatos():

    def __init__(self):
        pass

    def salva_contatos(self,contatos):
        for contato in contatos:
            with open(CRUD_AGENDA,"a") as arquivo:
                arquivo.write(str(contato)+"\n") 
                arquivo.flush()
                arquivo.close()
    
    def ler_contatos(self, contatos):
        with open(CRUD_AGENDA) as arquivo:
            for linha in arquivo:
                contatos.addContato(ast.literal_eval(linha.rstrip()))
            arquivo.close()