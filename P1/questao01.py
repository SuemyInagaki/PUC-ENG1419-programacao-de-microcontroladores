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
    from flask import Flask
    from threading import Timer
    from Adafruit_CharLCD import Adafruit_CharLCD
    from mplayer import Player

    

    global timer
    timer = None
    
    global q
    q = 0
    # definição das funções
    def exibe_mensagem():
        lcd.clear()
        lcd.message("Teste")
        sleep(2)
        lcd.clear()
    
    def exibe_movimento():
        lcd.clear()
        if sensor_de_movimento.motion_detected:
            lcd.message("Com movimento\nDistancia: ")
            d = sensor_de_distancia.distance
            d = str(round(d,3))
            lcd.message(d)
            sleep(1)
            lcd.clear()
        else:
            lcd.clear()
            lcd.message("Sem movimento\nDistancia: ")
            d = sensor_de_distancia.distance
            d = str(round(d,3))
            lcd.message(d)
            sleep(1)
            lcd.clear()
    
    def toca_musica():
        player.loadfile("som.mp3")
        player.pause()
    # inicialização dos componentes
    global ultimo
    #
    # o print/botao3 estava travando
    # entao usei o lcd message.
    # No dia da prova você pediu 
    # pra deixar um comentario 
    # avisando que fiz isso
    #
    #
    def imprime_tempo():
        global q
        global ultimo
        if q == 0: #primeira vez
            ultimo = datetime.now()
            lcd.clear()
            lcd.message("Primeira vez clicando")
            q+=1
        else:
            depois = datetime.now() - ultimo
            depois = depois.total_seconds()
            lcd.clear()
            lcd.message("Clicou de novo depois\nde %.1f segundos" %depois)
            ultimo = datetime.now()
        
        
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
    botao1 = Button(11)
    botao2 = Button(12)
    botao3 = Button(13)
    botao4 = Button(14)
    sensor_de_movimento = MotionSensor(27)
    sensor_de_luz = LightSensor(8)
    sensor_de_luz.threshold = 0.35
    sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
    sensor_de_luz.when_dark = toca_musica
    
    botao1.when_pressed = exibe_mensagem
    botao2.when_pressed = exibe_movimento
    botao3.when_pressed = imprime_tempo
    
    
    
    # Definir o parametro
    sensor_de_distancia.threshold_distance = 0.1
    player = Player()
    
    # loop infinito    
    while True:
        sleep(0.2)