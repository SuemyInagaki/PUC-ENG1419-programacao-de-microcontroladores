from extra.aula import rodar

@rodar
def programa():
  
  # importação de bibliotecas
  from time import sleep
  from gpiozero import LED, Button, DistanceSensor, Buzzer, LightSensor, MotionSensor
  from datetime import datetime
  from pymongo import MongoClient, ASCENDING, DESCENDING
  #from extra.redefinir_banco import redefinir_banco
  from requests import post
  from flask import Flask
  from threading import Timer
  
  
  # inicialização do banco e da chave do IFTTT
  #redefinir_banco()
  
  cliente = MongoClient("localhost", 27017)
  banco = cliente["implementacao"]
  colecao_dados = banco["leds"]
  
  app = Flask(__name__)

  # definição de funções
  global timer
  timer = None
  


  def inicio(): 
    ordenacao = [["data", DESCENDING]]
    documento = colecao_dados.find_one(sort=ordenacao)
    print(documento)
    
    if documento != None:
      for index in range(len(leds)):
        if documento["estados_dos_leds"][index]:
              leds[index].on()
        else:
              leds[index].off()
    
  def movimento_detectado():
    global timer
    leds[0].on()

    if timer != None:
      timer.cancel()
      timer = None
  
  
  def inercia_detectada():
    global timer
    timer = Timer(6, inercia_10_segundos)
    timer.start()
    

  def inercia_10_segundos(): 
    leds[0].off()
    atualiza_led(0, False)


  # definição das funções
  @app.route("/led/<int:number>/<string:state>")
  def led(number, state):
      index = number - 1 
      if state == "on":
        leds[index].on()
      else:
        leds[index].off()
      
      atualiza_led(index, state)

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
    if index < len(leds): 
      if estado: 
        leds[index].on() 
      else: 
        leds[index].off()

    envia_dados()

  def apaga_led():
    atualiza_led(1, False)

  def acende_led():
    atualiza_led(1, True)
  
  @app.route("/")
  def main_page():
    texto = "<h1>"
    dado = [0,0,0,0,0]
    for i in range(0, len(leds)):
      if leds[i].is_active:
        dado[i] = "acesa"
      else:
        dado[i] = "apagada"
    for i in range(1, len(leds) + 1):
      texto+= "<li>" + "Luz " + str(i) + ": " +  dado[i-1]+"</li>"
    texto+= "</h1>"
    return texto
  # criação de componentes
  leds = [LED(21), LED(22), LED(23), LED(24), LED(25)]
  sensor_de_movimento = MotionSensor(27)
  sensor_de_luz = LightSensor(8)
  sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
  sensor_de_luz.threshold = 0.5
  sensor_de_luz.when_light = apaga_led
  sensor_de_luz.when_dark = acende_led

  sensor_de_movimento.when_motion = movimento_detectado
  sensor_de_movimento.when_no_motion = inercia_detectada

  inicio()
  
  # criação do servidor
  app.run(port=5000)
  

  # definição das páginas do servidor
  
  
    
  # rode o servidor
  
  
  
  # loop infinito (pode remover depois de criar o servidor)
  while True:
    sleep(2)
