import os
import time
import shutil
caminho  = r"C:\Users\evert\OneDrive\Desktop\pastateste"
#Aprendizado
"""arquivos = os.listdir(caminho)
names_foldesExtensao  = []


for i in arquivos:
    #print(os.path.splitext(i)[1]) Aqui consigo pegar somente as extensões

    names_foldesExtensao.append(os.path.splitext(i)[1])

print(names_foldesExtensao)

#Criação de pasta 
teste = os.path.join(caminho, "Pasta_zip")
os.mkdir(teste)


teste = os.makedirs(caminho, exist_ok=True)"""

#================================Código=========================


arquivos = os.listdir(caminho)# Me entrega um vetor dos arquivos dentro da pasta
extensoes = []
for i in arquivos:
    #print(os.path.splitext(i)[1])
    extensoes.append(os.path.splitext(i)[1])

#==Remover duplicatas=====

extensoes = list(set(extensoes))#Remover as duplicadas para a criação das pastas
extensoes = [item[1:] for item in extensoes] #Remover os pontos
extensoes = [elemento for elemento in extensoes if elemento] #Remover os espaços em branco



#Criação das pastas caso elas nao existam
for n in extensoes:
    if  os.path.exists(caminho + r"\Pasta" + f"_{n}"):
        break
    else:
        create = os.path.join(caminho, "Pasta" + f"_{n}")
        os.mkdir(create)



for i in arquivos:
    print(i)

    