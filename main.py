# main.py

from tkinter import Tk, Label, Entry, Button, Menu, Canvas, Scrollbar, Frame
import dataBase  # Importa o arquivo dataBase.py onde está a função criar_tabela_alunos
import sqlite3  # Importa o módulo sqlite3 para trabalhar com o banco de dados

class Application:
    def __init__(self):
        self.root = Tk()
        self.setup_window()
        self.create_menu()
        self.create_scrollable_window()
        self.create_widgets()
        self.root.mainloop()

    def setup_window(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="gray")
        self.root.geometry("900x700")

    def create_menu(self):
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Sair", command=self.root.quit)

    def create_scrollable_window(self):
        # Cria um canvas para a janela principal com rolagem
        self.canvas = Canvas(self.root, bg="gray")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Adiciona uma barra de rolagem vertical para o canvas
        self.scrollbar = Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        # Conecta a barra de rolagem ao canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Cria um frame dentro do canvas para conter os widgets
        self.scrollable_frame = Frame(self.canvas, bg="gray")
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configura a scrollregion do canvas
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def create_widgets(self):
        # Adiciona widgets dentro do scrollable_frame
        self.label = Label(self.scrollable_frame, text="Nome:", bg="gray")
        self.label.pack(pady=10)

        self.entry_nome = Entry(self.scrollable_frame)
        self.entry_nome.pack(pady=10)

        self.label_data_nascimento = Label(self.scrollable_frame, text="Data de Nascimento:", bg="gray")
        self.label_data_nascimento.pack(pady=10)

        self.entry_data_nascimento = Entry(self.scrollable_frame)
        self.entry_data_nascimento.pack(pady=10)

        self.label_data_matricula = Label(self.scrollable_frame, text="Data de Matrícula:", bg="gray")
        self.label_data_matricula.pack(pady=10)

        self.entry_data_matricula = Entry(self.scrollable_frame)
        self.entry_data_matricula.pack(pady=10)

        self.label_filiacao_pai = Label(self.scrollable_frame, text="Filiação - Pai:", bg="gray")
        self.label_filiacao_pai.pack(pady=10)

        self.entry_filiacao_pai = Entry(self.scrollable_frame)
        self.entry_filiacao_pai.pack(pady=10)

        self.label_filiacao_mae = Label(self.scrollable_frame, text="Filiação - Mãe:", bg="gray")
        self.label_filiacao_mae.pack(pady=10)

        self.entry_filiacao_mae = Entry(self.scrollable_frame)
        self.entry_filiacao_mae.pack(pady=10)

        self.label_cpf = Label(self.scrollable_frame, text="CPF:", bg="gray")
        self.label_cpf.pack(pady=10)

        self.entry_cpf = Entry(self.scrollable_frame)
        self.entry_cpf.pack(pady=10)

        self.label_contato1 = Label(self.scrollable_frame, text="Contato 1:", bg="gray")
        self.label_contato1.pack(pady=10)

        self.entry_contato1 = Entry(self.scrollable_frame)
        self.entry_contato1.pack(pady=10)

        self.label_contato2 = Label(self.scrollable_frame, text="Contato 2:", bg="gray")
        self.label_contato2.pack(pady=10)

        self.entry_contato2 = Entry(self.scrollable_frame)
        self.entry_contato2.pack(pady=10)

        self.button = Button(self.scrollable_frame, text="Salvar", command=self.salvar_aluno)
        self.button.pack(pady=10)

    def salvar_aluno(self):
        nome = self.entry_nome.get()
        data_nascimento = self.entry_data_nascimento.get()
        data_matricula = self.entry_data_matricula.get()
        filiacao_pai = self.entry_filiacao_pai.get()
        filiacao_mae = self.entry_filiacao_mae.get()
        cpf = self.entry_cpf.get()
        contato1 = self.entry_contato1.get()
        contato2 = self.entry_contato2.get()

        # Conecta ao banco de dados
        conn = sqlite3.connect('alunos.db')
        cursor = conn.cursor()

        # Insere os dados na tabela
        cursor.execute('''
            INSERT INTO alunos (nome, data_nascimento, data_matricula, 
            filiacao_pai, filiacao_mae, cpf, contato1, contato2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, data_nascimento, data_matricula, filiacao_pai, filiacao_mae, cpf, contato1, contato2))

        # Salva as mudanças e fecha a conexão
        conn.commit()
        conn.close()

        # Limpa os campos após salvar
        self.entry_nome.delete(0, 'end')
        self.entry_data_nascimento.delete(0, 'end')
        self.entry_data_matricula.delete(0, 'end')
        self.entry_filiacao_pai.delete(0, 'end')
        self.entry_filiacao_mae.delete(0, 'end')
        self.entry_cpf.delete(0, 'end')
        self.entry_contato1.delete(0, 'end')
        self.entry_contato2.delete(0, 'end')

# Inicializa a aplicação
if __name__ == "__main__":
    app = Application()

