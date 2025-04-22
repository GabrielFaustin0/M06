import utils,mesas
def menuestatisticas():
    op=0
    while op!=3:
        op=utils.Menu(["Numero de cliêntes","Mesas ocupada","Voltar"],"Menu estatisticas: ")
        if op==5:
            break
        if op==1:
            numeroclientes()
        if op==2:
            numeromesasocup()
def numeroclientes():
    n=0
    for i in mesas.mesas:
        n=n+i["lugares_ocupados"]
    print(n)
def numeromesasocup():
    n=0
    for i in mesas.mesas:
        if i["estado"]=="indisponivel":
            n=n+1
    print(n)