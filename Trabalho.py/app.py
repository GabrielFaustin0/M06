import utils,pratos,os,mesas,pedidos,estatisticas
DEBUG=False
def menuprincipal():
    if DEBUG:
        pratos.configurar()
        mesas.configurar()
    os.system("cls")
    op=0
    while op!=7:
        op=utils.Menu(["Cardapio","Mesas","Pedidos","Dar entrada","Dar saida","Estatisticas","Terminar"],"Menu Principal")
        if op==7:
            break
        if op==1:
            pratos.menupratos()
        if op==2:
            mesas.menumesas()
        if op==3:
            pedidos.menupedidos()
        if op==4:
            pedidos.Entrar()
        if op==5:
            pedidos.saida()
        if op==6:
            estatisticas.menuestatisticas()

if __name__=="__main__":
    menuprincipal()