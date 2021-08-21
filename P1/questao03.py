from extra.prova import rodar

@rodar
def programa():
    
    # importação das bibliotecas
    from time import sleep
    from gpiozero import LED, Button, DistanceSensor, Buzzer, LightSensor, MotionSensor
    from datetime import datetime
    from pymongo import MongoClient, ASCENDING, DESCENDING
    #from extra.redefinir_banco import redefinir_banco
    from requests import post
    from flask import Flask, render_template, redirect
    from threading import Timer
    from Adafruit_CharLCD import Adafruit_CharLCD
    from mplayer import Player
    from lirc import init, nextcode
    from py_irsend.irsend import send_once, list_codes
    
    global tempo
    tempo = 0
    global pos
    pos = 0
    global timer
    timer = None
    global em_andamento
    # parâmetros do Telegram e IFTTT
    #Suemy
    chaveI = "cZcBTcJeQr10EpUhOvhmwu0FjLIjg0bjCHu2fZpLprq"

    evento = "questao3"
    endereco = "https://maker.ifttt.com/trigger/" + evento + "/with/key/"  + chaveI  
        
    
    # inicialização dos componentes
    
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
    botao1 = Button(11)
    botao2 = Button(12)
    botao3 = Button(13)
    botao4 = Button(14)
    sensor_de_movimento = MotionSensor(27)
    sensor_de_luz = LightSensor(8)
    sensor_de_luz.threshold = 0.7
    sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
    buzzer = Buzzer(16)
    init("aula", blocking=False)
    
    # definição das funções
    #para enviar dados
    def envia_dados():
        global tempo
        agora = datetime.now()
        hora = agora.strftime("%H:%M:%S")
        dados = {"value1": str(tempo), "value2": hora}
        resultado = post(endereco, json=dados)
        print("\n", resultado.text, "\n\n")
    
    def timer_recorrente():
        global timer
        global tempo
        global em_andamento
        if em_andamento:
            tempo-=1
            lcd.clear()
            lcd.message("Tempo: "+str(tempo))
            if tempo == 0:
                buzzer.beep(n=1,on_time=0.5)
                em_andamento=False
                lcd.clear()
                lcd.message(mensagem)
        timer = Timer(1.0, timer_recorrente) #declara o timer
        timer.start() #start no timer
        
            
    
    # loop infinito
    mensagem = "Escolha o tempo\nem segundos"
    lcd.clear()
    lcd.message(mensagem)
    while True:
        lista_com_codigo = nextcode()
    
        # Se tiver chegado alguma coisa...
        if lista_com_codigo != []:
            # Pega o código dentro da lista
            codigo = lista_com_codigo[0]
            if codigo == "KEY_UP":
                tempo+=1
            elif codigo == "KEY_DOWN":
                tempo-=1
                if tempo < 0:
                    tempo = 0
            elif codigo == "KEY_OK":
                global v
                em_andamento = True
                envia_dados()
                timer_recorrente()
------
        sleep(0.2)