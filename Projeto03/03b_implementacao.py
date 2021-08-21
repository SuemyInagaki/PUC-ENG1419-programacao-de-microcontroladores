from extra.aula import rodar

@rodar
def programa():
  # importação de bibliotecas
  from extra.redefinir_banco import redefinir_banco
  from Adafruit_CharLCD import Adafruit_CharLCD
  from pymongo import MongoClient
  from lirc import init, nextcode
  from datetime import datetime, timedelta 
  from gpiozero import LED, Button, Buzzer, DistanceSensor
  from time import sleep
  
  # a linha abaixo apaga todo o banco e reinsere os moradores
  redefinir_banco()
  
  # parâmetros iniciais do banco
  cliente = MongoClient("localhost", 27017)
  banco = cliente["projeto03"]
  colecao = banco["moradores"]
  oi SUEMY
  apt = ""
  senha = "" 
    # criação de componentes
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  init("aula", blocking=False)
  
  # definição de funções
  def validar_apartamento(apt):
    dado = colecao.find_one({"apartamento": apt})
    if dado == None:
      return False
    else:
      return True

  def selecionar_numero(tecla):
    return (tecla[-1])
  
  def retornar_nome_do_morador(str_apt, str_senha):
    dado = colecao.find_one({"apartamento": str_apt, "senha": str_senha})
    if(dado == None):
      return None
    else:
      return dado["nome"]

  def coletar_digitos(mensagem):
    lcd.clear()
    lcd.message(mensagem + "\n")
    apt = ""
    while True:
      lista_com_codigo = nextcode()
      if lista_com_codigo != []:
        # Pega o código dentro da lista
        codigo = lista_com_codigo[0]
        if codigo == "KEY_OK":
          return apt
        else:
          apt += selecionar_numero(codigo)
          lcd.message("*")
      sleep(0.1)
      
  
  # print( validar_apartamento("102") )
  # print( validar_apartamento("000") )
  # print( retornar_nome_do_morador("102", "102001") )
  # print( retornar_nome_do_morador("102", "00") )
  # print( coletar_digitos("Digite o apto:") )
  # print( coletar_digitos("Digite a senha:") ) 

  # loop infinito
  while True:
    apt = coletar_digitos("Digite o apto:")
    if(validar_apartamento(apt)):
      senha = coletar_digitos("Digite a senha:")
      nome = retornar_nome_do_morador(apt, senha)
      if nome == None:
        lcd.clear()
        lcd.message("Acesso Negado\n")
        sleep(1.0)
      else:
        lcd.clear()
        lcd.message("Bem-vindo(a)\n" + nome + "!")
        sleep(1.0)
    else:
        lcd.clear()
        lcd.message("Apartamento\ninvalido!")
        sleep(1.0)
    
    sleep(0.2)