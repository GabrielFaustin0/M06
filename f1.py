'''
PSI - Módulo 6
Coleções - F1
'''
 
GrandePremios = [
    {"Número": 1, "Grande Prêmio": "Barém", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 2, "Grande Prêmio": "Arábia Saudita", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 3, "Grande Prêmio": "Austrália", "Vencedor": "Carlos Sainz Jr.", "Equipe": "Ferrari"},
    {"Número": 4, "Grande Prêmio": "Japão", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 5, "Grande Prêmio": "China", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 6, "Grande Prêmio": "Miami", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"},
    {"Número": 7, "Grande Prêmio": "Emília-Romanha", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 8, "Grande Prêmio": "Mônaco", "Vencedor": "Charles Leclerc", "Equipe": "Ferrari"},
    {"Número": 9, "Grande Prêmio": "Canadá", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 10, "Grande Prêmio": "Espanha", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 11, "Grande Prêmio": "Áustria", "Vencedor": "George Russell", "Equipe": "Mercedes"},
    {"Número": 12, "Grande Prêmio": "Grã-Bretanha", "Vencedor": "Lewis Hamilton", "Equipe": "Mercedes"},
    {"Número": 13, "Grande Prêmio": "Hungria", "Vencedor": "Oscar Piastri", "Equipe": "McLaren-Mercedes"},
    {"Número": 14, "Grande Prêmio": "Bélgica", "Vencedor": "Lewis Hamilton", "Equipe": "Mercedes"},
    {"Número": 15, "Grande Prêmio": "Países Baixos", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"},
    {"Número": 16, "Grande Prêmio": "Itália", "Vencedor": "Charles Leclerc", "Equipe": "Ferrari"},
    {"Número": 17, "Grande Prêmio": "Azerbaijão", "Vencedor": "Oscar Piastri", "Equipe": "McLaren-Mercedes"},
    {"Número": 18, "Grande Prêmio": "Singapura", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"},
    {"Número": 19, "Grande Prêmio": "Estados Unidos", "Vencedor": "Charles Leclerc", "Equipe": "Ferrari"},
    {"Número": 20, "Grande Prêmio": "Cidade do México", "Vencedor": "Carlos Sainz Jr.", "Equipe": "Ferrari"},
    {"Número": 21, "Grande Prêmio": "São Paulo", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 22, "Grande Prêmio": "Las Vegas", "Vencedor": "George Russell", "Equipe": "Mercedes"},
    {"Número": 23, "Grande Prêmio": "Catar", "Vencedor": "Max Verstappen", "Equipe": "Red Bull Racing-Honda RBPT"},
    {"Número": 24, "Grande Prêmio": "Abu Dhabi", "Vencedor": "Lando Norris", "Equipe": "McLaren-Mercedes"}
]

def procura(lista,campo,valor,devolver):
    for i in lista:
        if i[campo]==valor:
            print(i[devolver])

 
# Quem ganhou o GP do São Paulo

procura(GrandePremios,"Grande Prêmio","São Paulo","Vencedor")
 
# Quais os grandes prémios que ganhou a Ferrari
for i in GrandePremios:
    if i["Equipe"]=="Ferrari":
        print(i["Grande Prêmio"])
# Quais os Grande Prémios que um determinado piloto ganhou (escolha do utilizador)
escolha=input("Digite o nome do piloto")
for i in GrandePremios:
    if i["Vencedor"]==escolha:
        print(i["Grande Prêmio"])
# Lista de vencedores (só aparece uma vez)
sete=set()
for i in GrandePremios:
    sete.add(i["Vencedor"])
print(sete)
 
# Lista de construtores que ganharam provas (só aparece uma vez)
sete=set()
for i in GrandePremios:
    sete.add(i["Equipe"])
print(sete)
# Mostrar quantos grandes prémios ganhou cada um desses pilotos
pilotosv=[]
for gp in GrandePremios:
    pilotosv.append(gp["Vencedor"])
for nome in set(pilotosv):
    vitoria=pilotosv.count(nome)
    print(f"{nome}->{vitoria}")