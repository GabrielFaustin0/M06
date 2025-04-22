alunos=[
    {"nprocesso":123,"nome":"Maria","email":"maria@gmail.com"},
    {"nprocesso":124,"nome":"Joaquim","email":"joaquim@gmail.com"},
    {"nprocesso":125,"nome":"Antómio","email":"antonio@gmail.com"}
]
notas=[
    {"nprocesso":alunos[0],"notas":[10,11,12,13]},
    {"nprocesso":alunos[1],"notas":[10,15,8,14]}
]
for nota in notas:
    print(f"{nota["nprocesso"]["nome"]}->{nota["notas"]}")
del alunos[0]
for nota in notas:
    print(f"{nota["nprocesso"]["nome"]}->{nota["notas"]}")