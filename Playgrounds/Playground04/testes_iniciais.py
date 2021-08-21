from extra.aula import rodar

@rodar
def programa():
    
  # importação de bibliotecas
  from time import sleep
  from gpiozero import LED, Button
  from Adafruit_CharLCD import Adafruit_CharLCD
  from os import system
  from subprocess import Popen
  
  # parâmetros iniciais do Telegram
  chave = "1742854251:AAEIBHi-IwYt03L0_l6hQ7wGhpbUguiji-A"
  id_da_conversa = "COLOQUE O ID DA SUA CONVERSA AQUI!"
  endereco_base = "https://api.telegram.org/bot" + chave
  
  # WINDOWS (escreva o nome do microfone que aparece ao rodar listar_midias.bat)
    #system('ffmpeg -y -f dshow -i audio="COLOQUE AQUI O SEU MICROFONE" -t 00:03 audio1.wav')
    
    # MAC (substitua o número depois do -i se necessário)
    #system("ffmpeg -y -f avfoundation -i :1 -t 3 audio1.wav")
    
    # LINUX
    #system("arecord --duration 3 audio1.wav")
  # definição de funções
  

  def iniciar_gravacao():
    system('ffmpeg -y -f dshow -i audio="Microfone (2- Realtek(R) Audio)" -t 00:03 audio1.wav')
    # LINUX
    #system("arecord --duration 5 audio1.wav")     
    lcd.clear()
    lcd.message("Gravando...")
  
  # criação de componentes
  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  

  botao1.when_pressed = iniciar_gravacao

  # loop infinito
  while True:
  
    sleep(0.2)
