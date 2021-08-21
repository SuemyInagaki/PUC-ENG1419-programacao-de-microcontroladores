from extra.aula import rodar

@rodar
def programa():
  
  # importação de bibliotecas
  from time import sleep
  from gpiozero import LED
  from datetime import datetime
  from pymongo import MongoClient, ASCENDING, DESCENDING
  #from extra.redefinir_banco import redefinir_banco
  from requests import post
  from flask import Flask
  
  
  # inicialização do banco e da chave do IFTTT
  #redefinir_banco()
  
  cliente = MongoClient("localhost", 27017)
  banco = cliente["implementacao"]
  colecao_dados = banco["leds"]
  
  app = Flask(__name__)

  
  # definição das funções
  @app.route("/led/<int:index>/<string:state>")
  def led(index, state):
      
      if state == "on":
        leds[index-1].on()
      else:
        leds[index-1].off()
      
      print("Alterei o estado do LED %d para %s" %(index, state))
      
      return "Texto qualquer, porque quem vai acessar esta página é o IFTTT."


  

  def envia_dados():
    data = datetime.now()
    estado_dos_leds = []

    for led in leds: 
      estado_dos_leds.append(led.is_lit)
   
    dados = {"data": data, "estados_dos_leds": estado_dos_leds} 
    colecao_dados.insert(dados)


  def atualiza_led(index, estado): 
    if index < range(leds): 
      if estado: 
        leds[index].on() 
      else: 
        leds[index].off()

  
  
  # criação de componentes
  leds = [LED(21), LED(22), LED(23), LED(24), LED(25)]
  
  
    
  # criação do servidor
  app.run(port=5000)
  

  # definição das páginas do servidor
  
  
    
  # rode o servidor
  
  
  
  # loop infinito (pode remover depois de criar o servidor)
  while True:

    sleep(2)