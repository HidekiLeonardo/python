from tkinter import *
from tkinter import ttk

co0 = '#ffffff' #branco
co1 = '#0DA0FC' #azul claro
co2 = '#444466' #preto
co3 = '#4056FF' #azul escuro



janela = Tk()
janela.title('')
janela.geometry('320x255')
janela.configure(bg=co0)

#dividindo a janela
frame_cima = Frame(janela, width=320, height=55, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=320, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#frame_cima
app_nome = Label(frame_cima, text='Calculadora de IMC', width=24, height=1, relief='flat', anchor='center', font=('Arial 16 bold'), bg =co0, fg=co2)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=320, height=1, relief='flat', anchor='center', font=('Arial 1 bold'), bg =co3, fg=co0)
app_linha.place(x=0, y=36)

#logica
def calcular():
    peso = float(n_peso.get())
    altura = float(n_altura.get())

    imc = peso / altura**2
    resultado = imc

    if resultado < 18.5:
        l_resultado_text['text'] = 'Seu IMC: ABAIXO DO PESO'
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_text['text'] = 'Seu IMC: NORMAL'
    elif resultado >= 25 and resultado < 30:
        l_resultado_text['text'] = 'Seu IMC: SOBREPESO'
    else:
        l_resultado_text['text'] = 'Seu IMC: OBESIDADE'

    l_resultado['text'] = "{:.2f}".format(resultado)

#frame_baixo
app_peso = Label(frame_baixo, text='Insira seu peso(Kg):', height=1, padx=0, relief='flat', anchor='w', font=('Arial 10 bold'), bg =co0, fg=co2)
app_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

n_peso = Entry(frame_baixo,width=6, relief='solid', font=('Arial 10 bold'), justify='center')
n_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)


app_altura = Label(frame_baixo, text='Insira sua altura(m):', height=1, padx=0, relief='flat', anchor='w', font=('Arial 10 bold'), bg =co0, fg=co2)
app_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

n_altura = Entry(frame_baixo,width=6, relief='solid', font=('Arial 10 bold'), justify='center')
n_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Arial 23 bold'), bg =co3, fg=co0)
l_resultado.place(x=200, y=10)

l_resultado_text = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Arial 10 bold'), bg=co0, fg=co3)
l_resultado_text.place(x=3, y=85)


b_calcular = Button(frame_baixo, command=calcular, text='Calcular',width=37, height=1, overrelief=SOLID, relief='raised', anchor='s', font=('Arial 10 bold'), bg=co1, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=80, padx=5, columnspan=50)



janela.mainloop()