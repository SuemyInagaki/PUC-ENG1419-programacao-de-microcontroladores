# Neste playground, vamos trabalhar com o microfone e a câmera.
# ATENÇÃO: lembre-se que os comandos variam de acordo com o sistema operacional!
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Inicialização do simulador. Escreva todo o seu código dentro da main!
from extra.playground import rodar

@rodar
def main():
    
	#[dshow @ 00000235b6c4c240] DirectShow video devices (some may be both video and audio devices)
	#[dshow @ 00000235b6c4c240]  "USB Camera"
	#[dshow @ 00000235b6c4c240]     Alternative name "@device_pnp_\\?\usb#vid_0c45&pid_6367&mi_00#6&bbbec35&0&0000#{65e8773d-8f56-11d0-a3b9-00a0c9223196}\global"

	#[dshow @ 00000235b6c4c240] DirectShow audio devices
	#[dshow @ 00000235b6c4c240]  "Microfone (2- Realtek(R) Audio)"
	#[dshow @ 00000235b6c4c240]     Alternative name "@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{5331879B-057A-4120-B941-0CF3918C7AAF}"


    # Começamos importando as bibliotecas, como sempre.
    from os import system
    from subprocess import Popen
    
    from datetime import datetime
    from gpiozero import LED, Button
    from Adafruit_CharLCD import Adafruit_CharLCD
    from time import sleep
    
    
    # Vamos começar com a parte de tirar fotos com a câmera web.
    # Mas primeiro temos alguns avisos importantes!
    
    # 1. Caso você não tenha uma câmera web, existem apps que conectam a câmera do seu celular com o computador.
        # Nesse caso, experimente apps como o Camo ou o Iriun.
        
    # 2. Usuários de Windows e Mac precisam anotar o identificador da câmera e do microfone.
        # Windows: rode o arquivo listar_midias.bat e anote os nomes.
        # Mac: rode o arquivo listar_midias.command (botão direito > Abrir) e anote os números.
        
    # 3. Usuários de Mac ainda precisam de 2 detalhes extras:
        # Vá na pasta extra/binarios/ffmpeg/mac, clique com o botão direito no ffmpeg e selecione Abrir.
            # (só precisa fazer isso 1 vez, para dar permissão de execução ao binário)
        # Use sempre o Run > Run current script in terminal do Thonny.
        

    
    # Conforme eu comentei na teoria, a ideia aqui é chamar um aplicativo externo por linha de comando, via system.
    # Só que esse app vai variar de acordo com o seu sistema operacional.
    
    
    # DESCOMENTE UMA DAS LINHAS ABAIXO, DE ACORDO COM O SEU SISTEMA OPERACIONAL.
    # EM SEGUIDA, RODE O CÓDIGO E ABRA O ARQUIVO foto_camera.jpg CRIADO NA MESMA PASTA DESTE ARQUIVO PYTHON.
    # CASO A FOTO APAREÇA CORRETAMENTE, COMENTE A LINHA NOVAMENTE.
    
    # WINDOWS
    agora = datetime.now()
    hora = agora.strftime("%H:%M:%S")
    nome_arquivo = "foto_" + hora + ".jpg"
    system("CommandCam /filename foto_camera.jpg /delay 500")
    system("CommandCam /filename " +  nome_arquivo + " /delay 500")
    
    # MAC (substitua o valor de frames por segundo depois do -r e/ou o número da câmera depois do -i, se necessário)
    #system("ffmpeg -y -pix_fmt uyvy422 -ss 0.5 -f avfoundation -r 30 -i 0 foto_camera.jpg")
    
    # LINUX
    #system("fswebcam --resolution 640x480 --skip 10 foto_camera.jpg")
    
    
    
    # O próximo passo é tentar gravar o áudio do microfone.
    # Vamos começar capturando o som por 3 segundos.
    
    
    # DESCOMENTE UMA DAS LINHAS ABAIXO, DE ACORDO COM O SEU SISTEMA OPERACIONAL.
    # DEPOIS RODE O CÓDIGO, FALE ALGO NO MICROFONE E ABRA O ARQUIVO audio1.wav CRIADO NA MESMA PASTA DESTE ARQUIVO PYTHON.
    # CASO O ÁUDIO TENHA SIDO GRAVADO CORRETAMENTE, COMENTE A LINHA NOVAMENTE.
    
    # WINDOWS (escreva o nome do microfone que aparece ao rodar listar_midias.bat)
    #system('ffmpeg -y -f dshow -i audio="Microfone (2- Realtek(R) Audio)" -t 00:03 audio1.wav')
    
    # MAC (substitua o número depois do -i se necessário)
    #system("ffmpeg -y -f avfoundation -i :1 -t 3 audio1.wav")
    
    # LINUX
    #system("arecord --duration 3 audio1.wav")
    
    
    
    # Por fim, vamos testar o controle manual do início e do término da gravação.
    # Copiei o mesmo exemplo lá da teoria.
    
    global aplicativo
    aplicativo = None
    
    def iniciar_gravacao():
        global aplicativo
        
        
        # DESCOMENTE UMA DAS LINHAS ABAIXO, DE ACORDO COM O SEU SISTEMA OPERACIONAL.
        
        # WINDOWS (escreva o nome do microfone que aparece ao rodar listar_midias.bat)
        comando = ["ffmpeg", "-y", "-f", "dshow", "-i", "audio=Microfone (2- Realtek(R) Audio)", "-t", "00:30", "audio2.wav"]
        
        # MAC (substitua o número depois do -i se necessário)
        #comando = ["ffmpeg", "-y", "-f", "avfoundation", "-i", ":1", "-t", "30", "audio2.wav"]
        
        # LINUX
        #comando = ["arecord", "--duration", "30", "audio2.wav"]
        
        
        aplicativo = Popen(comando)
        
        print("Iniciando gravação de áudio...\n\n")
        
    def parar_gravacao():
        global aplicativo
        if aplicativo != None:
            aplicativo.terminate()
            aplicativo = None
            
            print("\n\n Parando gravação de áudio...\n\n")
            
    
    # Mas agora vamos chamar essas funções ao apertar os botões 1 e 2.
    
    botao1 = Button(11)
    botao2 = Button(12)
    
    botao1.when_pressed = iniciar_gravacao
    botao2.when_pressed = parar_gravacao
    
    
    # RODE O CÓDIGO, APERTE O BOTÃO 1, AGUARDE UM POUCO E APERTE O BOTÃO 2.
    # ABRA O ARQUIVO audio2.wav CRIADO NA MESMA PASTA DESTE ARQUIVO PYTHON.
    # VERIFIQUE SE O ÁUDIO TEM A MESMA DURAÇÃO DE TEMPO ENTRE O CLIQUE NOS DOIS BOTÕES.
    # CASO O TEMPO NÃO ESTEJA CORRETO, EXPERIMENTE USAR O Run > Run current script in terminal DO THONNY.
    
    
    # EXPERIMENTE INTEGRAR OS DISPOSITIVOS COM A CÂMERA! BRINQUE À VONTADE!
    # Sugestão 1: tire uma foto caso o sensor de distância detecte proximidade.
    # Sugestão 2: ao apertar o botão 1, exiba o tempo de gravação (segundos + milissegundos) no LCD.
        # Dica: use o while True abaixo, uma variável global tipo datetime e o total_seconds.
    

    while True:
        
        
        sleep(0.1)