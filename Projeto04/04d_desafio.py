from extra.aula import rodar

@rodar
def programa():
  
  # importação de bibliotecas
  from time import sleep
  from gpiozero import LED, Button, Buzzer, DistanceSensor
  from Adafruit_CharLCD import Adafruit_CharLCD
  from os import system
  from subprocess import Popen
  from requests import get, post
  from datetime import datetime
  from urllib.request import urlretrieve
  from mplayer import Player
  import unidecode
  
  
  # parâmetros iniciais do Telegram
  # MARCOS
  #chave = "1742854251:AAEIBHi-IwYt03L0_l6hQ7wGhpbUguiji-A"
  #id_da_conversa = "1257553349"
  
  #SUEMY
  chave = "1794507245:AAGilc5zBwf8zdtzBkrxUc5B3ZzuI7XjQao"
  id_da_conversa = "744769004"
  endereco_base = "https://api.telegram.org/bot" + chave
  
  
  # definição de funções
  global aplicativo
  aplicativo = None
  
  global chegada
  chegada = 0

  
  
  def iniciar_gravacao():
    global aplicativo
  
    # WINDOWS (escreva o nome do microfone que aparece ao rodar listar_midias.bat)
    #comando = ["ffmpeg", "-y", "-f", "dshow", "-i", "audio=COLOQUE AQUI O SEU MICROFONE", "-t", "00:30", "audio2.wav"]
    
    # LINUX
    comando = ["arecord", "--duration", "30", "audio.wav"]
    
    
    aplicativo = Popen(comando)
    
    print("Iniciando gravação de áudio...\n\n")
        
  def parar_gravacao():
    global gravando
    gravando = False
    global aplicativo
    if aplicativo != None:
        aplicativo.terminate()
        aplicativo = None
        #system("lame audio.wav audio.mp3")
        system("opusenc audio.wav audio.ogg")
        print("\n\n Parando gravação de áudio...\n\n")
        endereco_para_audio = endereco_base + "/sendVoice"
        dados = {"chat_id": id_da_conversa}
        arquivo = {"voice": open("audio.ogg", "rb")} # foto de exemplo do Playground 04
    
        print("\nEnviando audio...")
        resultado = post(endereco_para_audio, data=dados, files=arquivo)
        print(resultado.text)
            
  def apaga_led1():
    led1.off()
  def buzzer_cinco():
    buzzer.beep(n=5, on_time=0.2, off_time=0.5)
  def acende_led():
    led1.on()
  def toca_campainha():
    buzzer.on()
  def desliga_campainha():
    buzzer.off()
    dados = {"chat_id": id_da_conversa, "text": "Alguém está na porta"}
    endereco_para_mensagem = endereco_base + "/sendMessage"
    print("\nEnviando mensagem...")
    resultado = post(endereco_para_mensagem, json=dados)
    print(resultado.text)
    #system("fswebcam --resolution 640x480 --skip 10 foto_camera.jpg")
    #system("CommandCam /filename foto_camera.jpg /delay 500")
    endereco_para_foto = endereco_base + "/sendPhoto"
    dados = {"chat_id": id_da_conversa}
    arquivo = {"photo": open("foto_camera.jpg", "rb")} # foto de exemplo do Playground 04
    
    print("\nEnviando foto...")
    resultado = post(endereco_para_foto, data=dados, files=arquivo)
    print(resultado.text)
    
    buttonAbrir = {"text":"Abrir"}
    buttonSoarAlarme = {"text":"Soar Alarme"} 
    buttonIgnorar = {"text":"Ignorar"}
    teclado = [[buttonAbrir], [buttonSoarAlarme], [buttonIgnorar]]
    dados = {"chat_id": id_da_conversa, "text": "Abrir porta para esta pessoa?", "reply_markup":{"keyboard":teclado,"one_time_keyboard":True}}
    endereco_para_mensagem = endereco_base + "/sendMessage"
    print("\nEnviando mensagem...")
    resultado = post(endereco_para_mensagem, json=dados)
    print(resultado.text)
  
  

  def pessoa_chegou():
    global chegada
    chegada = datetime.now() #hora que a pessoa chegou

  def pessoa_saiu():
    global chegada
    if chegada != 0:
      intervalo = datetime.now() - chegada 
      intervalo = intervalo.total_seconds()
      chegada = 0
      if(intervalo >= 10):
        dados = {"chat_id": id_da_conversa, "text": "Pessoa Saiu"}
        endereco_para_mensagem = endereco_base + "/sendMessage"
        print("\nEnviando mensagem Pessoa Saiu...")
        resultado = post(endereco_para_mensagem, json=dados)
        print(resultado.text)


  # criação de componentes
  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  buzzer = Buzzer(16)
  led1 = LED(21)
  
  botao1.when_held = toca_campainha
  botao1.when_released = desliga_campainha
  botao2.when_pressed = apaga_led1
  botao3.when_held = iniciar_gravacao
  botao3.when_released = parar_gravacao
  sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
  sensor_de_distancia.threshold_distance = 0.1
  sensor_de_distancia.when_in_range = pessoa_chegou
  sensor_de_distancia.when_out_of_range = pessoa_saiu
  player = Player()
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  
  # loop infinito
  proximo_id_de_update = 0
  while True:
    endereco = endereco_base + "/getUpdates"
    dados = {"offset": proximo_id_de_update}
    resposta = get(endereco, json=dados)
    dicionario_da_resposta = resposta.json()
    for update in dicionario_da_resposta["result"]:
      mensagem = update["message"]
      proximo_id_de_update = update["update_id"] + 1

      if 'text' in mensagem:
        notificacao = mensagem["text"]
        if ( notificacao =="Abrir"):
          acende_led()
        elif ( notificacao == "Soar Alarme"):
          buzzer_cinco()
        elif ( notificacao == "Ignorar"):
          continue
        else:
          lcd.clear()
          lcd.message("Mensagem recebida")
          buzzer.beep(n=1, on_time=0.5, off_time=0.5)
          sleep(1)
          lcd.clear()
          sleep(1)
          lcd.message("Mensagem recebida")
          buzzer.beep(n=1, on_time=0.5, off_time=0.5)
          sleep(1)
          lcd.clear()
          sem_acento = unidecode.unidecode(notificacao)
          sleep(1)
          if len(sem_acento) <= 16:
            lcd.clear()
            lcd.message(sem_acento)
          else:
            pos = 0
            while(True):
              lcd.clear()
              lcd.message(sem_acento[pos:pos+16])
              sleep(1)
              pos+=1
              if (pos+16 > len(sem_acento)):
                pos = 0
                break



      elif 'voice' in mensagem:
        notificacao = mensagem["voice"]["file_id"]
        print(notificacao)
        resposta = get(endereco_base + "/getFile", json= {"file_id": notificacao})
        final_do_endereco = resposta.json()["result"]["file_path"]
        base = "https://api.telegram.org/file/bot" + chave + "/"
        endereco_do_arquivo = base + final_do_endereco
        print(endereco_do_arquivo)
        urlretrieve(endereco_do_arquivo, "meuaudio.ogg")

        player.loadfile("meuaudio.ogg")
      #for update in dicionario_da_resposta["result"]:
      #    proximo_id_de_update = update["update_id"] + 1
    sleep(1)


