import utils,Livros,leitores
import os
from datetime import datetime,timedelta
#livro ({}),leitor ({}),data_emprestimo,data_devolução,estado
emprestimos=[]
def menuemprestimos():
    os.system("cls")
    op=0
    while op!=4:
        op=utils.Menu(["Emprestimos","Devoluções","Listar","Voltar"],"Menu de Empréstimos/Devoluções")
        if op==4:
            break
        if op==1:
            Emprestimo()
        if op==2:
            Devolucao()
        if op==3:
            listar()
def Emprestimo():
    novo={}
    print("Indique o livro a inprestar")
    livro_inprestar=Livros.pesquisar()
    if len(livro_inprestar)==0:
        print("tente novamente")
        return
    elif len(livro_inprestar)>1:
        Livros.Listar(livro_inprestar)
        id=utils.ler_numero_inteiro("intruduza o id do livro a inprestar: ")
        for livro in livro_inprestar:
            if livro["id"]==id:
                if livro["estado"]!="disponivel":
                    print("Esse livro está emprestado")
                return
            novo["livro"]=livro
            break
        if "livro" not in novo:
            print("O id indicado não existe")
            return
    else:
        if livro_inprestar[0]["estado"]!="disponivel":
            print("Esse livro já está emprestado.")
            return
        novo["livro"]=livro_inprestar[0]
    print("Indique o leitor para inprestar o livro")
    leitor_inprestar=leitores.Pesquisar()
    if len(leitor_inprestar)==0:
        print("tente novamente")
        return
    elif len(leitor_inprestar)>1:
        print("Leitores encontrados:")
        leitores.Listar(leitor_inprestar)
        id=utils.ler_numero_inteiro("Indique o id do leitor: ")
        for leitor in leitor_inprestar:
            if leitor["id"]==leitor:
                novo["leitor"]=leitor
                break
        if "leitor" not in novo:
            print("O id indicado não existe.")
    else:
        novo["leitor"]=leitor_inprestar[0]
    data_atual=datetime.now()
    data_entrega=data_atual+timedelta(days=30)
    str_data_atual=data_atual.strftime("%Y-%m-%d")
    str_data_entrega=data_entrega.strftime("%Y-%m-%d")
    novo["data_emprestimo"]=str_data_atual
    novo["data_devolução"]=str_data_entrega
    novo["estado"]=True
    emprestimos.append(novo)
    novo["livro"]["estado"]="emprestado"
    novo["livro"]["leitor"]=novo["leitor"]
    print("Emprestimo registado com sucsso")
    print(f"livro emprestado: {novo["livro"]}")
    print(f"Leitor: {novo['leitor']}")
def Devolucao():
    id_livro=utils.ler_numero_inteiro("Indique o id do livro a devolver: ")
    livro=Livros.getlivro(id_livro)
    if livro==None:
        print("Esse livro não está emprestado: ")
    if livro["estado"]!="emprestado":
        print("Esse livro não está emprestado")
    emprestimo_devolver=None
    for enprestimo in emprestimos:
        if enprestimo["livro"]==livro and enprestimo["estado"]==True:

            data_devolucao=enprestimo
        if emprestimo_devolver==None:
            print("Emprestimo não encontrado")
            return
        data_devolucao=emprestimo_devolver["data_devolução"]
        data_atual=datetime.now()
        idata_atual=int(data_atual.strftime("%Y%m%d"))
        idata_devolucao=int(datetime.strptime(data_devolucao,"%Y%m%d").strftime("%Y%m%d"))
        if idata_atual>idata_devolucao:
            print("Devolução de prazo")
            emprestimo_devolver["leitor"]["infracoes"]+="Entrega fora de prazo"
    livro["nr_emprestimos"]+=1
    livro["estado"]="disponivel"
    livro["leitor"]=None
    emprestimo_devolver["estado"]=False
    print("Devolução com sucesso")
def listar():
    op=utils.lerstr(1,"Listar[T]odos ou só por [c]oncluir")
    for emp in emprestimos:
        if op in "tT" or (op in "cC" and emp["estado"]==True):
            print(f"{emp["livro"]["titulo"]} {emp["leitor"]["nome"]} {emp["estado"]} ")