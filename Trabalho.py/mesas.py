import utils
mesas=[]
exemplomesas=[{"n":1,"lugares":8,"lugares_ocupados":0,"estado":"disponivel","preço_pagar":0,"produtos_mesa":{}},
              {"n":2,"lugares":4,"lugares_ocupados":3,"estado":"indisponivel","preço_pagar":7.50,"produtos_mesa":{"Feijoada á Brasileira":1}},
              {"n":3,"lugares":2,"lugares_ocupados":2,"estado":"indisponivel","preço_pagar":20.00,"produtos_mesa":{"Feijoada á Brasileira":2,"Acetea":2}}
]
def configurar():
    mesas.extend(exemplomesas)
def menumesas():
    op=0
    while op!=6:
        op=utils.Menu(["Adicionar","listar","apagar","Pesquisar","Voltar"],"Menu De mesas")
        if op==5:
            break
        if op==1:
            adicionar()
        if op==2:
            listar(mesas)
        if op==3:
            apagar()
        if op==4:
            pesqusar()
def adicionar():
    lugares=utils.ler_numero_inteiro("intrudoza numero de lugares: ")
    n=1
    if len(mesas)>0:
        n=mesas[len(mesas)-1]["n"]+1
    novo={
        "n":n,
        "lugares":lugares,
        "lugares_ocupados":0,
        "estado":"disponivel",
        "preço_pagar":0,
        "produtos_mesa":{}
        }
    mesas.append(novo)
    print(f"Mesa registado com sucesso. Tem {len(mesas)}")
def listar(mesas):
    for mesa_p in mesas:
        print(f"Numero da mesa: {mesa_p["n"]}/ lugares: {mesa_p["lugares"]}/ estado: {mesa_p["estado"]}/produtos da mesa:{mesa_p["produtos_mesa"]}/preço a pagar: {mesa_p["preço_pagar"]}€")
def pesqusar():
    n_mesa=utils.ler_numero_inteiro("Qual o numero da mesa")
    for mesa in mesas:
        if n_mesa==mesa["n"]:
            print(f"Numero da mesa: {mesa["n"]}/ lugares: {mesa["lugares"]}/ estado: {mesa["estado"]}/produtos da mesa:{mesa["produtos_mesa"]}/preço a pagar: {mesa["preço_pagar"]}€")
            return mesa
        
def apagar():
    mesa_apagar=pesqusar()
    if mesa_apagar==None:
        print("Mesa não existe.")
        return
    if mesa_apagar==0:
        print("Não foram encontradas mesas.")
        return
    op = input(f"Deseja apagar {mesa_apagar["n"]}? s/n: ")
    if op in "sS":
        mesas.remove(mesa_apagar)
        print("Mesa removida com sucesso")