from extra.aula import rodar

@rodar
def programa():
    
  # importação de bibliotecas
  from time import sleep
  from threading import Timer
  from gpiozero import LED, Button, DistanceSensor, Buzzer, LightSensor, MotionSensor
  from Adafruit_CharLCD import Adafruit_CharLCD
  from requests import post
  from flask import Flask

  # definição de funções
  global timer
  timer = None
  
  def movimento_detectado():
    global timer
    led1.on()
    led2.on()
    if timer != None:
      timer.cancel()
      timer = None
  
  
  def inercia_detectada():
    global timer
    led1.off()
    timer = Timer(4, incercia_8_segundos)
    timer.start()
    

  def incercia_8_segundos(): 
    led1.off()
    led2.off()
  
  def envia_dados():
    quantidade_de_luz = sensor_de_luz.value
    quantidade_de_luz = quantidade_de_luz*100
    quantidade_de_luz = round(quantidade_de_luz, 2)
    dis = sensor_de_distancia.distance*100
    dis = round(dis, 2)
    dados = {"value1": str(quantidade_de_luz), "value2": str(dis)}
    resultado = post(endereco, json=dados)
    print("\n", resultado.text, "\n\n")
  # criaçtão de componentes
  #Suemy
  #chave = "cZcBTcJeQr10EpUhOvhmwu0FjLIjg0bjCHu2fZpLprq"
  #Bruna 
  #chave = "c8ffdmk6Gv0q58-Hiephck"
  evento = "Sensores"
  endereco = "https://maker.ifttt.com/trigger/" + evento + "/with/key/"  + chave  
 
  
  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  led1 = LED(21)
  led2 = LED(22)
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  sensor_de_movimento = MotionSensor(27)
  sensor_de_luz = LightSensor(8)
  sensor_de_distancia = DistanceSensor(trigger=17, echo=18)

  botao1.when_pressed = envia_dados
  sensor_de_movimento.when_motion = movimento_detectado
  sensor_de_movimento.when_no_motion = inercia_detectada
 
  
  # loop infinito
  while True:

    sleep(0.2)
