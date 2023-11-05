from time import sleep
import tkinter as tk

cor4 = {'azul': '\033[0:34m',
        'amarelo': '\033[1:33m',
        'roxo': '\033[1:35m',
        'azul2': '\033[1:34m'}

def numerar_cpf(cpf):
    cpf_numerado = []
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)
    return cpf_numerado

def verificar_quantidade(cpf):
    return len(cpf) == 11

def calcular_primeiro_digito(cpf_numerado):
    if len(cpf_numerado) == 11:
        acumulador = 0
        controlador = 10
        for numeros in cpf_numerado[0:9]:
            resultado = numeros * controlador
            acumulador += resultado
            controlador = controlador - 1
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0
        return acumulador == cpf_numerado[9]
    return False

def calcular_segundo_digito(cpf_numerado):
    if len(cpf_numerado) == 11:
        acumulador2 = 0
        controlador2 = 11
        for numeros2 in cpf_numerado[0:10]:
            resultado2 = numeros2 * controlador2
            acumulador2 += resultado2
            controlador2 = controlador2 - 1
        acumulador2 = acumulador2 * 10 % 11
        if acumulador2 == 10:
            acumulador2 = 0
        return acumulador2 == cpf_numerado[10]
    return False

def analisar_cpf():
    cpf = entry_cpf.get().replace('.', '').replace('-', '')
    label_analise.config(text="ANALISANDO ...")
    janela.update()
    sleep(3)
    cpf_numerado = numerar_cpf(cpf)

    if verificar_quantidade(cpf) and calcular_primeiro_digito(cpf_numerado) and calcular_segundo_digito(cpf_numerado):
        label_resultado.config(text="Maravilha, o seu CPF é válido")
        label_resultado1.config(text="FECHE A JANELA PARA CONTINUAR")
    else:
        label_resultado.config(text="Poxa que pena, infelizmente seu CPF não é válido")

# Criar a interface gráfica usando Tkinter
janela = tk.Tk()
janela.title("Análise de CPF")

label_cpf = tk.Label(janela, text="Digite o seu CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(janela)
entry_cpf.pack()

button_analisar = tk.Button(janela, text="Analisar CPF", command=analisar_cpf)
button_analisar.pack()

label_analise = tk.Label(janela, text="")
label_analise.pack()

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

label_resultado1 = tk.Label(janela, text="")
label_resultado1.pack()

label_carregando = tk.Label(janela, text="")
label_carregando.pack()



janela.mainloop()
