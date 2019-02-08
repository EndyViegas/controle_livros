class Livro:     #classe pai (interface)
  def __init__(self,nome,autor,ano,categoria): #construtor
    self.nome = nome
    self.autor = autor
    self.ano = ano
    self.categoria = categoria  #atributos da classe pai
  
  def getNome(self):
    return self.nome

  def getCategoria(self):
    return self.categoria

  def getAutor(self):
    return self.autor

  def getAno(self):
    return self.ano

  def imprimirDescricao(self,livro):
    print("Descrição completa:")
    print("Codigo: "+self.codigo)
    print("Nome: "+self.nome)
    print("Ano: "+self.ano)
    print("Categoria: "+self.categoria)


  
  
  
