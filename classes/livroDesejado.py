from classes.livro import Livro

class LivroDesejado(Livro):  #classe filha
  qtdLivros = 0

  def __init__(self,preco_real, preco_desconto,nome,autor,ano,categoria):    #método contrutor
    Livro.__init__(self,nome,autor,ano,categoria)
    self.preco_real = preco_real
    self.preco_desconto = preco_desconto
    self.qtdLivros+=1
    self.codigo = self.qtdLivros
 
  def getPrecoReal(self):
    return self.preco_real

  def getPrecoDesconto(self):
    return self.preco_desconto

  def imprimirDescricao(self,livro): #polimorfismo (sobrescrita)
    print("Descrição completa:")
    print("Codigo: "+str(livro.codigo))
    print("Nome: "+str(livro.nome))
    print("Ano: "+str(livro.ano))
    print("Categoria: "+str(livro.categoria))
    print("Preco real: "+str(livro.preco_real))
    print("Preco desconto: "+str(livro.preco_desconto))
    

