import tkinter as tk
from time import sleep

def iniciar_conversa():
    nome = entry_nome.get()
    label_resposta.config(text="MUITO PRAZER EM TE CONHECER, " + nome + ".")
    sleep(2)

def escolher_opcao():
    label_opcao.config(text="TUDO BEM COM O SR(a)?")
    sleep(2)

def responder(opcao):
    if opcao == 1:
        label_resposta_opcao.config(text="QUE BOM, EU ESTOU BEM TAMBÉM.")
    elif opcao == 2:
        label_resposta_opcao.config(text="QUE PENA, MAIS LOGO LOGO TUDO MELHORA.")
    else:
        label_resposta_opcao.config(text="OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
        sleep(3)

def iniciar_simulado():
    label_simulado.config(text="PARA CONTINUARMOS")
    label_opcao_simulado.config(text="VOU PRECISAR DE ALGUNS DADOS OK?")

def texto():
    label_simulado.config(text="ENTÃO VAMOS COMEÇAR!")
    label_carregando.config(text="FECHE A JANELA PARA CONTINUAR")

janela = tk.Tk()
janela.title("Bem-vindo à AUTORAIO")

cor = {'vermelho': '\033[1;31;40m'}

label1 = tk.Label(janela, text="SEJA BEM VINDO À AUTORAIO", fg="red")
label1.pack()

sleep(2)

cor1 = {'azul': '\033[0;34m', 'amarelo': '\033[1;33m', 'roxo': '\033[1;35m', 'azul2': '\033[1;34m'}

label2 = tk.Label(janela, text="OLÁ, ME CHAMO MARIA, COM QUEM EU FALO?")
label2.pack()

entry_nome = tk.Entry(janela)
entry_nome.pack()

btn_iniciar_conversa = tk.Button(janela, text="SEGUIR", command=iniciar_conversa)
btn_iniciar_conversa.pack()

label_resposta = tk.Label(janela, text="")
label_resposta.pack()

btn_escolher_opcao = tk.Button(janela, text="O PRAZER É TODO MEU!", command=escolher_opcao)
btn_escolher_opcao.pack()

label_opcao = tk.Label(janela, text="")
label_opcao.pack()

btn_resposta_opcao1 = tk.Button(janela, text="- ESTOU BEM SIM, E VOCÊ?", command=lambda: responder(1))
btn_resposta_opcao1.pack()

btn_resposta_opcao2 = tk.Button(janela, text="- NÃO ESTOU MUITO BEM.", command=lambda: responder(2))
btn_resposta_opcao2.pack()

label_resposta_opcao = tk.Label(janela, text="")
label_resposta_opcao.pack()

btn_iniciar_simulado = tk.Button(janela, text="SEGUIR COM O ATENDIMENTO", command=iniciar_simulado)
btn_iniciar_simulado.pack()

label_simulado = tk.Label(janela, text="")
label_simulado.pack()

label_opcao_simulado = tk.Label(janela, text="")
label_opcao_simulado.pack()

btn_texto = tk.Button(janela, text="OPA, SEM PROBLEMAS!", command=texto)
btn_texto.pack()

label_carregando = tk.Label(janela, text="")
label_carregando.pack()

janela.mainloop()
