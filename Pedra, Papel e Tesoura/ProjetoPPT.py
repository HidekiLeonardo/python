import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

#cores--------------------------------
co0 = "#FFFFFF" #branca
co1 = "#333333" #cinza
co2 = "#fcc058" #laranja
co3 = "#fff873" #amarela
co4 = "#34eb3d" #verde
co5 = "#e85151" #vermelha
co6 = "#000000" #preto
fundo = '#525050'

#confirando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

#dividindo a janela
frame_cima = Frame(janela,width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando frame_cima
app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('Arial 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Arial 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)


app = Label(frame_cima, text=":", height=1, anchor='center', font=('Arial 30 bold'), bg=co1, fg=co0)
app.place(x=125, y=20)

app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Arial 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('Arial 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('Arial 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_pc = Label(frame_baixo, text="", height=1, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co0)
app_pc.place(x=190, y=10)

global voce
global pc
global rounds
global pontos_vc
global pontos_pc

pontos_vc = 0
pontos_pc = 0
rounds = 5

#funcao logica
def jogar(i):
    global rounds
    global pontos_vc
    global pontos_pc

    if rounds > 0:
        print(rounds)
        opcoes = ['pedra', 'papel', 'tesoura']
        pc = random.choice(opcoes)
        voce = i

        app_pc['text'] = pc.upper()
        app_pc['fg'] = co6

        #caso for igual
        if voce == 'pedra' and pc == 'pedra':
            print('EMPATE!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        elif voce == 'papel' and pc == 'papel':
            print('EMPATE!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3
        elif voce == 'tesoura' and pc == 'tesoura':
            print('EMPATE!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
            app_linha['bg'] = co3

        #caso vc ganhar
        elif voce == 'pedra' and pc == 'tesoura':
            print('GANHOU!')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_vc += 10

        elif voce == 'papel' and pc == 'pedra':
            print('GANHOU!')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_vc += 10

        elif voce == 'tesoura' and pc == 'papel':
            print('GANHOU!')
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0
            pontos_vc += 10

        #caso pc ganhar
        elif pc == 'tesoura' and voce == 'papel':
            print('PERDEU!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0
            pontos_pc += 10

        elif pc == 'papel' and voce == 'pedra':
            print('PERDEU!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0
            pontos_pc += 10

        elif pc == 'pedra' and voce == 'tesoura':
            print('PERDEU!')
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            app_linha['bg'] = co0
            pontos_pc += 10

        #atualizando a pontuacao
        app_1_pontos['text'] = pontos_vc
        app_2_pontos['text'] = pontos_pc

        #atualizando rounds
        rounds -= 1

    else:
        app_1_pontos['text'] = pontos_vc
        app_2_pontos['text'] = pontos_pc
        #chamando a funcao terminar
        fim()

#funcao iniciar
def iniciar():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('imagens/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Arial 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y =60)

    icon_2 = Image.open('imagens/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Arial 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y =60)

    icon_3 = Image.open('imagens/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Arial 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y =60)

#funcao terminar
def fim():
    global rounds
    global pontos_vc
    global pontos_pc

    #reiniciando
    pontos_pc = 0
    pontos_vc = 0
    rounds = 5

    #destruindo os botoes
    app_pc['text'] = ''
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    #vencedor
    jogador_vc = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])
    
    if jogador_vc > jogador_pc:
        app_vencedor = Label(frame_baixo, text="Parabéns, você ganhou!", height=1, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)
    elif jogador_pc > jogador_vc:
        app_vencedor = Label(frame_baixo, text="Infelizmente, você perdeu!", height=1, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text="Empate", height=1, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co6)
        app_vencedor.place(x=5, y=60)

    #jogar denovo
    def jogar_denovo():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()

        b_jogar_denovo.destroy()

        iniciar()

    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=30, text='JOGAR DENOVO', compound=CENTER, bg=co1, fg=co0, font=('Arial 10 bold'), anchor=CENTER, relief=FLAT, overrelief=FLAT)
    b_jogar_denovo.place(x=5, y=151)

b_jogar = Button(frame_baixo, command=iniciar, width=30, text='JOGAR', compound=CENTER, bg=co1, fg=co0, font=('Arial 10 bold'), anchor=CENTER, relief=FLAT, overrelief=FLAT)
b_jogar.place(x=5, y=151)



janela.mainloop()