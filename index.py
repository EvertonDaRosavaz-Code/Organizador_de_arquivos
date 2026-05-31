import os
from pathlib import Path
from time import sleep

#===============================Código=========================
caminho  = Path(r"C:\Users\evert\OneDrive\Desktop\pastateste")
caminho_texto = str(caminho)
pasta = "teste" 
#Achei interresante tornar uma variavel caso eu queira que o nome da pasta seja diferente e assim poderiamos mudar ela de forma globalmente sem ter que alterar uma por uma 


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
    #Verificar se a pasta Pasta_(a extenção) existe

    if  os.path.exists(caminho_texto + r"\ " + f"{pasta}" + f"_{n}"):                      
        break
    else:
        create = os.path.join(caminho, f"{pasta}" + f"_{n}")
        os.mkdir(create)

print('Movendo para as pastas')
sleep(3)
#Proximo passo ja com as pastas criadas mover os arquivos para suas respectivas pastas
for item in caminho.iterdir():
    if item.is_file():
        pasta_destino = caminho / f"{pasta}_{item.suffix[1:]}"
        destino = pasta_destino / item.name
        item.rename(destino)
        
        