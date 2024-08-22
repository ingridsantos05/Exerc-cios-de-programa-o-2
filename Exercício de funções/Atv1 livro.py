#Suponha que você esta desenvolvendo um sistema de biblioteca . crie a classe livro com as seguintes caracteristicas:
#Atributos: titulo, autor, ano_publicado.
#Métodos: exibir_detalhes.
class livro:
    def __init__(self, titulo, autor, ano_publicação):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicação = ano_publicação

    def exibir_detalhes(self):
        print(f"Titulo: {self.titulo}\n")
        print(f"Autor: {self.autor}\n")
        print(f"Ano de publicação: {self.ano_publicação}\n")

livro1 = livro("Menino do pijama listrado", "John boyne",  2006)
livro2 = livro("Harry Potter", "Radcliffe", 2010)

print(livro1.exibir_detalhes())

print(livro2.exibir_detalhes())

