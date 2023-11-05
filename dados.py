import tkinter as tk
from tkinter import Entry, Button, Label, StringVar, OptionMenu
from time import sleep

cor3 = {'azul':'\033[0:34m', 'amarelo':'\033[1:33m', 'roxo':'\033[1:35m', 'azul2':'\033[1:34m'}

def continuar():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    sexo = entry_sexo.get()
    data_nascimento = entry_data_nascimento.get()
    nome_mae = entry_nome_mae.get()
    nome_pai = entry_nome_pai.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()
    bairro = entry_bairro.get()
    num_casa = int(entry_num_casa.get())
    profissao = profissao_var.get()

    # Agora você pode processar os dados como desejar

    if profissao == "1":
        profissao = "ADMINISTRAÇÃO"
    elif profissao == "2":
        profissao = "APOSENTADO"
    # E assim por diante para as outras opções

    print('Nome:', nome)
    print('Idade:', idade)
    print('Sexo:', sexo)
    print('Data de Nascimento:', data_nascimento)
    print('Nome da Mãe:', nome_mae)
    print('Nome do Pai:', nome_pai)
    print('Telefone:', telefone)
    print('Endereço:', endereco)
    print('Bairro:', bairro)
    print('Número da Casa:', num_casa)
    print('Profissão:', profissao)

def texto():
    label_carregando.config(text="FECHE A JANELA PARA CONTINUAR")

    # Você pode continuar processando os dados como desejar

janela = tk.Tk()
janela.title("Cadastro de Pessoa")

label_nome = Label(janela, text="Digite o seu Nome Completo:")
label_nome.pack()
entry_nome = Entry(janela)
entry_nome.pack()

label_idade = Label(janela, text="Digite a sua Idade:")
label_idade.pack()
entry_idade = Entry(janela)
entry_idade.pack()

label_sexo = Label(janela, text="QUAL SEU GÊNERO? [M/F]:")
label_sexo.pack()
entry_sexo = Entry(janela)
entry_sexo.pack()

label_data_nascimento = Label(janela, text="Digite sua Data de Nascimento:")
label_data_nascimento.pack()
entry_data_nascimento = Entry(janela)
entry_data_nascimento.pack()

label_nome_mae = Label(janela, text="Digite o Nome da sua Mãe:")
label_nome_mae.pack()
entry_nome_mae = Entry(janela)
entry_nome_mae.pack()

label_nome_pai = Label(janela, text="Digite o Nome do seu Pai:")
label_nome_pai.pack()
entry_nome_pai = Entry(janela)
entry_nome_pai.pack()

label_telefone = Label(janela, text="Digite um Número para Contato (DDD):")
label_telefone.pack()
entry_telefone = Entry(janela)
entry_telefone.pack()

label_endereco = Label(janela, text="Digite o seu Endereço:")
label_endereco.pack()
entry_endereco = Entry(janela)
entry_endereco.pack()

label_bairro = Label(janela, text="Digite o Nome do seu Bairro:")
label_bairro.pack()
entry_bairro = Entry(janela)
entry_bairro.pack()

label_num_casa = Label(janela, text="Digite o Número da sua Casa:")
label_num_casa.pack()
entry_num_casa = Entry(janela)
entry_num_casa.pack()

label_profissao = Label(janela, text="QUAL A SUA PROFISSÃO:")
label_profissao.pack()

profissoes = ["ADMINISTRAÇÃO", "APOSENTADO", "ARTES E DESIGN", "CIÊNCIAS BIOLÓGICAS E DA TERRA",
             "CIÊNCIAS SOCIAIS E HUMANAS", "COMUNICAÇÃO E INFORMAÇÃO", "DESEMPREGADO",
             "ENGENHARIA E PRODUÇÃO", "SAÚDE E BEM-ESTAR", "SERVIDOR PÚBLICO", "TECNOLOGIA DA INFORMAÇÃO", "OUTROS"]

profissao_var = StringVar(janela)
profissao_var.set(profissoes[0])
profissao_menu = OptionMenu(janela, profissao_var, *profissoes)
profissao_menu.pack()

btn_continuar = Button(janela, text="Continuar", command=continuar)
btn_continuar.pack()

label_carregando = tk.Label(janela, text="FECHE A JANELA PARA CONTINUAR")
label_carregando.pack()

janela.mainloop()
