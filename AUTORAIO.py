# saudacao.py
import tkinter as tk

class AUTORAIO:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.label = tk.Label(root, text="Bem-vindo!")
        self.label.pack()

        # Botão "Próxima"
        self.next_button = tk.Button(root, text="Próxima", command=self.controller.mostrar_validacpf)
        self.next_button.pack()

        # Botão "Pular" para a próxima interface (no exemplo, "validacpf")
        self.skip_button = tk.Button(root, text="Pular", command=self.controller.mostrar_validacpf)
        self.skip_button.pack()

# Restante do código

# ValidaCPF, Dados, Carros, Pergunta2, Simulado, Dialogo e Dialogo2 seguem o mesmo padrão de saudacao.py.

# main.py
import tkinter as tk

from saudação import iniciar_conversa
from validacpf import numerar_cpf
from dados import continuar
from Carros import mostrar_carros_por_marca
from perguntas import mostrar_resultado
from simulado import calcular_simulacao
from dialogo import SimuladorAtendimento
#from dialogo2 import Dialogo2


class MainController:
    def __init__(self, root):
        self.root = root
        self.show_saudacao()

    def show_saudacao(self):
        self.clear_frame()
        self.current_interface = iniciar_conversa(self.root, self)

    def show_validacpf(self):
        self.clear_frame()
        self.current_interface = numerar_cpf(self.root, self)

    def show_dados(self):
        self.clear_frame()
        self.current_interface = continuar(self.root, self)

    def show_carros(self):
        self.clear_frame()
        self.current_interface = mostrar_carros_por_marca(self.root, self)

    def show_pergunta(self):
        self.clear_frame()
        self.current_interface = mostrar_resultado(self.root, self)

    def show_simulado(self):
        self.clear_frame()
        self.current_interface = calcular_simulacao(self.root, self)

    def show_dialogo(self):
        self.clear_frame()
        self.current_interface = SimuladorAtendimento(self.root, self)

    #def show_dialogo2(self):
        #self.clear_frame()
        #self.current_interface = Dialogo2(self.root, self)

    def clear_frame(self):
        if hasattr(self, 'current_interface'):
            self.current_interface.root.destroy()


root = tk.Tk()
app = MainController(root)
root.mainloop()
