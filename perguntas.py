import tkinter as tk
from tkinter import Label, StringVar, IntVar, OptionMenu

def mostrar_resultado():
    nome = entry_nome.get()
    tem_casa = tem_casa_var.get()
    tem_carro = tem_carro_var.get()
    tem_moto = tem_moto_var.get()
    banco = banco_var.get()

    resultado = f"Olá, {nome}!\n"

    if tem_casa:
        resultado += "Você tem uma casa.\n"
    else:
        resultado += "Você não tem uma casa.\n"

    if tem_carro:
        resultado += "Você tem um carro.\n"
    else:
        resultado += "Você não tem um carro.\n"

    if tem_moto:
        resultado += "Você tem uma moto.\n"
    else:
        resultado += "Você não tem uma moto.\n"

    resultado += f"Você tem conta no banco {banco}.\n" \
                 f"FECHE A JANELA PARA CONTINUAR"

    label_resultado.config(text=resultado)

janela = tk.Tk()
janela.title("Perguntas ao Cliente")

label_nome = Label(janela, text="Digite novamente o seu nome?")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_casa = Label(janela, text="Você possui uma casa?")
label_casa.pack()
tem_casa_var = IntVar()
check_casa = tk.Checkbutton(janela, text="Sim", variable=tem_casa_var)
check_casa.pack()
check_nao_casa = tk.Checkbutton(janela, text="Não", variable=tem_casa_var, onvalue=0, offvalue=1)
check_nao_casa.pack()

label_carro = Label(janela, text="Você possui um carro?")
label_carro.pack()
tem_carro_var = IntVar()
check_carro = tk.Checkbutton(janela, text="Sim", variable=tem_carro_var)
check_carro.pack()
check_nao_carro = tk.Checkbutton(janela, text="Não", variable=tem_carro_var, onvalue=0, offvalue=1)
check_nao_carro.pack()

label_moto = Label(janela, text="Você possui uma moto?")
label_moto.pack()
tem_moto_var = IntVar()
check_moto = tk.Checkbutton(janela, text="Sim", variable=tem_moto_var)
check_moto.pack()
check_nao_moto = tk.Checkbutton(janela, text="Não", variable=tem_moto_var, onvalue=0, offvalue=1)
check_nao_moto.pack()

label_banco = Label(janela, text="Em qual banco você tem conta?")
label_banco.pack()
bancos = ["Banco do Brasil", "Bradesco", "Caixa", "Itau", "Safra", "Santander", "Outro"]
banco_var = StringVar()
banco_var.set(bancos[0])  # Valor padrão
banco_menu = OptionMenu(janela, banco_var, *bancos)
banco_menu.pack()

btn_enviar = tk.Button(janela, text="Enviar", command=mostrar_resultado)
btn_enviar.pack()

label_resultado = Label(janela, text="")
label_resultado.pack()

janela.mainloop()
