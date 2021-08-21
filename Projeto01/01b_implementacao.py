from extra.aula import rodar

@rodar
def programa():
  
  # importação de bibliotecas
  from time import sleep
  from mplayer import Player
  from Adafruit_CharLCD import Adafruit_CharLCD
  from gpiozero import LED, Button
 
  # definição de funções
  def tocar_pausar():
    player.pause()
    if player.paused:
      led1.blink()
    else:
      led1.on()
  
  def avancar():
    player.pt_step(1)
  
  def faixa_anterior():
    if(player.time_pos):
      if(player.time_pos > 2):
        player.time_pos=0
      else:
        player.pt_step(-1)
  # criação de componentes
  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  
  led1 = LED(21)
  
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)

  player = Player()
  player.loadlist("playlist.txt")
  botao2.when_pressed = tocar_pausar
  botao3.when_pressed = avancar
  botao1.when_pressed = faixa_anterior

  # loop infinito
  while True:
    lcd.clear()
    metadados = player.metadata
    if metadados != None:
      lcd.message(player.metadata["Title"])
    
    
    sleep(0.2)