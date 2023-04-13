import os
import shutil
dir_origem = "c:\\Users\\CLIENTE\\Downloads"
dir_destino = "c:\\Users\\CLIENTE\\Downloads\\copy"

lista_arq = os.listdir(dir_origem)
if os.path.exists(dir_destino):
    for nome_arq in lista_arq:
        nome, ext = os.path.splitext(nome_arq)
        if ext=='':
            continue
        if ext in ['.gif','.png','.jpg','.jpeg']:
             print(nome)
             print(ext)
             path1=dir_origem+"\\"+nome_arq 
             print(path1) 
             path2=dir_destino+"\\"+nome_arq 
             print(path2)
             shutil.copy(path1,path2)
else:
     
    print("Criando pasta"+dir_destino)
    os.makedirs(dir_destino)
    

          
           