"""
Trabalho Modelo - Módulo6
Um programa para gerir livros e empréstimos de uma biblioteca Requesitos foncionais:
-Gestão de livros(CRUD)
-Gestão de leitores(CRUD)
-Emprestimos e devoluções
-Estatisticas(emprestimos em atraso, top livros, top mês, top leitores, ...)
"""
import utils,Livros,leitores,emprestimos,os,estastisticas
DEBUG=True
def MenuPrincipal():
    if DEBUG:
        Livros.configurar()
        leitores.Configurar()
    op=0
    while op!=5:
        os.system("cls")
        op=utils.Menu(["Livros","Leitores","Empréstimos/devoluções","Estatísticas","Sair"],"Menu principal")
        if op==5:
            break
        if op==1:
            Livros.menulivros()
        if op==2:
            leitores.MenuLeitores()
        if op==3:
            emprestimos.menuemprestimos()
        if op==4:
            estastisticas.menuestatisticas()
if __name__=="__main__":
    MenuPrincipal()