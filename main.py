
from classes.livroAdquirido import LivroAdquirido
from classes.livroDesejado import LivroDesejado
opt = 1
livrosAdquiridos=[]
livrosDesejados=[]
print("Controle de livros")
while opt != 0:
  print("-----------------------------")
  print("1 - Inserir livro adquirido")
  print("2 - Listar livros adquiridos")
  print("3 - Inserir livro desejado")
  print("4 - Listar livros desejados")
  print("5 - Selecionar um livro adquirido")
  print("6 - Selecionar um livro desejado")
  print("0 - Sair")
  print("-----------------------------")
  opt = int(input("Digite uma opção:"))

  if opt == 1:
  
    preco_comprado = float(input("Preco:"))
    data_compra=input("Data da compra:")
    nome = input("Nome:")
    autor = input("Autor:")
    ano = int(input("Ano que foi lançado:"))
    categoria = input("Categoria:")

    #lista de objetos 

    livrosAdquiridos.append(LivroAdquirido(preco_comprado,data_compra,nome,autor,ano,categoria)) #instancia classe filha
    print("Codigo do livro:")
    print(livrosAdquiridos[-1].codigo)
    print("Livro adicionado com sucesso!")
  elif opt == 2:
    
    print("Livros Adquiridos | Total: " + str(len(livrosAdquiridos)))
  
    for livros in livrosAdquiridos:
      print(livros.nome)

  elif opt == 3:
    
    preco_real = float(input("Preco:"))
    preco_desconto=input("Preco com desconto:")
    nome = input("Nome:")
    autor = input("Autor:")
    ano = int(input("Ano que foi lançado:"))
    categoria = input("Categoria:")
   
    #lista de objetos 
    livrosDesejados.append(LivroDesejado(preco_real,preco_desconto,nome,autor,ano,categoria)) #instancia classe filha
    print("Codigo do livro:")
    print(livrosDesejados[-1].codigo)
    print("Livro adicionado com sucesso!")
  elif opt == 4:
    print("Livros Desejados | Total: " + str(len (livrosDesejados)))

    for livros in livrosDesejados:
      print(livros.nome)
  elif opt == 5:
    codigo = int(input("Código do livro:"))
    livrosAdquiridos[codigo-1].imprimirDescricao(livrosAdquiridos[codigo-1])
  elif opt == 6:
    codigo = int(input("Código do livro:"))
    livrosDesejados[codigo-1].imprimirDescricao(livrosDesejados[codigo-1])
  
print("Fim do programa")




