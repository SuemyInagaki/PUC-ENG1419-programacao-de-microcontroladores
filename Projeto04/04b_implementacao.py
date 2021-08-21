from extra.aula import rodar

@rodar
def programa():
  
  # importação de bibliotecas
  from time import sleep
  from gpiozero import LED, Button, Buzzer
  from Adafruit_CharLCD import Adafruit_CharLCD
  from os import system
  from subprocess import Popen
  from requests import get, post
  
  # parâmetros iniciais do Telegram
  chave = "1742854251:AAEIBHi-IwYt03L0_l6hQ7wGhpbUguiji-A"
  id_da_conversa = "1257553349"
  
  #chave = "1794507245:AAGilc5zBwf8zdtzBkrxUc5B3ZzuI7XjQao"
  #id_da_conversa = "744769004"
  endereco_base = "https://api.telegram.org/bot" + chave
  
  
  # definição de funções
  

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
    
  # criação de componentes
  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  buzzer = Buzzer(16)
  led1 = LED(21)
  
  botao1.when_held = toca_campainha
  botao1.when_released = desliga_campainha
  botao2.when_pressed = apaga_led1
  
  # loop infinito
  proximo_id_de_update = 0
  while True:
    endereco = endereco_base + "/getUpdates"
    dados = {"offset": proximo_id_de_update}
    resposta = get(endereco, json=dados)
    dicionario_da_resposta = resposta.json()
    if dicionario_da_resposta["result"] != []:
      notificacao = dicionario_da_resposta["result"][0]["message"]["text"] 
      if ( notificacao =="Abrir"):
        acende_led()
      if ( notificacao == "Alarme"):
        buzzer_cinco()
      for update in dicionario_da_resposta["result"]:
          proximo_id_de_update = update["update_id"] + 1
    sleep(1)
