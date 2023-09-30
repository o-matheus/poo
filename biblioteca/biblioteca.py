from livro.livro_fisico import LivroFisico
from membros.membro import Membro

class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__membros = []

    def cadastrarMembro(self, membro: Membro):
        self.__membros.append(membro)
        print("Novo membro adicionado a biblioteca!")

    def deletarMembro (self, membro_id):
        for membro in self.__membros:
            if membro.membro_id == membro_id:
                self.__membros.remove(membro)
                print("Membro deletado com sucesso")

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print("Novo Livro adicionado a biblioteca!")

    def deletarLivros(self, livro_id):
        for livro in self.__livros:
            if livro.livro_id == livro_id:
                self.__livros.remove(livro)
                print("Livro deletado com sucesso")

    def listarLivros(self):
        print("---- Livros Cadastrados ----")
        for livro in self.__livros:
            print("---- Dados do Livro ----")
            print(f"Id: {livro.livro_id}")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano_publi}")
            print(f"Nº de páginas: {livro.numero_paginas} \n")

    def listarMembros(self):
        print("---- Membros Cadastrados ----")
        for membro in self.__membros:
            print(f"Id: {membro.membro_id}")
            print(f"Nome: {membro.nome}")
            print(f"Endereço: {membro.endereco}")
            print(f"Telefone: {membro.telefone}")

if __name__ == "__main__":
    biblioteca = Biblioteca()
    m1 = Membro(1, "Agatha", "Rua A", "85 99999 - 8888")
    m2 = Membro(1, "Rui", "Rua R", "85 98888 - 1111")
    l1 = LivroFisico(1, "Tolkien", "LOR", 1960, "1000")
    l2 = LivroFisico(2, "JK", "HP", 1990, "300")
    biblioteca.cadastrarMembro(m1)
    biblioteca.cadastrarMembro(m2)
    biblioteca.cadastrarLivro(l1)
    biblioteca.cadastrarLivro(l2)
    biblioteca.listarLivros()
    biblioteca.listarMembros()
