import os 
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

# Dicionario
locais = {
    # chave : valor
    "imagens":[".png", ".jpg"],
    "planilhas":[".xlsx"],
    "pdfs":[".pdf"],
    "csv":[".csv"],
    "diversos":[".docx", ".pptx", ".zip"],
}

for arquivo in lista_arquivos:
    # 01.arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]: 
            if not os.path.exists(f"{caminho}/{pasta}"): 
                os.mkdir(f"{caminho}/{pasta}")    # se não existe criar a pasta
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") # renomeando arquivo