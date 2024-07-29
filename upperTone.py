"""
Para rodar este código fora do executável através do próprio python é necessário instalar o docx
pip install python-docx
"""
import tkinter as tk
from tkinter import filedialog
import os
import re
from docx import Document

class FileManager:
    file_path = ""
    arquivo_nome = ""

class nmbr_tones:
    nmbr_of_tones = ""

class Screen:
    def __init__(self, master):
        self.Screen = master
        self.botao_clicado = False 

        self.Screen.title("Editor de Notas")
        self.Screen.geometry("400x200")
        self.Screen.grid_columnconfigure(0, weight=1)
        self.Screen.grid_rowconfigure(0, weight=1)

        self.frame_principal = tk.Frame(self.Screen)
        self.frame_principal.grid(sticky="nsew")
        self.frame_principal.grid_columnconfigure(0, weight=1)
        self.frame_principal.grid_rowconfigure(0, weight=1)

        self.barra_menu = tk.Menu(self.Screen)
        self.Screen.config(menu=self.barra_menu)

        self.barra_menu.add_command(label="Ler arquivo", command=self.readFile)

        # Labels e Entry para ler quantidade de tons
        self.lb_qntd_tons = tk.Label(self.frame_principal, text="Quantidade de tons que vai subir: ")
        self.lb_qntd_tons.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.qntd_entry = tk.Entry(self.frame_principal)
        self.qntd_entry.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.btn_get_quantity = tk.Button(self.frame_principal, text="Obter Quantidade", command=self.get_quantity)
        self.btn_get_quantity.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.btn_salvar = tk.Button(self.frame_principal, text="Salvar e Fechar", command=self.save_and_close)
        self.btn_salvar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
    def readFile(self):
        self.arquivo = filedialog.askopenfile(mode="rb", initialdir="/Desktop", title="Selecione um arquivo", filetypes=(("Arquivos do Word", "*.doc *.docx"), ("Arquivos do WordPad", "*.rtf"), ("Todos os arquivos", "*.*")))
        if self.arquivo:
            FileManager.file_path = self.arquivo.name  # Atualiza o caminho do arquivo
            FileManager.arquivo_nome = os.path.basename(self.arquivo.name)
            print(f"Caminho do arquivo: {FileManager.file_path}")
            self.arquivo.close()

    # funcao para saber a quantidade de tons que deseja subir 
    def get_quantity(self):
        self.botao_clicado = True
        print("Método obterQuantidade chamado")  
        quantity = self.qntd_entry.get()
        print(f"Quantidade de tons que vai subir: {quantity}")
        nmbr_tones.nmbr_of_tones = quantity

    # Seleciona onde salvar o arquivo e depois encerra a execução
    def save_and_close(self):
        if not nmbr_tones.nmbr_of_tones:
            print("Quantidade de tons não definida.")
            return

        self.arquivo_salvar = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=(("Documentos Word", "*.docx"), ("Todos os arquivos", "*.*")))
        if self.arquivo_salvar:
            caminho_saida = self.arquivo_salvar
            self.Screen.quit()  # Fecha a janela principal
            main(caminho_saida)

    # dep 
    def verificarClique(self):
        if self.botao_clicado and nmbr_tones.nmbr_of_tones != "":
            print("O botão foi clicado e a quantidade de tons foi definida.")
            self.Screen.quit()  # Fecha a janela principal

# faz a subida de nota por nota. 
def up_tone(nota, semitons):
    notas = ["DO", "DO#", "RE", "RE#", "MI", "FA", "FA#", "SOL", "SOL#", "LA", "LA#", "SI"]
    if nota not in notas:
        return nota  # Se a nota não estiver na lista, retorna a nota original (para tratamento de erros)
    index = notas.index(nota)
    new_index = (index + semitons) % len(notas)
    return notas[new_index]

# le o arquivo, sua extensao e caminho 
def read_file(file_path):
    extension = os.path.splitext(file_path)[1].lower()
    linhas = []
    
    try:
        if extension == '.txt':
            with open(file_path, 'r') as file:
                conteudo = file.readlines()  # lê o arquivo linha por linha
        elif extension == '.docx':
            doc = Document(file_path)
            conteudo = [para.text for para in doc.paragraphs]
        else:
            print(f"Extensão de arquivo {extension} não suportada.")
            return []

        for linha in conteudo:
            # regex para separar por espaços ou hífens que não estão no meio das notas
            notas_linha = re.findall(r'[A-Z]+#?', linha.strip().upper())
            delimitadores = re.split(r'[A-Z]+#?', linha.strip().upper())
            linhas.append((notas_linha, delimitadores))
        return linhas
    except FileNotFoundError:
        print(f"Arquivo {file_path} não encontrado.")
        return []

# processa nota por nota, mantendo a formatação do arquivo, como nome, linhas, separação de notas, etc
def process_notes(linhas, semitons):
    new_rows = []
    for notas, delimitadores in linhas:
        notas_modificadas = [up_tone(nota, semitons) for nota in notas]
        nova_linha = ''
        for i in range(len(notas_modificadas)):
            nova_linha += delimitadores[i] + notas_modificadas[i]
        nova_linha += delimitadores[-1]  # Adiciona o último delimitador
        new_rows.append(nova_linha)
    return new_rows


# salva o arquivo no path que o usuário escolhe 
def save_file(file_path, linhas):
    doc = Document()
    for linha in linhas:
        doc.add_paragraph(linha)
    doc.save(file_path)

# printa o resultado apos processamento das notas
def show_result(linhas):
    for linha in linhas:
        print(linha)

def main(caminho_saida):
    file_path = FileManager.file_path
    file_input_path = file_path  # Nome do arquivo de entrada (pode ser .txt ou .docx)
    
    # Verifica se a quantidade de tons foi definida
    if not nmbr_tones.nmbr_of_tones:
        print("Quantidade de tons não definida.")
        return
    
    try:
        semitones = int(nmbr_tones.nmbr_of_tones)
    except ValueError:
        print("Quantidade de tons inválida.")
        return

    # Le as notas do arquivo
    rows = read_file(file_input_path)
    
    if not rows:
        print("Nenhuma nota foi lida do arquivo.")
        return
    
    # Processa notas
    modified_notes = process_notes(rows, semitones)
    
    # Salva e exibe resultado
    save_file(caminho_saida, modified_notes)
    show_result(modified_notes)

if __name__ == "__main__":
    mainFrame = tk.Tk() # tela principal 
    screen_app = Screen(mainFrame)
    mainFrame.mainloop()
    screen_app.verificarClique()
