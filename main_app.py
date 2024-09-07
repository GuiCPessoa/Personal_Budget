# Importações
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Cores
color0 = "#2e2d2b" # Preto
color1 = "#feffff" # Branco
color2 = "#4fa882" # Verde
color3 = "#38576b" # Valor
color4 = "#303d3d" # Letra
color5 = "#e06636" # Profit
color6 = "#038cfc" # Azul
color7 = "#3fbfb9" # Verde
color8 = "#263238" # + Verde
color9 = "#e9edf5" # + Verde
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







janela.mainloop()