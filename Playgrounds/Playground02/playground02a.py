# Neste playground, vamos trabalhar com o controle remoto.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Inicialização do simulador. Escreva todo o seu código dentro da main!
from extra.aula import rodar

@rodar
def main():
    
    # Começamos importando as bibliotecas, como sempre.
    
    from py_irsend.irsend import send_once
    from py_irsend.irsend import list_remotes
    from lirc import init, nextcode
    
    from gpiozero import LED, Button
    from Adafruit_CharLCD import Adafruit_CharLCD
    from time import sleep
    
    #list_remotes()
    
    # Imagine que a gente quisesse controlar algum aparelho a distância via programação.
    # Para isso, o Raspberry Pi poderia emitir sinais pelo LED infravermelho, como se fosse um controle remoto. 
    # Nesse caso, é só chamar a send_once com o nome do controle e os códigos das teclas.
    # No caso do simulador, o sinal que seria enviado vai aparecer no Shell. Rode o código para testar.
    print("Emitindo o código de uma tecla...")
    send_once("mini", ["KEY_1"]) # o código da(s) tecla(s) tem que estar sempre numa lista!!!
    
    print("\nEmitindo o código de várias teclas...")
    send_once("mini", ["KEY_2", "KEY_3"])
    
    
    # Esses comandos poderiam ser enviados ao apertar um dos botões físicos do Raspberry Pi
    # ATENÇÃO: não confundir o Botão 1 (abaixo do LCD) com a Tecla 1 do controle (à direita)!
    
    def enviar_tecla_4():
        # ENVIE O CÓDIGO DA TECLA 4 DO CONTROLE "mini"
        # DEPOIS APERTE O BOTÃO 1 PARA TESTAR
        print("Apertei o botão 1 para enviar o código da tecla 4")
        send_once("mini", ["KEY_4"])
    
    #led1 = LED(21)
    botao1 = Button(11)
    botao1.when_pressed = enviar_tecla_4



    # AO APERTAR O BOTÃO 2, ENVIE O CÓDIGO DAS TECLAS UP, DOWN, LEFT E RIGHT
    
    def enviar_setas():
        print("Apertei o botão 2 para enviar o código das setas")
        send_once("mini", ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"])

    botao2 = Button(12)
    botao2.when_pressed = enviar_setas
    
    
    
    # Outros componentes que usaremos a seguir
    led1 = LED(21)
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
    
    
    # Além de enviar comandos para algum aparelho, podemos receber sinais de um controle remoto.
    # Para isso, primeiro é necessário inicializar a comunicação com o lirc, SEMPRE deste jeito:
    init("aula", blocking=False)
    quant = 0
    posi = 0
    
    # Agora é só usar o while True aqui no final para ficar monitorando os sinais vindos do controle.
    # Aperte as teclas no simulador para testar.
    while True:
        # Tenta capturar algo enviado.
        lista_com_codigo = nextcode()
        
        # Se tiver chegado alguma coisa...
        if lista_com_codigo != []:
            
            # Pega o código dentro da lista
            codigo = lista_com_codigo[0]
            
            # Agora é só verificar qual código recebemos
            if codigo == "KEY_1":
                print("Apertaram a tecla 1 do controle!")
                
                
            elif codigo == "KEY_2":
                print("Apertaram a tecla 2 do controle!")
            
            elif codigo == "KEY_3":
                led1.on()

            elif codigo == "KEY_4":
                led1.off()
                
            
            # SE A TECLA 3 FOR PRESSIONADA, ACENDA O LED 1
            # SE A TECLA 4 FOR PRESSIONADA, APAGUE O LED 1
            elif codigo == "KEY_7":
                quant+=1
                lcd.clear()
                lcd.message(str(quant)+'\n')
            
            elif codigo == "KEY_LEFT":
                lcd.clear()
                if posi == 0:
                    posi = 15
                else:
                    posi-=1
                    lcd.message(" "*posi + "o")
            elif codigo == "KEY_RIGHT":
                lcd. clear()
                if posi == 15:
                    posi = 0
                else:
                    posi+=1
                    lcd.message(" "*posi + "o")
            
            
            
            
            
            # CONTE QUANTAS VEZES A TECLA 7 FOI PRESSIONADA E EXIBA ISSO NO LCD
            # DICA 1: CRIE UMA VARIÁVEL FORA DO WHILE E ATUALIZE SEU VALOR AQUI
            # DICA 2: LEMBRE DE CONVERTER O NÚMERO PARA TEXTO ANTES DE PASSAR PARA O LCD!
        
        
        

            # INVENTE OUTRAS FUNCIONALIDADES PARA AS TECLAS DE ESQUERDA E DIREITA!
            
            
            
            

        sleep(0.1)