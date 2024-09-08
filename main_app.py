# Importações
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Função para calcular porcentagens (copiada do código anterior)
def calcular_porcentagens(renda_mensal):

    # Valores das porcentagens
    valor_necessidade = 50
    valor_gastos = 30
    valor_economias = 20

    # Obtendo as porcentagens
    obter_50_percent = (valor_necessidade / 100) * renda_mensal
    obter_30_percent = (valor_gastos / 100) * renda_mensal
    obter_20_percent = (valor_economias / 100) * renda_mensal

    # Retornando resultados
    return obter_50_percent, obter_30_percent, obter_20_percent


# Cores
color0 = "#2e2d2b"  # Preto
color1 = "#feffff"  # Branco
color2 = "#4fa882"  # Verde
color3 = "#38576b"  # Valor
color4 = "#303d3d"  # Letra
color5 = "#e06636"  # Profit
color6 = "#038cfc"  # Azul
color7 = "#3fbfb9"  # Verde
color8 = "#263238"  # + Verde
color9 = "#e9edf5"  # + Verde
color10 = "#6e8faf"
color11 = "#f2f4f2"

# Criando janela vazia e definindo parâmetros da Janela
janela = Tk()
janela.title("")
janela.geometry("250x400")
janela.configure(background=color1)
janela.resizable(width=FALSE, height=FALSE)

# Estilo da janela
style = ttk.Style(janela)
style.theme_use("clam")

# Frames cima
frameTop = Frame(janela, width=300, height=50, bg=color1, relief="flat")
frameTop.grid(row=0, column=0)

# Frames meio
frameMiddle = Frame(janela, width=300, height=90, bg=color1, relief="flat")
frameMiddle.grid(row=1, column=0)

# Frames baixo
frameDown = Frame(janela, width=300, height=290, bg=color9, relief="flat")
frameDown.grid(row=2, column=0)

# Logo APP
app_ = Label(frameTop, text="Orçamento", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=color1, fg=color4)
app_.place(x=0, y=0)

# Abrindo imagem
app_img = Image.open("Personal_Budget/assets/iconLogo.png")
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameTop, image=app_img, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=color1, fg=color4)
app_logo.place(x=160, y=0)

app_linha = Label(frameTop, width=295, relief=FLAT, anchor=NW, font=('Verdana 1'), bg=color3, fg=color1)
app_linha.place(x=0, y=47)

# Função para Calcular
def calcular():
    # Obtendo o valor total
    renda_mensal = float(e_valor.get())

    # Usando a função calcular_porcentagens para obter as porcentagens
    necessidades, gastos, economias = calcular_porcentagens(renda_mensal)

    # Exibindo resultados
    l_necessidades['text'] = ("R${:,.2f}".format(necessidades))
    l_gastos['text'] = ("R${:,.2f}".format(gastos))
    l_economias['text'] = ("R${:,.2f}".format(economias))


# Frame Middle
app_ = Label(frameMiddle, text="Entrada - Renda mensal: ", relief=FLAT, anchor=NW, font=('Ivy 10'), bg=color1, fg=color4)
app_.place(x=7, y=15)

e_valor = Entry(frameMiddle, width=10, font=('Ivy 14'), justify='center', relief='solid')
e_valor.place(x=10, y=40)

b_calcular = Button(frameMiddle, command=calcular, text='Calcular'.upper(), overrelief=RIDGE, anchor=NW, font=('Ivy 9'), bg=color1, fg=color0)
b_calcular.place(x=150, y=40)


# Frame Down
app_ = Label(frameDown, text="Seus números para economizar", relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=color3, fg=color1)
app_.place(x=0, y=0)

# Necessidades
l_total_necessidades = Label(frameDown, text="Necessidades:", relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=color9, fg=color0)
l_total_necessidades.place(x=10, y=40)

l_necessidades = Label(frameDown, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=color1, fg=color4)
l_necessidades.place(x=10, y=75)

# Gastos
l_total_gastos = Label(frameDown, text="Gastos:", relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=color9, fg=color0)
l_total_gastos.place(x=10, y=115)

l_gastos = Label(frameDown, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=color1, fg=color4)
l_gastos.place(x=10, y=145)

# Economias
l_total_economias = Label(frameDown, text="Economias:", relief=FLAT, width=35, anchor=NW, font=('Verdana 10'), bg=color9, fg=color0)
l_total_economias.place(x=10, y=185)

l_economias = Label(frameDown, relief=FLAT, width=22, anchor=NW, font=('Verdana 12'), bg=color1, fg=color4)
l_economias.place(x=10, y=215)

# Executando a janela
janela.mainloop()
