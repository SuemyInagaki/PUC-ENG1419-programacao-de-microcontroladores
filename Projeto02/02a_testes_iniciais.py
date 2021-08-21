from extra.aula import rodar

@rodar
def programa():
    
  # importação de bibliotecas
  from gpiozero import LED, Button
  from Adafruit_CharLCD import Adafruit_CharLCD
  from lirc import init, nextcode
  from time import sleep
  



  # definição de funções
  def btn1_pressed():
    for led in leds:
      led.on()

  def btn2_pressed():
    for led in leds:
      led.off()
  

  # criação de componentes
  leds = [LED(21), LED(22), LED(23), LED(24), LED(25)]
  init("aula", blocking=False)
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  btn1 = Button(11)
  btn1.when_pressed = btn1_pressed
  
  btn2 = Button(12)
  btn2.when_pressed = btn2_pressed
  
  led = 1
  # loop infinito
  while True:
  # Tenta capturar algo enviado.
    lista_com_codigo = nextcode()
    
    # Se tiver chegado alguma coisa...
    if lista_com_codigo != []:
        
        # Pega o código dentro da lista
        codigo = lista_com_codigo[0]
        
        # Agora é só verificar qual código recebemos
        if codigo == "KEY_1":
          lcd.clear()
          lcd.message("LED 1\nselecionado")
          led = 1
            
        elif codigo == "KEY_2":
          lcd.clear()
          lcd.message("LED 2\nselecionado")
          led = 2
        
        elif codigo == "KEY_3":
          lcd.clear()
          lcd.message("LED 3\nselecionado")
          led = 3

        elif codigo == "KEY_4":
          lcd.clear()
          lcd.message("LED 4\nselecionado")
          led = 4
        
        elif codigo == "KEY_5":
          lcd.clear()
          lcd.message("LED 5\nselecionado")
          led = 5
        
        elif codigo == "KEY_OK":
          lcd.clear()
          lcd.message("LED "+str(led)+"\nselecionado")
          for i in range(len(leds)):
            if i+1 == led:
              leds[i].toggle()

        elif codigo == "KEY_UP":
          if led == 5:
            led = 1
          else:
            led+=1
          lcd.clear()
          lcd.message("LED "+str(led)+"\nselecionado")

        elif codigo == "KEY_DOWN":
          if led == 1:
            led = 5
          else:
            led-=1
          lcd.clear()
          lcd.message("LED "+str(led)+"\nselecionado")
    sleep(0.2)
