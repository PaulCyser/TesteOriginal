import tkinter as tk
from tkinter import messagebox


class SimuladorAtendimento:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Simulador de Atendimento")
        self.janela.geometry("400x400")

        self.frame = tk.Frame(self.janela)
        self.frame.pack()

        self.frases_atendente = [
            "Parabéns pela compra, Sr(a)!",
            "É uma sensação maravilhosa, não é?",
            "Estarei entrando em contato para agendarmos uma data",
            "Para acertarmos tudo e o Sr(a) retirar o seu veículo,",
            "mais uma vez agradeço a preferência",
            "Tenha um dia abençoado!"
        ]

        self.respostas_cliente = [
            "Obrigado!",
            "Com certeza, estou muito feliz!",
            "Ficarei aguardando o contato.",
            "Vou providenciar a documentação.",
            "Obrigado, vocês foram ótimos!",
            "Igualmente, tenha um ótimo dia!"
        ]

        self.frase_atual = 0
        self.label = tk.Label(self.frame, text=self.frases_atendente[self.frase_atual])
        self.label.pack()

        self.options = tk.StringVar(self.janela, value="")

        self.option_menu = tk.OptionMenu(self.janela, self.options, *self.respostas_cliente)
        self.option_menu.pack()

        self.button_responder = tk.Button(self.frame, text="Responder", command=self.exibir_resposta_cliente)
        self.button_proxima_frase = tk.Button(self.frame, text="Próxima", command=self.exibir_proxima_frase)

        self.perguntas_satisfacao = [
            "Qual foi o nível de satisfação com o atendimento? (Ruim, Regular, Bom, Muito Bom, Excelente)",
            "Você ficou satisfeito com o veículo adquirido? (Sim, Não)",
            "Você recomendaria nossa loja a outras pessoas? (Sim, Não)"
        ]

        self.respostas_satisfacao = []
        self.pergunta_satisfacao_atual = 0
        self.label_pergunta_satisfacao = tk.Label(self.frame,
                                                  text=self.perguntas_satisfacao[self.pergunta_satisfacao_atual])
        self.entry_resposta_satisfacao = tk.Entry(self.frame)
        self.button_proxima_pergunta_satisfacao = tk.Button(self.frame, text="Próxima pergunta",
                                                            command=self.registrar_resposta_satisfacao)

    def exibir_resposta_cliente(self):
        resposta_cliente = self.options.get()
        if resposta_cliente:
            self.label.config(text=resposta_cliente)
            self.button_responder.pack_forget()
            self.button_proxima_frase.pack()
            self.respostas_cliente[self.frase_atual] = resposta_cliente
        else:
            messagebox.showerror("Erro", "Por favor, selecione uma resposta.")

    def exibir_proxima_frase(self):
        if self.frase_atual < len(self.frases_atendente) - 1:
            self.frase_atual += 1
            self.label.config(text=self.frases_atendente[self.frase_atual])
            self.options.set("")  # Limpa a seleção
            self.button_responder.pack()
            self.button_proxima_frase.pack_forget()
        else:
            self.iniciar_pesquisa_satisfacao()

    def iniciar_pesquisa_satisfacao(self):
        self.label.config(text="Por favor, preencha a pesquisa de satisfação abaixo:")
        self.button_responder.pack_forget()
        self.button_proxima_frase.pack_forget()

        self.label_pergunta_satisfacao.pack()
        self.entry_resposta_satisfacao.pack()
        self.button_proxima_pergunta_satisfacao.pack()

    def registrar_resposta_satisfacao(self):
        resposta_satisfacao = self.entry_resposta_satisfacao.get()
        if resposta_satisfacao:
            self.respostas_satisfacao.append(resposta_satisfacao)
            self.entry_resposta_satisfacao.delete(0, tk.END)
            self.pergunta_satisfacao_atual += 1
            if self.pergunta_satisfacao_atual < len(self.perguntas_satisfacao):
                self.label_pergunta_satisfacao.config(text=self.perguntas_satisfacao[self.pergunta_satisfacao_atual])
            else:
                self.finalizar_pesquisa_satisfacao()
        else:
            messagebox.showerror("Erro", "Por favor, digite uma resposta.")

    def finalizar_pesquisa_satisfacao(self):
        self.label.config(text="AUTORAIO AGRADECE! TENHA UM ÓTIMO DIA!")
        self.label_pergunta_satisfacao.pack_forget()
        self.entry_resposta_satisfacao.pack_forget()
        self.button_proxima_pergunta_satisfacao.pack()
        self.exibir_resultados()

    def exibir_resultados(self):
        resultados = "\nRespostas do cliente:\n"
        for frase, resposta in zip(self.frases_atendente, self.respostas_cliente):
            resultados += f"{frase}\nCliente: {resposta}\n\n"
        resultados += "\nPerguntas de Satisfação:\n"
        for pergunta, resposta in zip(self.perguntas_satisfacao, self.respostas_satisfacao):
            resultados += f"{pergunta}\nResposta: {resposta}\n\n"

        messagebox.showinfo("Resultados da Pesquisa", resultados)

    def executar(self):
        self.button_responder.pack()
        self.janela.mainloop()


simulador = SimuladorAtendimento()
simulador.executar()
