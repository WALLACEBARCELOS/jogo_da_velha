import tkinter
from tkinter import *
from tkinter import ttk



#cores ------------------------------

co0 = "#FFFFFF" # branca 
co1 = "#333333" # preta pesado
co2 = "#fcc058" # laranja
co3 = "#38576c" #valor
co4 = "#3297a8" #azul
co5 = "#fff873" #amarelo
co6 = "#fcc058" #laranja
co7 = "#e85151" #vermelha
co8 = co4 # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b" #preta


#Criando janela principal
janela = Tk()
janela.title('')
janela.geometry('260x370')
janela.configure(bg=fundo)

#Dividindo a janela em dois frames

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

#Configurando o frame cima
#Configurando o label X
app_x =Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)  
app_x.place(x=25, y=10) #mover item dentro da janela
#Texto abaixo do X
app_x =Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)  
app_x.place(x=17, y=70) #mover item dentro da janela
#Pontuação
app_x_pontos=Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)  
app_x_pontos.place(x=30, y=20) #mover item dentro da janela



janela.mainloop()

