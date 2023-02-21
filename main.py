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

##Configurando o frame cima


#Configurando o label X
app_x =Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)  
app_x.place(x=25, y=10) #mover item dentro da janela
#Texto abaixo do X
app_x =Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)  
app_x.place(x=17, y=70) #mover item dentro da janela
#Pontuação
app_x_pontos=Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)  
app_x_pontos.place(x=80, y=20) #mover item dentro da janela



# Dois pontos separador
app_separador =Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)  
app_separador.place(x=110, y=20) #mover item dentro da janela



#Configurando o label 0
app_o =Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)  
app_o.place(x=170, y=10) #mover item dentro da janela
#Texto abaixo do X
app_o =Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)  
app_o.place(x=165, y=70) #mover item dentro da janela
#Pontuação
app_o_pontos=Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)  
app_o_pontos.place(x=130, y=20) #mover item dentro da janela



##Configurando o frame baixo

#criando linhas verticais
app_ =Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)  
app_.place(x=90, y=15) #mover item dentro da janela
app_ =Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)  
app_.place(x=157, y=15) #mover item dentro da janela

#criando linhas horizontais
app_ =Label(frame_baixo, text=' ', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)  
app_.place(x=30, y=63) #mover item dentro da janela
app_ =Label(frame_baixo, text=' ', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)  
app_.place(x=30, y=127) #mover item dentro da janela


##CRIANDO BOTÃO

#linha 0 coluna 1
b_0 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_0.place(x=30, y=15) #mover item dentro da janela

#linha 0 coluna 2
b_1 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_1.place(x=96, y=15) #mover item dentro da janela

#linha 0 coluna 3
b_2 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_2.place(x=162, y=15) #mover item dentro da janela

#linha 1 coluna 1
b_3 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_3.place(x=30, y=75) #mover item dentro da janela

#linha 1 coluna 2
b_4 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_4.place(x=96, y=75) #mover item dentro da janela

#linha 1 coluna 3
b_5 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_5.place(x=162, y=75) #mover item dentro da janela

#linha 2 coluna 1
b_6 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_6.place(x=30, y=135) #mover item dentro da janela

#linha 2 coluna 2
b_7 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_7.place(x=96, y=135) #mover item dentro da janela

#linha  coluna 3
b_8 =Button(frame_baixo, text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
b_8.place(x=162, y=135) #mover item dentro da janela


##BOTAO JOGAR

b_jogar =Button(frame_baixo, text='Jogar', width=10, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)  
b_jogar.place(x=85, y=210) #mover item dentro da janela



janela.mainloop()

