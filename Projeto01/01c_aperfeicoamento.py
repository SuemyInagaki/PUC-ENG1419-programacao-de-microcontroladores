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
    player.speed = 2

  def volta_ao_normal():
    if player.speed == 2:
      player.speed = 1
    else:
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
  botao3.when_held = avancar
  botao3.when_released = volta_ao_normal
  botao1.when_pressed = faixa_anterior

  
  global tempo
  tempo = 0
  
  # loop infinito
  while True:
    lcd.clear()

    metadados = player.metadata

    if metadados != None:
      lcd.message(player.metadata["Title"])
      
    if player.time_pos and player.length:
      duracao_em_segundos = player.length
      seg = duracao_em_segundos
      minuto = str(int(seg//60)).zfill(2)
      seg = str(int(seg%60)).zfill(2)
      duracao_total = minuto+':'+seg

      atual = player.time_pos
      seg = atual
      minuto = str(int(seg//60)).zfill(2)
      seg = str(int(seg%60)).zfill(2)
      posi_atual = minuto+':'+seg +' de '
      lcd.message('\n'+posi_atual+duracao_total)
    
    sleep(0.2)
