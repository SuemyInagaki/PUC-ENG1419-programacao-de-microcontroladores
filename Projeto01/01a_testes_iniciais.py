from extra.aula import rodar

@rodar
def programa():
  
  global qt
  qt = 0
  # importação de bibliotecas
  from gpiozero import LED, Button
  from time import sleep
  from Adafruit_CharLCD import Adafruit_CharLCD


  # definição de funções
  def muda_led2():
    led2.toggle()

  def piscar_led3():
    global qt
    qt+=1
    lcd.clear()
    lcd.message(str(qt))
    led3.blink(n=4)



  # criação de componentes
  led1 = LED(21)
  led2 = LED(22)
  led3 = LED(23)
  led4 = LED(24)
  led5 = LED(25)

  botao1 = Button(11)
  botao2 = Button(12)
  botao3 = Button(13)
  botao4 = Button(14)
  
  lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
  led1.blink(on_time=1.0, off_time=3.0)

  
  
  botao2.when_pressed = muda_led2
  botao3.when_pressed = piscar_led3


  # loop infinito
  while True:
    if(botao1.is_pressed and led1.is_lit):
      led5.on()
    else:
      led5.off()

    sleep(0.2)
    