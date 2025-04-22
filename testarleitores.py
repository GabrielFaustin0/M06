import utils
Leitores=[]
###############################################################
exemploleitores=[
    {"id":1,
    "nome":"Pedro",
    "idade":19,
    "email":"Email1@gmail.com",
    "infracoes":0
    },
    {"id":2,
    "nome":"Maria",
    "idade":20,
    "email":"Email2@gmail.com",
    "infracoes":3
    },
    {"id":3,
    "nome":"Manuel",
    "idade":10,
    "email":"Email3@gmail.com",
    "infracoes":1
    },
]
campos_privados=["id","nome"]
def configurar():
    Leitores.extend(exemploleitores)
#####################################################################
def menuleitores():
    op=0
    while op!=6:
        op=utils.Menu(["Adicionar","listar","Editar","Apagar","Pesquisar","Voltar"],"Menu de Leitores")
        if op==6:
            break
        if op==1:
            adicionar()
        if op==2:
            listar(Leitores)
        if op==3:
            editar()
        if op==4:
            pass
        if op==5:
            pesquisar_listar()

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################
def adicionar():
    print("###"*10)
    print("###"*10)
    print("#### Adicionar leitor novo ####")
    #nome
    nome=utils.lerstr(3,"intrudoza o nome: ")
    #idade
    idade=utils.ler_numero_inteiro_limites(5,120,"intrudoza a idade: ")
    #email
    email=utils.lerstr(3,"intrudoza o email: ")
    #Infrações
    infrações=0
    #id
    id=1
    if len(Leitores)>0:
        id=Leitores[len(Leitores)-1]["id"]+1
    novo={
        "id":id,
        "nome":nome,
        "idade":idade,
        "email":email,
        "infracoes":infrações
        }
    Leitores.append(novo)
    print(f"Novo Leitor registado com sucesso. Tem {len(Leitores)}")
    print("###"*10)
    print("###"*10)
##############################################################################
def listar(lista_listar):
    print("#"*80)
    for leitor in lista_listar:
        print(f"Id:{leitor["id"]} Nome:{leitor["nome"]} Assunto:{leitor["idade"]} Estado:{leitor["email"]} infrações:{leitor["infracoes"]}")
        print("-"*80)
###############################################
def editar():
    #pesquisar o livro a editar
    livros_editar=pesquisar()
    #mostrar os dados de cada livro encontrado
    if len(livros_editar)==0:
        print("não foram encontrados leitores.")
        return
    #mostrar todos os dados
    listar(livros_editar)
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
    for c in campos_privados:
        lista_campos.remove(c)
    op=utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo=lista_campos[op-1]
    #Mostrar o valor atual do campo a editar
    print(f"O campo {campo} tem o valor {livro[campo]}")
    novo_valor=utils.lerstr(3,"Novo")
    livro[campo]=novo_valor
    print("Edição concluída com sucessos. ")




########################################
def pesquisar_listar():
    resultado=pesquisar()
    listar(resultado)
def pesquisar():
    #deixar o utilizador escolher o campo de pesquisa
    op=utils.Menu(["nome","email"],"Escolha o campo de pesquisa: ")

    #criar um lista para os resultados
    l_resultados=[]
    if op==1:
        campo="nome"
    else:
        campo="email"
    pesquisa=utils.lerstr(3,f"{campo} a pesqquisar: ")
    for livro in Leitores:
        if pesquisa.lower() in livro[campo].lower():
            l_resultados.append(livro)
    return (l_resultados)

    #adicionar à lista os que correspondem ao resultado