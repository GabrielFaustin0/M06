import utils,emprestimos
from datetime import datetime
def menuestatisticas():
    op=0
    while op!=5:
        op=utils.Menu(["livro mais requesitado","leitor com mais requesições","emprestimos fora de prazo","top dos meses","voltar"],"voltar")
        if op==5:
            break
        if op==1:
            livromais()
        if op==2:
            leitormais
        if op==3:
            emprestimoforadepraso()
        if op==4:
            mesmais()
def livromais():
    """Função para encontrar o livro mais requisitado no último mês (mês anterior ao mês atual)"""
    if len(emprestimos.emprestimos) == 0:
        print("Não tem empréstimos")
        return
    #mês e ano a pesquisar
    data_atual = datetime.now()
    data_atual.strftime("%Y-%m-%d")
    partes = data_atual.split("-")
    ano = int(partes[0])
    mes = int(partes[1])
    mes = mes - 1
    if mes == 0:
        mes = 12
        ano = ano - 1
   
    #criar um dicionário { titulo: contagem}
    dicionario_livros={}
    #percorrer empréstimos
    for emprestimo in emprestimos.emprestimos:
        #verificar se é do mês anterior (comparar mês e ano)
        data_emprestimo = emprestimo['data_emprestimo'].split("-")
        ano_emprestimo = int(data_emprestimo[0])
        mes_emprestimo = int(data_emprestimo[1])
        if ano_emprestimo == ano and mes_emprestimo == mes:
            #contar se sim
            if emprestimo['livro']['titulo'] in dicionario_livros:
                dicionario_livros[emprestimo['livro']['titulo']] += 1
            else:
                dicionario_livros[emprestimo['livro']['titulo']] = 1
    #percorrer o dicionário e encontrar o maior
    maior = 0
    titulo_maior =""
    for livro in dicionario_livros:
        if dicionario_livros[livro]>maior:
            titulo_maior = livro
            maior = dicionario_livros[livro]
    print(f"O livro mais emprestado no mês anterior ({mes}/{ano}) foi {titulo_maior} com {maior} empréstimos.")
def leitormais():
    if len(emprestimos.emprestimos)==0:
        print("Nao tem emprestimos")
        return
    lista_leitores={}
    for imprestimo in emprestimos.emprestimos:
        nome=imprestimo["leitor"]["nome"]
        if nome in lista_leitores:
            lista_leitores[nome]+=1
        else:
            lista_leitores[nome]=1
        nomemaior=""
        maior=0
        for leitor in lista_leitores:
            if lista_leitores[leitor]>maior:
                nomemaior=leitor
        print(nomemaior)
def emprestimoforadepraso():
    data_atual=datetime.now()
    idata_atual=int(data_atual.strftime("%Y%m%d"))
    for emprestimo in emprestimos.emprestimos:
        data_devoluçao=emprestimo["data_devolucao"]
        idata_devoluçao=int(datetime.strptime(data_devoluçao,"%Y-%m-%d").strftime("%Y%m%d"))
        if idata_atual>idata_devoluçao and emprestimo["estado"]==True:
            dias_atraso=idata_atual-idata_devoluçao
            print(f"O leitor {emprestimo["leitor"]["nome"]} tem o livro {emprestimo["livro"]["titulo"]} por entregar fora de prazo há {dias_atraso} dias.")
def mesmais():
    meses=[]
    for i in range(12):
        meses.append(0)
    for inprest in emprestimos.emprestimos:
        partes=inprest["data_emprestimo"].split("-")
        mes_emprestimo=int(partes[1])
        meses[mes_emprestimo]+=1
        posicaomaior=0
        for i in range(len(meses)):
            if meses[i]>meses[posicaomaior]:
                posicaomaior=i
        print(f"O mês que tem mais emprestimos é {posicaomaior+1}")