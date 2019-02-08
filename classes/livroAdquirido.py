from classes.livro import Livro

class LivroAdquirido(Livro):   #classe filha
  qtdLivros = 0
  
  def __init__(self,preco_comprado, data_compra,nome,autor,ano,categoria): #construtor
    Livro.__init__(self,nome,autor,ano,categoria)
    self.preco_comprado = preco_comprado
    self.data_compra = data_compra
    LivroAdquirido.qtdLivros+=1
    self.codigo = self.qtdLivros
 
  def getPrecoComprado(self):
    return self.preco_comprado

  def getDataCompra(self):
    return self.data_compra
    
  def imprimirDescricao(self,livro): #polimorfismo (sobrescrita)
    print("Descrição completa:")
    print("Codigo: "+str(livro.codigo))
    print("Nome: "+str(livro.nome))
    print("Ano: "+str(livro.ano))
    print("Categoria: "+str(livro.categoria))
    print("Preco comprado: "+str(livro.preco_comprado))
    print("Data de compra: "+str(livro.data_compra))
