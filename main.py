from tkinter import Tk, Label, Entry, Button, Menu

class Application:
    def __init__(self):
        self.root = root
        self.setup_window()
        self.create_menu()
        root.mainloop()

    def setup_window(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="gray")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

        self.add_widgets()

    def create_menu(self):
        # Cria a barra de menu
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Cria o menu "Arquivo"
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Novo", command=self.novo_arquivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_arquivo)
        self.file_menu.add_command(label="Salvar", command=self.salvar_arquivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.root.quit)

        # Cria o menu "Editar"
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cortar", command=self.cortar)
        self.edit_menu.add_command(label="Copiar", command=self.copiar)
        self.edit_menu.add_command(label="Colar", command=self.colar)

    def add_widgets(self):
        # Adiciona um rótulo
        self.label = Label(self.root, text="Nome:", bg="gray")
        self.label.pack(pady=10)
        
        # Adiciona uma caixa de entrada de texto
        self.entry = Entry(self.root)
        self.entry.pack(pady=10)
        
        # Adiciona um botão
        self.button = Button(self.root, text="Salvar", command=self.save)
        self.button.pack(pady=10)

    def save(self):
        nome = self.entry.get()  # Obtém o texto digitado na caixa de entrada
        print(f"Nome do cliente: {nome}")

    def novo_arquivo(self):
        print("Novo arquivo criado.")

    def abrir_arquivo(self):
        print("Abrir arquivo.")

    def salvar_arquivo(self):
        print("Arquivo salvo.")

    def cortar(self):
        print("Cortar.")

    def copiar(self):
        print("Copiar.")

    def colar(self):
        print("Colar.")

# Inicializa a aplicação
if __name__ == "__main__":
    root = Tk()
    app = Application()

