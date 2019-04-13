from cryptform import Cry
from tkinter import *
tk = Tk()
key = b'Ad81dpwP787wpmq8Aowq20dp871P0w1q' #aqui deixaremos a key, deverar ter 36caracteres, 36bytes
#####################funcoes extras###########
#servem para apagar o conteudo de algumas Entry
def dele(event):
    chat3.delete('0','end')
def dele1(event):
    entr1.delete('0','end')
def dele2(event):
    entr.delete('0','end')
#########################################
def sifra():#funcao de entrada de dados a ser criptografado e saida criptografada
    global key # declaremos a key como global
    chat.delete('0',"end")#deletemos qualquer conteudo que esteja no campo  referente
    chat2.delete('0',"end")#deletemos qualquer conteudo que esteja no campo  referente
    mensagem = entr.get().encode()#aqui é responsavel por pegar a mensagem a ser criptografada,e codificar pra tipo bytes
    teste = Cry()#iniciamos o objeto
    chat.insert(END,str(teste.encryp(mensagem, key)))#chamamos a funcao de criptografia, e passamos a mensagem e a key definida
    #na linha 4, e irar retorna a mensagem criptografada para o entry no layout(chat)
    chat2.insert(END,teste.iv_())#devolvemos o valor do iv para o entry no layout(chat2)

def decifrar():
    global key
    chat1.delete('0',"end")#deletemos qualquer conteudo que esteja no campo  referente
    mensagem1 = entr1.get()#Responsavel por pegar a mesagem criptografada
    iv = chat3.get()#Responsavel por pegar o IV da mensagem
    teste1 = Cry()#Inicializamos o objeto
    chat1.insert(END,str(teste1.descry(mensagem1,key,iv)))#chamamos a funcao de descriptografia, e passamos a mensagem,IV e a key definida
    #na linha 4, e irar retorna a mensagem descriptografada para o entry no layout(chat1)


######################################Funcoes do tkinter###########################################

#######entrada de msg##############
entr = Entry()
entr.grid(row=0,column=2)
entr.bind('<Button-1>', dele2)
#-------------------------------------#

entr1 = Entry()
entr1.grid(row=0,column=4)
entr1.bind('<Button-1>', dele1)
##############Botoes################
but1 = Button(text="Cifrar",command=sifra)
but1.grid(row=4,column=2)
#-------------------------------------#

but2 = Button(text="Decifrar",command=decifrar)
but2.grid(row=4,column=4)


################Entry's###############
chat = Entry()
chat.grid(row=1, column=2)
chat["bg"] ="green"
chat['fg'] = 'black'
#-------------------------------------#
chat1 = Entry()
chat1.grid(row=1, column=4)
chat1["bg"] ="green"
chat1['fg'] = 'black'
#-------------------------------------#

chat2 = Entry()
chat2.grid(row=2, column=2)
chat2["bg"] ="red"
chat2['fg'] = 'black'
chat2.insert(END,"Não digite aqui!!!")
#-------------------------------------#

chat3 = Entry()
chat3.grid(row=2, column=4)
chat3["bg"] ="red"
chat3['fg'] = 'black'
chat3.insert(END,"Digite o IV:")
chat3.bind('<Button-1>', dele)
############Labels###################
lb1 = Label(text="Entrada de dados:")
lb1.grid(row=0,column=0)
lb1['bg']="grey"
#-------------------------------------#

lb2 = Label(text="Mensagem Criptografada:")
lb2.grid(row=1,column=0)
lb2['bg']="grey"
#-------------------------------------#

lb3 = Label(text="Gerador do IV:")
lb3.grid(row=2,column=0)
lb3['bg']="grey"
#-------------------------------------#

lb4 = Label(text="Dados Criptografados:")
lb4.grid(row=0,column=3)
lb4['bg']="grey"
#-------------------------------------#

lb5 = Label(text="Mensagem Decifrada:")
lb5.grid(row=1,column=3)
lb5['bg']="grey"
#-------------------------------------#

lb6 = Label(text="Entrada do IV:")
lb6.grid(row=2,column=3)
lb6['bg']="grey"
#-------------------------------------#






tk.title("Cript/Descript")
tk.geometry("550x100")
tk['bg'] ='grey'
tk.mainloop()