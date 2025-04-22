alunos=[
    {"nprocesso":123,"nome":"Maria","email":"maria@gmail.com"},
    {"nprocesso":124,"nome":"Joaquim","email":"joaquim@gmail.com"},
    {"nprocesso":125,"nome":"Antómio","email":"antonio@gmail.com"}
]
notas=[
    {"nprocesso":123,"notas":[10,11,12,13]},
    {"nprocesso":124,"notas":[10,15,8,14]}
]
for i in notas:
    for k in alunos:
        if i["nprocesso"]==k["nprocesso"]:
            print(f"{k["nome"]}->{i["notas"]}")