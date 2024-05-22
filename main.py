import tkinter as tk
from tkinter import ttk

def criar_campos(num_campos):
    try:
        global entrada_widgets
        num_campos = int(num_campos)
        num_colunas = min(10, (num_campos + 9) // 10)  # Define o número de colunas baseado no número de pessoas

        for widget in entrada_widgets:
            widget.destroy()  # Limpa os campos anteriores

        entrada_widgets.clear()  # Limpa a lista de widgets

        for i in range(num_campos):
            coluna = i % num_colunas
            linha = i // num_colunas

            entrada_var = tk.StringVar()
            entrada = ttk.Entry(frame_principal, textvariable=entrada_var, width=10)
            entrada.grid(row=linha, column=coluna, padx=5, pady=5)

            entrada_widgets.append(entrada)
    except ValueError:
        tk.messagebox.showerror("Erro", "Insira um valor válido para o número de pessoas.")

def ler_valores():
    try:
        valores_lidos = [int(entrada.get()) for entrada in entrada_widgets if entrada.get()]

        contagem_valores = {}
        for valor in valores_lidos:
            contagem_valores[valor] = contagem_valores.get(valor, 0) + 1

        contagens_ordenadas = sorted(contagem_valores.items(), key=lambda x: int(x[0]))

        resultados_texto = ""
        for valor, contagem in contagens_ordenadas:
            resultados_texto += f"{contagem} pessoas teve {valor}cm\n"

        faq = criar_faq(contagem_valores)

        percentil_menor = faq[-1] * 0.05
        percentil_medio = faq[-1] * 0.5
        percentil_superior = faq[-1] * 0.95

        resultados_janela = tk.Toplevel(root)
        resultados_janela.title("Resultados")

        faq_label = tk.Label(resultados_janela, text="Lista FAQ:")
        faq_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)
        faq_texto = "\n".join(str(valor) for valor in faq)
        faq_texto_label = tk.Label(resultados_janela, text=faq_texto)
        faq_texto_label.grid(row=1, column=0, sticky="w", padx=20, pady=5)

        contagem_label = tk.Label(resultados_janela, text="Contagem de Pessoas:")
        contagem_label.grid(row=0, column=1, sticky="w", padx=20, pady=10)
        contagem_texto = resultados_texto
        contagem_texto_label = tk.Label(resultados_janela, text=contagem_texto)
        contagem_texto_label.grid(row=1, column=1, sticky="w", padx=20, pady=5)

        percentis_label = tk.Label(resultados_janela, text="Percentis:")
        percentis_label.grid(row=0, column=2, sticky="w", padx=20, pady=10)
        percentis_texto = f"Percentil Menor: {percentil_menor:.2f}\nPercentil Médio: {percentil_medio:.2f}\nPercentil Superior: {percentil_superior:.2f}"
        percentis_texto_label = tk.Label(resultados_janela, text=percentis_texto)
        percentis_texto_label.grid(row=1, column=2, sticky="w", padx=20, pady=5)
    except ValueError:
        tk.messagebox.showerror("Erro", "Insira valores numéricos válidos para os campos.")

def criar_faq(contagem_valores):
    faq = []
    soma_acumulada = 0
    for _, contagem in sorted(contagem_valores.items()):
        soma_acumulada += contagem
        faq.append(soma_acumulada)
    return faq

# Cria uma instância da classe Tk, que representa a janela principal da aplicação
root = tk.Tk()

# Define o título da janela
root.title("Fisioterapia | Desenvolvido por Luan Bonfim")

# Obtém as dimensões da tela do dispositivo
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

# Define a geometria da janela para ocupar toda a tela do dispositivo
root.geometry(f"{largura_tela}x{altura_tela}")

# Rótulo grande para o título
titulo_label = ttk.Label(root, text="Fisioterapeuta Marya - FADAP", font=("Helvetica", 24))
titulo_label.pack(pady=20)

# Cria um rótulo com instruções para o usuário
instrucoes_label = ttk.Label(root, text="Insira o número de pessoas:")
instrucoes_label.pack(pady=20)

# Campo de entrada para o número de pessoas
num_pessoas_var = tk.StringVar()
num_pessoas_entry = ttk.Entry(root, textvariable=num_pessoas_var, width=10)
num_pessoas_entry.pack()

# Botão para criar os campos
criar_campos_button = ttk.Button(root, text="Criar Campos", command=lambda: criar_campos(num_pessoas_var.get()))
criar_campos_button.pack(pady=10)

# Frame principal para os campos de entrada
frame_principal = ttk.Frame(root)
frame_principal.pack(padx=20, pady=10)

# Lista para armazenar os widgets de entrada
entrada_widgets = []

# Botão para ler os valores e mostrar os resultados
ler_valores_button = ttk.Button(root, text="Ler Valores", command=ler_valores)
ler_valores_button.pack(pady=10)

# Rodapé
rodape_label = ttk.Label(root, text="Desenvolvido por Luan Bonfim - UNOESTE FIPP", font=("Helvetica", 10))
rodape_label.pack(pady=10)

# Inicia o loop principal da aplicação para que a janela seja exibida e responda às interações do usuário
root.mainloop()
