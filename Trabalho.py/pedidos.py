import utils,mesas,pratos
def menupedidos():
    op=0
    while op!=5:
        op=utils.Menu(["Dar entrada","Adicionar pedidos","Consultar pedidos Da mesa","Dar Saida","Voltar"],"Escolha uma opção: ")
        if op==5:
            break
        if op==1:
            Entrar()
        if op==2:
            adicionar_pedidos()
        if op==3:
            mesas.listar(mesas.mesas)
        if op==4:
            saida()
def Entrar():
    cliêntes=utils.ler_numero_inteiro("Quantos cliêntes são.")
    mesa_ocupar=mesas.pesqusar()
    if mesa_ocupar==None:
        print("Mesa não existe.")
        return
    if mesa_ocupar["estado"]=="indisponivel":
        print("Já existem pessoas nessa mesa")
        return
    if mesa_ocupar==0:
        print("Não foram encontradas mesas.")
        return
    if cliêntes > mesa_ocupar["lugares"]:
        print(f"Não há lugares sufeciêntes na mesa {mesa_ocupar["n"]}")
        return
    mesa_ocupar["lugares_ocupados"]=cliêntes
    op="s"
    while op in "sS":
        op = input(f"Deseja dar entrada {mesa_ocupar["n"]}? s/n: ")
        if op in "sS":
            mesa_ocupar["estado"]="indisponivel"
            print("Entrada terminada")
            break
def adicionar_pedidos():
    mesa_pedido=mesas.pesqusar()
    if mesa_pedido==None:
        print("Mesa não existe.")
        return
    if mesa_pedido["estado"]=="disponivel":
        print("Não está ninguem na mesa para faser o pedido.")
        return
    if mesa_pedido==0:
        print("Não foram encontradas mesas.")
        return
    op="s"
    while op=="s" or op=="S":
        op = input(f"Deseja fazer o pedido na mesa {mesa_pedido["n"]}? s/n: ")
        if op in "sS":
            produto_pesquisar=pratos.pesqusar()
            if len(produto_pesquisar)==0:
                print("Não foram encontrados produtos.")
                return
            
            pratos.listar(produto_pesquisar)
            for produto in produto_pesquisar:
                op = input(f"Deseja adicionar {produto["nome"]} á mesa {mesa_pedido["n"]}? s/n: ")
                if op in "sS":
                    mesa_pedido["produtos_mesa"][produto["nome"]] = mesa_pedido["produtos_mesa"].get(produto["nome"],0) + 1
                    mesa_pedido["preço_pagar"]=mesa_pedido["preço_pagar"]+produto["preço"]
                    print("Pedido adicionado à mesa")
                    return
def saida():
    mesa_saida=mesas.pesqusar()
    if mesa_saida==None:
        print("Mesa não existe.")
        return
    if mesa_saida["estado"]=="disponivel":
        print("Não está ninguem na mesa para dar saida.")
        return
    if mesa_saida==0:
        print("Não foram encontradas mesas.")
        return
    print(f"O preço a pagar na mesa {mesa_saida["n"]} é de {mesa_saida["preço_pagar"]}€")
    mesa_saida["estado"]="disponivel"
    mesa_saida["lugares_ocupados"]=0
    mesa_saida["preço_pagar"]=0
    mesa_saida["produtos_mesa"]={}
    print("Saida concluida.")