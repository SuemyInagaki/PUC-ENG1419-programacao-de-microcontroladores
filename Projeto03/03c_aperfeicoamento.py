# COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
# DEPOIS FAÇA OS NOVOS RECURSOSfrom extra.aula import rodar
from extra.aula import rodar

@rodar
def programa():
  # importação de bibliotecas
  from extra.redefinir_banco import redefinir_banco
  from Adafruit_CharLCD import Adafruit_CharLCD
  from pymongo import MongoClient, ASCENDING, DESCENDING
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
  admin = banco["admin"]

  
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
        buzzer.beep(on_time=0.1, n=1)
        # Pega o código dentro da lista
        codigo = lista_com_codigo[0]
        if codigo == "KEY_OK":
          return apt
        else:
          apt += selecionar_numero(codigo)
          lcd.message("*")
      sleep(0.1)

  def portaria(): 
      apt = coletar_digitos("Digite o apto:")
      if(validar_apartamento(apt)):
        senha = coletar_digitos("Digite a senha:")
        nome = retornar_nome_do_morador(apt, senha)
        if nome == None:
          lcd.clear()
          lcd.message("Acesso Negado\n")
          buzzer.beep(on_time=1, n=1)
          dado = {"apt": apt, "data": datetime.now()}
          admin.insert_one(dado)
          sleep(1.0)
        else:
          lcd.clear()
          lcd.message("Bem-vindo(a)\n" + nome + "!")
          dado = {"apt": apt, "data": datetime.now(), "nome": nome}
          admin.insert_one(dado)
          sleep(1.0)
      else:
          lcd.clear()
          lcd.message("Apartamento\n invalido!")
          buzzer.beep(on_time=1, n=1)
          dado = {"apt": apt, "data": datetime.now()}
          admin.insert_one(dado)
          sleep(1.0)

  def mostra_admin(apt):
    busca = {"apt": apt}
    ordenacao = [["data", DESCENDING]]
    documentos = list(admin.find(busca, sort=ordenacao))
    for doc in documentos:
      if not "nome" in doc:
        print(doc["data"].strftime("%d/%m (%H:%M): SENHA INCORRETA\n"))
      else:
        print(doc["data"].strftime("%d/%m (%H:%M): " + doc["nome"]))

  def pedir_apt():
    apt = coletar_digitos("Digite o apt:")
    mostra_admin(apt)
    
  # criação de componentes
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  init("aula", blocking=False)
  buzzer = Buzzer(16)
  sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
  sensor_de_distancia.threshold_distance = 0.1
  sensor_de_distancia.when_in_range = portaria
  botao1 = Button(11)
  botao1.when_pressed = pedir_apt

  # loop infinito
  while True:

    
    sleep(0.2)