Notas={"aluno1":{"PT":"","ING":"","AI":"","TIC":""},"aluno2":{"PT":"","ING":"","AI":"","TIC":""}}
for i in Notas.keys():
    Notas[i]["PT"]=int(input("Digite a sua nota de português"))
    Notas[i]["ING"]=int(input("Digite a sua nota de inglês"))
    Notas[i]["AI"]=int(input("Digite a sua nota de area de integração"))
    Notas[i]["TIC"]=int(input("Digite a sua nota de TIC"))
soma=0
for i in Notas["aluno1"].keys():
    soma=Notas["aluno1"][i]+soma
media=soma/4
Notas["aluno1"]["media"]=media
soma=0
for i in Notas["aluno2"].keys():
    soma=Notas["aluno2"][i]+soma
media2=soma/4
Notas["aluno2"]["media"]=media2

for chaves,valores in Notas["aluno1"].items():
    print(f"{chaves}->{valores}")
for chaves,valores in Notas["aluno2"].items():
    print(f"{chaves}->{valores}")

mediam=(media+media2)/2
print(f"A media dos alunos é {mediam}")