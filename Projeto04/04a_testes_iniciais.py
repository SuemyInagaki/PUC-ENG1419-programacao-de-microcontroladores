from extra.aula import rodar

@rodar
def programa():
    
  # importação de bibliotecas
  from time import sleep
  from gpiozero import LED, Button
  from Adafruit_CharLCD import Adafruit_CharLCD
  from os import system
  from subprocess import Popen
  from requests import get, post
  
  # parâmetros iniciais do Telegram
  chave = "1742854251:AAEIBHi-IwYt03L0_l6hQ7wGhpbUguiji-A"
  id_da_conversa = "1257553349"
  endereco_base = "https://api.telegram.org/bot" + chave
  
  # WINDOWS (escreva o nome do microfone que aparece ao rodar listar_midias.bat)
    #system('ffmpeg -y -f dshow -i audio="COLOQUE AQUI O SEU MICROFONE" -t 00:03 audio1.wav')
    
    # MAC (substitua o número depois do -i se necessário)
    #system("ffmpeg -y -f avfoundation -i :1 -t 3 audio1.wav")
    
    # LINUX
    #system("arecord --duration 3 audio1.wav")
  # definição de funções
  

  def iniciar_gravacao():
    lcd.clear()
    lcd.message("Gravando...")
    #system('ffmpeg -y -f dshow -i audio="Microfone (2- Realtek(R) Audio)" -t 00:05 audio1.wav')
    # LINUX
    #system("arecord --duration 5 audio1.wav")     
    lcd.clear()
    
  def tirar_cinco_fotos():
    for i in range(5):
      #LINUX
      #system("fswebcam --resolution 640x480 --skip 10 foto_camera"+str(i)+".jpg")
      #system("CommandCam /filename foto" + str(i) +".jpg /delay 500")
      sleep(2)
      led1.blink(n=1, on_time=0.1, off_time=0.1)
  # criação de componentes
  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  led1 = LED(21)
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  
  def enviar_mensagem():
    dados = {"chat_id": id_da_conversa, "text": "Mensagem enviada pelo Python!"}
    endereco_para_mensagem = endereco_base + "/sendMessage"
    print("\nEnviando mensagem...")
    resultado = post(endereco_para_mensagem, json=dados)
    print(resultado.text)

  botao1.when_pressed = iniciar_gravacao
  botao2.when_pressed = tirar_cinco_fotos
  botao3.when_pressed = enviar_mensagem
  # loop infinito
  while True:
  
    sleep(0.2)
