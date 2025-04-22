import utils
livros=[]
#lista livros de exemplo
exemplolivros=[
    {"id":1,
    "titulo":"livro1",
    "autor":"autor1",
    "assunto":"assunto1",
    "editora":"editora1",
    "ano":2000,
    "estado":"disponivel",
    "leitor":None,
    "nr_emprestimos":0},
    {"id":2,
    "titulo":"livro2",
    "autor":"autor2",
    "assunto":"assunto2",
    "editora":"editora2",
    "ano":1500,
    "estado":"disponivel",
    "leitor":None,
    "nr_emprestimos":0 },
    {"id":3,
    "titulo":"livro3",
    "autor":"autor3",
    "assunto":"assunto3",
    "editora":"editora3",
    "ano":2020,
    "estado":"disponivel",
    "leitor":None,
    "nr_emprestimos":0 }
]
lista_campos_privados=["id","estado","leitor","nr_emprestimos"]
def getlivro(id):
    for livro in livros:
        if livros["id"]==id:
            return livro
    return None
def configurar():
    livros.extend(exemplolivros)
def menulivros():

    op=0
    while op!=6:
        op=utils.Menu(["Adicionar","listar","Editar","Apagar","Pesquisar","Voltar"],"Menu de livros")
        if op==6:
            break
        if op==1:
            Adicionar()
        if op==2:
            Listar(livros)
        if op==3:
            editar()
        if op==4:
            Apagar()
        if op==5:
            pesquisar_listar()
def Adicionar():
    print("#### Adicionar livro novo ####")
    #Titulo
    titolo=utils.lerstr(3,"intrudoza o titulo: ")
    #Autor
    autor=utils.lerstr(3,"intrudoza o autor: ")
    #Assunto
    assunto=utils.lerstr(3,"intrudoza o assunto: ")
    #editora
    editora=utils.lerstr(3,"intruduza a editora: ")
    #ano de edição
    ano=utils.ler_numero_inteiro_limites(1500,2030,"introduza o ano de edição: ")
    #id
    id=1
    if len(livros)>0:
        id=livros[len(livros)-1]["id"]+1
    novo={
        "id":id,
        "titulo":titolo,
        "autor":autor,
        "assunto":assunto,
        "editora":editora,
        "ano":ano,
        "estado":"disponivel",
        "leitor":None,
        "nr_emprestimos":0
        }
    livros.append(novo)
    print(f"livro registado com sucesso. Tem {len(livros)}")
#listar livro
def Listar(lista_listar):
    print("#"*80)
    for livro in lista_listar:
        print(f"Id:{livro["id"]} Nome:{livro["titulo"]} Assunto:{livro["assunto"]} Estado:{livro["estado"]}")
        print("-"*80)
#editar livro
def editar():
    #pesquisar o livro a editar
    livros_editar=pesquisar()
    #mostrar os dados de cada livro encontrado
    if len(livros_editar)==0:
        print("não foram encontrados livros.")
        return
    #mostrar todos os dados
    Listar(livros_editar)
    #permitir alterar os dados
    id=utils.ler_numero_inteiro("Intrudoza o Id do livro a editar ou 0(zero) para cancelar: ")
    #livro com o Id indicado
    livro=None
    for l in livros_editar:
        if l["id"]==id:
            livro=l
            break
    if livro==None:
        print("O id indicado não existe")
        return
    #escolher o campo a editar
    lista_campos=list(livro.keys())
    for c in lista_campos_privados:
        lista_campos.remove(c)
    op=utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo=lista_campos[op-1]
    #Mostrar o valor atual do campo a editar
    print(f"O campo {campo} tem o valor {livro[campo]}")
    novo_valor=utils.lerstr(3,"Novo")
    livro[campo]=novo_valor
    print("Edição concluída com sucessos. ")
#apagar livro
def Apagar():
    # Pesquisar o leitor a editar
    leitores_apagar = pesquisar()
    # mostrar os dados de cada leitor encontrado
    if len(leitores_apagar) == 0:
        print("Não foram encontrados leitores com esse nome.")
        return
    # mostrar os leitores encontrados
    for leitor in leitores_apagar:
        op = input(f"Deseja apagar {leitor["autor"]}?: ")
        if op in "sS":
            livros.remove(leitor)
            print("livro removido com sucesso")
#pesquisar
def pesquisar_listar():
    resultado=pesquisar()
    Listar(resultado)
def pesquisar():
    #deixar o utilizador escolher o campo de pesquisa
    op=utils.Menu(["Autor","Titulo"],"Escolha o campo de pesquisa: ")

    #criar um lista para os resultados
    l_resultados=[]
    if op==1:
        campo="autor"
    else:
        campo="titulo"
    pesquisa=utils.lerstr(3,f"{campo} a pesqquisar: ")
    for livro in livros:
        if pesquisa.lower() in livro[campo].lower():
            l_resultados.append(livro)
    return (l_resultados)

    #adicionar à lista os que correspondem ao resultado