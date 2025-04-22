import utils,os
Produtos=[]
exemploprodutos=[{"nome":"Feijoada á Brasileira","tipo":"Carne","descricao":"Feijão preto com cubos de carne de porco com arroz e batata frita","preço":7.50},
    {"nome":"Filetes de pescada","tipo":"Peixe","descricao":"Filetes de pescada com arroz","preço":7.50},
    {"nome":"Arroz de tofu","tipo":"Vegetariano","descricao":"Arroz com tofu","preço":7.50},
    {"nome":"Acetea","tipo":"bebida","descricao":"sumo","preço":2.50}
]
def configurar():
    Produtos.extend(exemploprodutos)
def menupratos():
    
    op=0
    while op!=6:
        op=utils.Menu(["Adicionar","listar","Editar","apagar","Pesquisar","Voltar"],"Menu De pratos e bebidas")
        if op==6:
            break
        if op==1:
            Adicionar()
        if op==2:
            listar(Produtos)
        if op==3:
            editar()
        if op==4:
            apagar()
        if op==5:
            pesquisarlistar()
def Adicionar():
    nome=utils.lerstr(3,"Introduza o nome do prato/bebida")
    tipo=utils.lerstr(5,"Digite o tipo de produto")
    descricao=utils.lerstr(5,"Digite uma breve descrição")
    preço=utils.ler_numero_decimal("Qual o preço do produto (Não é necessario usar o simbolo euro (€))")
    novo={
        "nome":nome.capitalize(),
        "tipo":tipo,
        "descricao":descricao,
        "preço":preço
    }
    Produtos.append(novo)
    print("O produto foi adicionado com sucesso")
def listar(lista_pesquisar):
    for i in lista_pesquisar:
        print(f"Nome do prato: {i["nome"]}/ tipo: {i["tipo"]}/ descrição: {i["descricao"]}/ preço: {i["preço"]}€")
def pesquisarlistar():
    resultado=pesqusar()
    listar(resultado)
def pesqusar():
    listapesquisar=[]
    filtro=utils.Menu(["Tipo de produto/(Carne,Peixe ou Vegetariano)","preço"],"Escolha um filtro")
    if filtro==1:
        filtro2=utils.lerstr(4,"Digite o tipo de produto/(Carne,Peixe ou Vegetariano)")
        for i in Produtos:
            if filtro2.lower() in i["tipo"].lower():
                listapesquisar.append(i)
    
    else:
        filtro2=utils.ler_numero_decimal("Digite o preço maximo que deseja.")
        for i in Produtos:
            if i["preço"]<=filtro2:
                listapesquisar.append(i)
    
    return listapesquisar

def editar():
    produto_editar=pesqusar()
    if len(produto_editar)==0:
        print("Não foram encontrados produtos.")
        return
    listar(produto_editar)
    nome=utils.lerstr(0,"Intruduza o nome do produto a editar ou não escreva para cancelar: ")
    if len(nome)==0:
        return
    produto=None
    for p in produto_editar:
        if nome.lower() in p["nome"].lower():
            produto=p
            break
    if produto==None:
        print("O produto indicado não existe")
        return
    lista_campos=list(produto.keys())
    op=utils.Menu(lista_campos,"Qual o campo a editar? ")
    campo=lista_campos[op-1]
    print(f"O campo {campo} tem o valor {produto[campo]}")
    novo_valor=utils.lerstr(4,"Novo")
    produto[campo]=novo_valor
    print("Edição concluída com sucessos. ")
def apagar():
    produto_apagar=pesqusar()
    if len(produto_apagar)==0:
        print("Não foram encontrados produtos.")
        return
    listar(produto_apagar)
    for produto in produto_apagar:
        op = input(f"Deseja apagar {produto["nome"]}? s/n: ")
        if op in "sS":
            Produtos.remove(produto)
            print("livro removido com sucesso")