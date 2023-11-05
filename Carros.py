import pyodbc
import pandas as pd
import tkinter as tk
from time import sleep

# Configuração da conexão com o SQL Server
server = 'PCMC0310\SQLEXPRESS'
database = 'AutoRaio'

# Função para ler os carros do SQL Server com base na marca selecionada
def mostrar_carros_por_marca():
    marca_selecionada = instrucoes_var.get()

    # Conectar-se ao banco de dados SQL Server
    conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};')
    cursor = conn.cursor()

    label_resultado.config(text=f"CARREGANDO OS CARROS DISPONÍVEIS PARA {marca_selecionada} ...")
    janela.update()
    sleep(2)

    # Consulta SQL para selecionar os carros com base na marca
    sql_query = "SELECT Nome_Carro, Preco, Ano FROM Carros_Table WHERE Marca = ?"
    cursor.execute(sql_query, marca_selecionada)

    carros_disponiveis = cursor.fetchall()
    label_resultado.config(text=f"ESTES SÃO OS CARROS QUE TEMOS DISPONÍVEIS PARA {marca_selecionada}:")

    # Use pandas para exibir os dados em uma tabela
    df = pd.DataFrame(carros_disponiveis, columns=['Nome_Carro'])
    df_str = df.to_string(index=False)

    label_carros_disponiveis = tk.Label(janela, text=df_str, justify="left")
    label_carros_disponiveis.pack()

    # Fechar a conexão com o banco de dados
    cursor.close()
    conn.close()

janela = tk.Tk()
janela.title("Escolha de Carros")

label_instrucoes = tk.Label(janela, text="SELECIONE A MARCA DO CARRO DESEJADO")
label_instrucoes.pack()

instrucoes = ["AUDI", "CHEVROLET", "CITROËN", "FIAT", "FORD", "HONDA", "HYUNDAI", "PEUGEOT", "RENAULT", "TOYOTA", "VOLKSWAGEN"]
instrucoes_var = tk.StringVar(janela)
instrucoes_var.set(instrucoes[0])

instrucoes_menu = tk.OptionMenu(janela, instrucoes_var, *instrucoes)
instrucoes_menu.pack()

button_analisar = tk.Button(janela, text="Verificar Carros Disponíveis por Marca", command=mostrar_carros_por_marca)
button_analisar.pack()

label_resultado = tk.Label(janela, text="Lembre-se do preço e feche a janela para continuar")
label_resultado.pack()

janela.mainloop()
