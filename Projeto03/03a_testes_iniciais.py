from extra.aula import rodar

@rodar
def programa():
    
  # importação de bibliotecas
  from time import sleep
  from datetime import datetime, timedelta 
  from gpiozero import LED, Button, Buzzer, DistanceSensor
  from Adafruit_CharLCD import Adafruit_CharLCD
  from pymongo import MongoClient, ASCENDING, DESCENDING
  from extra.redefinir_banco import redefinir_banco
  
  # definição de funções
  
  def toca_campainha():
    buzzer.beep(n=1, on_time=0.5)
  
  def sensor_proximo():
    led.blink(n=2)

  def mostra_distancia():
    lcd.clear()
    lcd.message(("%.1f cm") % (sensor_de_distancia.distance*100))
    dado = {"data": datetime.now(), "distancia": sensor_de_distancia.distance * 100 }
    colecao_dados.insert_one(dado)

  # criação de componentes
  led = LED(21)
  botao1 = Button(11)
  botao2 = Button(12)
  buzzer = Buzzer(16)
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
  
  sensor_de_distancia.threshold_distance = 0.1
  
  sensor_de_distancia.when_in_range = sensor_proximo
  sensor_de_distancia.when_out_of_range = sensor_proximo
  
  botao1.when_pressed = toca_campainha
  botao2.when_pressed = mostra_distancia
  
  # inicialização do banco de dados
  
  redefinir_banco()
  
  cliente = MongoClient("localhost", 27017)
  banco = cliente["testes_iniciais"]
  colecao_dados = banco["dados"]

  
  # loop infinito
  while True:
    sleep(0.2)
