###########LIBS utilizadas###########
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from base64 import b64encode
from base64 import b64decode
#######################################
class Cry():
    def __init__(self):

        #self.msg = msg
        #self.key = key
        pass
    def encryp(self,msg,key):#criamos a funcao encryp, responsavel pela encriptacao da mensagem
        global iv #declaramos o iv como variavel global

        cipher = AES.new(key, AES.MODE_CBC)#criamos um novo objeto AES
        byt = cipher.encrypt(pad(msg, 16))#ciframos a mensagem, passando o texto, e o block_size configurado para 16bytes
        iv = b64encode(cipher.iv).decode('utf-8')#aqui é gerado o iv, que sera usado para descriptografar
        byt_64 = b64encode(byt).decode('utf-8')#convertemos para b64
        return byt_64# retornemos o valor do byt_64 para a funcao
    def iv_(self):#criamos a funcao iv_ para poder imprimir separado da byt_64
        global iv
        return iv #retornemos o iv
    def descry(self,msg,key,iv):#criamos a funcao descry, responsavel por descriptografar a mensagem
        texto1 = b64decode(msg)#decodificamos a mensagem
        iv1 = b64decode(iv)#decodificamos o iv
        desi = AES.new(key, AES.MODE_CBC, iv1)#cria um objeto AES, passando a key, o AES.MODE e o iv
        pt = unpad(desi.decrypt(texto1), 16)#descriptografia a mensagem, passando o texto e o block_size
        return pt #retornemos o texto da variavel para ser chamado a funcao




