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


#Configurando o label X________________________________________________________________
app_x =Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)  
app_x.place(x=25, y=10) #mover item dentro da janela
#Texto abaixo do X
app_x =Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)  
app_x.place(x=17, y=70) #mover item dentro da janela
#Pontuação
app_x_pontos=Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)  
app_x_pontos.place(x=80, y=20) #mover item dentro da janela



# Dois pontos separador________________________________________________________________
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






#Criando logica do app

jogador_1 = "X"
jogador_2 = "O" 

pontuacao_1 = 0
pontuacao_2 = 0

tabela = [['1','2','3'], ['4','5','6'], ['7', '8', '9']]

jogando = 'X'
joga = ''
contador = 0
contador_de_rodada = 0


def iniciar_jogo():
    b_jogar.place(x=800, y=350)
    #Controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar
        
        #comparando o valor recebido
        if i==str(1):
            
            
            #verificando se a posição esta vazia ou nao
            if  b_0['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(2):
            #verificando se a posição esta vazia ou nao
            if  b_1['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(3):
            #verificando se a posição esta vazia ou nao
            if  b_2['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(4):
            #verificando se a posição esta vazia ou nao
            if  b_3['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(5):
            #verificando se a posição esta vazia ou nao
            if  b_4['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(6):
            #verificando se a posição esta vazia ou nao
            if  b_5['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(7):
            #verificando se a posição esta vazia ou nao
            if  b_6['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(8):
            #verificando se a posição esta vazia ou nao
            if  b_7['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
        
        if i==str(9):
            
            
            #verificando se a posição esta vazia ou nao
            if  b_8['text']=='':
                #verificando quem esta jogando e assim definir a cor do simbolo 
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor =co8
                    
                #definindo a cor do  texto do  botao e marcar a posição da tabela com o valor do jogador atual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando
            
                
                #verificando quem vai estar jogando para trocar para o proximo jogar
                if jogando == 'X':
                    jogando = 'O'
                    joga ='Jogador 1'
                else:
                    jogando = 'X'
                    joga ='Jogador 2'
                #Incrementando o contador para a próxima rodada
                contador+=1
                
                
        #Quando o contador for maior ou igual a 5, verifica se houve algum vencedor, de acordo com os seguites padroes dentro da tabela
        
        if contador>=5:
            #linhas 
            if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                vencedor(jogando)
                
                
            #Colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                vencedor(jogando)
                
            #diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                vencedor(jogando)

            #empate
            if contador>=9:
                vencedor('Foi empate')               
    
    #Decidir o vencedor
    def vencedor(i):
        global tabela
        global pontuacao_1
        global pontuacao_2
        global contador_de_rodada
        global contador
        
        #bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_vencedor =Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)  
        app_vencedor.place(x=40, y=220)
        
        if i == 'Foi empate':
            app_vencedor['text'] = 'Empate'
            
        if i == 'X':
            pontuacao_2+=1
            app_o_pontos['text'] = pontuacao_2
            app_vencedor['text'] = 'Jogador 2 venceu' 
            
        if i == 'O':
            pontuacao_1+=1
            app_x_pontos['text'] = pontuacao_1
            app_vencedor['text'] = 'Jogador 1 venceu'   
            
        
            
        def start():
            
            #limpado os botoes caso ganhe
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''
            
            #bloqueando os botoes
            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'
            
            
            
            app_vencedor.destroy()
            b_jogar.destroy()
            
        ##CHAMA A FUNÇÃO START
        b_jogar = Button(frame_baixo, command=start, text='Proxima Rodada', height= 1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)  
        b_jogar.place(x=70, y=197) #mover item dentro da janela
        
        def fim_de_jogo():
            b_jogar.destroy()
            app_vencedor.destroy()
            
            
            terminar()

            if contador_de_rodada>=5:
                fim_de_jogo()
                
            else:
                contador_de_rodada+=1
                #reiniciando a tabela
                tabela = [['1','2','3'], ['4','5','6'], ['7', '8', '9']]
                contador = 0
            
            
   
    
    #Terminar o jogo atual
    def terminar():
        global tabela
        global contador_de_rodada
        global pontuacao_1
        global pontuacao_2
        global contador
        
        tabela = [['1','2','3'], ['4','5','6'], ['7', '8', '9']]
        contador_de_rodada = 0
        pontuacao_1 = 0 
        pontuacao_2 = 0
        contador = 0
        
        
        #bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_fim =Label(frame_baixo, text='Fim de Jogo', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)  
        app_fim.place(x=25, y=90)
        
        #Jogar novamente
        
        def jogar_novamente():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()
            
            
            #iniciando o jogo novamente
            iniciar_jogo()
            
            
        #jogar novamente
        b_jogar =Button(frame_baixo, command=jogar_novamente, text='Jogar Novamente', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)  
        b_jogar.place(x=80, y=197) #mover item dentro da janela
        
        
    
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
    b_0 =Button(frame_baixo,command=lambda:controlar('1'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_0.place(x=30, y=15) #mover item dentro da janela

    #linha 0 coluna 2
    b_1 =Button(frame_baixo,command=lambda:controlar('2'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_1.place(x=96, y=15) #mover item dentro da janela

    #linha 0 coluna 3
    b_2 =Button(frame_baixo,command=lambda:controlar('3'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_2.place(x=162, y=15) #mover item dentro da janela

    #linha 1 coluna 1
    b_3 =Button(frame_baixo,command=lambda:controlar('4'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_3.place(x=30, y=75) #mover item dentro da janela

    #linha 1 coluna 2
    b_4 =Button(frame_baixo,command=lambda:controlar('5'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_4.place(x=96, y=75) #mover item dentro da janela

    #linha 1 coluna 3
    b_5 =Button(frame_baixo,command=lambda:controlar('6'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_5.place(x=162, y=75) #mover item dentro da janela

    #linha 2 coluna 1
    b_6 =Button(frame_baixo,command=lambda:controlar('7'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_6.place(x=30, y=135) #mover item dentro da janela

    #linha 2 coluna 2
    b_7 =Button(frame_baixo,command=lambda:controlar('8'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_7.place(x=96, y=135) #mover item dentro da janela

    #linha  coluna 3
    b_8 =Button(frame_baixo,command=lambda:controlar('9'), text='', width=3, font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)  
    b_8.place(x=162, y=135) #mover item dentro da janela


##BOTAO JOGAR

b_jogar =Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)  
b_jogar.place(x=85, y=197) #mover item dentro da janela



janela.mainloop()

