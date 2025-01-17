# Neste Playground 01B, vamos trabalhar o MPlayer, além dos dispositivos vistos no Playground 01A.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Como estamos longe do laboratório, usaremos um simulador gráfico para representar os componentes.
# Para controlar o hardware simulado, basta colocar todo o código dentro da função main abaixo.
# Os comandos são os mesmos da teoria, só que dentro da main.
from extra.playground import rodar

@rodar
def main():
    
    # Começamos importando as bibliotecas – sim, dentro da função main!
    from mplayer import Player
    
    from gpiozero import LED, Button
    from Adafruit_CharLCD import Adafruit_CharLCD
    from time import sleep
    
    botao1 = Button(11)
    botao2 = Button(12)
    botao3 = Button(13)
    botao4 = Button(14)
    # Para tocar uma música, primeiro é preciso iniciar o Player.
    # Você só precisa fazer isso uma vez no programa.
    player = Player()
    
    
    # Agora podemos carregar um arquivo de áudio.
    # Veja que o player busca a partir do diretório atual do seu código.
    player.loadfile("musica1.mp3")
    
    
    # Por padrão, a música começa a tocar quando carregamos o arquivo.
    # Se você quiser começar em silêncio, é só chamar pause logo em seguida.
    player.pause()
    
    
    # O comando player.pause() também serve para voltar a tocar a música
    
    # CHAME O PAUSE NOVAMENTE ABAIXO, PARA COMEÇAR A TOCAR
    
    player.pause()
    
    
    # Uma vez que a música está tocando, podemos ajustar alguns parâmetros
    
    # EXPERIMENTE MEXER NOS VALORES ABAIXO
    
    player.volume = 50  # valor entre 0 e 100
    player.speed = 3  # valor < 1 -> mais lento ||| valor > 1 -> mais rápido
    
    player.pause()
    # Outras propriedades retornam algumas informações da música
    duracao_em_segundos = player.length
    print(duracao_em_segundos)
    
    seg = duracao_em_segundos
    
    # CALCULE E IMPRIMA QUANTOS MINUTOS E SEGUNDOS A MÚSICA TEM (EX: "2:43")
    # DICA: USE A DIVISÃO INTEIRA DE PYTHON (OU ARREDONDAMENTO) E O RESTO DE DIVISÃO %
    minuto = int(seg//60)
    seg = int(seg%60)
    print(str(minuto)+':'+str(seg)+'\n')
    
    
    
    # Os metadados são retornados num dicionário de Python.
    # Mas pode ser que a música venha sem metadados, ou eles podem estar incompletos
    # Logo, é bom fazer umas verificações antes de acessar as chaves do dicionário.
    metadados = player.metadata
    print(metadados, "\n")
    
    if metadados != None:
        if "Title" in metadados:
            print("Nome da música: " + metadados["Title"])
            
        if "Artist" in metadados:
            print("Artista: " + metadados["Artist"])
            
    
    
    # EXPERIMENTE INTEGRAR OS DISPOSITIVOS COM O PLAYER! BRINQUE À VONTADE!
    # Sugestão 1: faça com que um dos botões pause/despause a música
    # Sugestão 2: mostre o nome da música e o artista no LCD (um em cada linha)
    # Sugestão 3: um botão que aumente o volume e outro que diminua (use uma variável global)
    def pausa_musica():
        player.pause()
    botao3.when_pressed = pausa_musica
    
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
    def mostra_lcd():
        lcd.clear()
        lcd.message(metadados["Title"])
        lcd.message('\n')
        lcd.message(metadados["Artist"])
    
    botao4.when_pressed = mostra_lcd
    
    def aumenta():
        if(player.volume <= 90):
            player.volume+=10
    
    botao1.when_pressed = aumenta
    
    def diminui():
        if(player.volume >=10):
            player.volume-=10
    botao2.when_pressed = diminui
    # Algumas propriedades da música mudam ao longo do tempo.
    # Só que o MPlayer não tem propriedades para avisar que algo mudou (tipo a when_pressed).
    # Por isso, temos que monitorá-las continuamente dentro do while True
    while True:
        
        # DESCOMENTE A LINHA ABAIXO PARA VER O PROGRESSO DA MÚSICA
        
        print("Instante da música (em segundos):", player.time_pos)
        
        
        # É importante ter o sleep no while True, para não sobrecarregar o programa!
        sleep(0.1)
    
    
    # Não escreva nenhum código depois do while True!
    # O loop infinito segura o programa, então nada aqui embaixo vai rodar.