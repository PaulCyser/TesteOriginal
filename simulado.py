import tkinter as tk
from tkinter import Entry, Label, Button, messagebox


def calcular_simulacao():
    valor_veiculo = float(entry_valor_veiculo.get())
    quantidade_veiculos = int(entry_quantidade.get())
    valor_entrada = float(entry_entrada.get())
    parcelas = int(entry_parcelas.get())

    if parcelas <= 32:
        juros = 0.10
    elif 33 <= parcelas <= 64:
        juros = 0.15
    else:
        juros = 0.30

    total_com_juros = valor_veiculo * quantidade_veiculos * (1 + juros)
    desconto_entrada = total_com_juros - valor_entrada
    parcela = total_com_juros / parcelas

    return total_com_juros, desconto_entrada, parcela


def calcular_aprovacao():
    salario = float(entry_salario.get())
    total_com_juros, desconto_entrada, parcela = calcular_simulacao()
    prestacao_maxima = salario * 0.3

    if parcela <= prestacao_maxima:
        resultado = "PARABENS! SEU VEICULO FOI APROVADO"
    else:
        resultado = "SINTO MUITO! SEU VEICULO FOI REPROVADO"

    messagebox.showinfo("Resultado", f"Preço do Veículo com Juros: R${total_com_juros:.2f}\n"
                                     f"Desconto da Entrada: R${desconto_entrada:.2f}\n"
                                     f"Valor da Parcela: R${parcela:.2f}\n"
                                     f"Resultado: {resultado}")


janela = tk.Tk()
janela.title("Simulador de Aprovação de Carro")
janela.geometry("400x400")

frame_principal = tk.Frame(janela)
frame_principal.pack()

label_valor_veiculo = Label(frame_principal, text="Valor do Veículo:")
label_valor_veiculo.pack()

entry_valor_veiculo = Entry(frame_principal)
entry_valor_veiculo.pack()

label_quantidade = Label(frame_principal, text="Quantidade de Veículos:")
label_quantidade.pack()

entry_quantidade = Entry(frame_principal)
entry_quantidade.pack()

label_entrada = Label(frame_principal, text="Valor da Entrada:")
label_entrada.pack()

entry_entrada = Entry(frame_principal)
entry_entrada.pack()

label_parcelas = Label(frame_principal, text="Número de Parcelas:")
label_parcelas.pack()

entry_parcelas = Entry(frame_principal)
entry_parcelas.pack()

label_salario = Label(frame_principal, text="Salário Mensal:")
label_salario.pack()

entry_salario = Entry(frame_principal)
entry_salario.pack()

button_calcular_aprovacao = Button(frame_principal, text="Calcular Aprovação", command=calcular_aprovacao)
button_calcular_aprovacao.pack()

button_calcular_simulacao = Button(frame_principal, text="DEPOIS DA APROVAÇÃO FECHE A JANELA PARA CONTINUAR", command=calcular_simulacao)
button_calcular_simulacao.pack()

janela.mainloop()
