# Neste playground, vamos trabalhar com um bot no Telegram.
# A configuração inicial é um pouco trabalhosa, mas você só precisa fazer 1 vez.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Inicialização do simulador. Escreva todo o seu código dentro da main!
from extra.playground import rodar

@rodar
def main():
    
    # Começamos importando as bibliotecas, como sempre.
    from requests import get, post
    
    from gpiozero import LED, Button
    from Adafruit_CharLCD import Adafruit_CharLCD
    from time import sleep
    
    
    # Primeiro, siga o passo-a-passo do vídeo para criar um bot:
    # 1 - Baixe o aplicativo Telegram e crie uma conta lá.
    # 2 - Busque pelo BotFather e inicie uma conversa com ele.
    # 3 - Envie a mensagem /newbot e escolha o nome e o usuário do seu bot.
    # 4 - Copie a chave secreta para a variável abaixo (algo como "12345:ABCDEFGLK...")
    chave = "1794507245:AAGilc5zBwf8zdtzBkrxUc5B3ZzuI7XjQao"
    
    
    # Aí a gente coloca a chave no endereço onde faremos as solicitações
    endereco_base = "https://api.telegram.org/bot" + chave
    
    
    # Podemos testar primeiro se a chave está ok fazendo um pedido para o /getMe
    # Rode o código e veja se a mensagem no Shell mostra os dados do seu bot
    endereco_dados_do_bot = endereco_base + "/getMe"

    print("Buscando dados sobre o bot...")
    resultado = get(endereco_dados_do_bot)
    print(resultado.text)
    
    
    # Agora vamos conversar com o bot
    # 5 - Abra o Telegrma, busque o usuário do seu bot e inicie uma conversa com ele.
    # 6 - Envie uma ou mais mensagens quaisquer.
    # 7 - Abra o seu navegador e acesse http://api.telegram.org/botSUA_CHAVE_SECRETA/getUpdates
    # 8 - Copie o id do chat (procure por "chat": {"id":123456...}).
    id_da_conversa = "COLOQUE AQUI O ID DA CONVERSA"
    
    
    # Pronto! Agora você pode enviar mensagens via programação!
    dados = {"chat_id": id_da_conversa, "text": "Mensagem enviada pelo Python!"}
    endereco_para_mensagem = endereco_base + "/sendMessage"
    
    # DESCOMENTE AS LINHAS ABAIXO PARA TESTAR, E DEPOIS COMENTE DE NOVO.
    
    #print("\nEnviando mensagem...")
    #resultado = post(endereco_para_mensagem, json=dados)
    #print(resultado.text)
    
    
    # Se você quiser enviar uma foto, é só abrir o arquivo e usar a sendPhoto.
    endereco_para_foto = endereco_base + "/sendPhoto"
    dados = {"chat_id": id_da_conversa}
    arquivo = {"photo": open("foto_telegram.jpg", "rb")} # foto de exemplo do Playground 04
    
    # DESCOMENTE AS LINHAS ABAIXO PARA TESTAR, E DEPOIS COMENTE DE NOVO.
    
    #print("\nEnviando foto...")
    #resultado = post(endereco_para_foto, data=dados, files=arquivo)
    #print(resultado.text)
    

    # Para obter as mensagens enviadas pelo usuário ao bot, usamos a getUpdates.
    # Na teoria, a gente usou o while True para ficar buscando mensagens continuamente.
    # Neste playground, vamos chamar só uma vez, para simplificar.
    proximo_id_de_update = 0
    endereco = endereco_base + "/getUpdates"
    dados = {"offset": proximo_id_de_update}
    
    # DESCOMENTE AS LINHAS ABAIXO PARA TESTAR, E DEPOIS COMENTE DE NOVO
    
    #print("\nBuscando novas mensagens...")
    #resposta = get(endereco, json=dados)
    #dicionario_da_resposta = resposta.json()
    #print(dicionario_da_resposta)



    # VERIFIQUE OS DADOS RETORNADOS E ENCONTRE O PRIMEIRO "update_id".
    # AGORA ATUALIZE A VARIÁVEL proximo_id_de_update ALI EM CIMA PARA ESSE VALOR + 1.
    # RODE NOVAMENTE O PROGRAMA E VEJA QUE O PRIMEIRO RESULTADO NÃO APARECE MAIS.
    # OBS: uma vez que você fornece um offset, as mensagens anteriores nunca mais serão retornadas.
    
    
    
    # EXPERIMENTE INTEGRAR O BOT COM OS DISPOSITIVOS DO SIMULADOR!
    # Sugestão 1: enviar uma mensagem ao apertar um botão.
    # Sugestão 2: usar o while True para tocar a campainha sempre que o usuário enviar uma mensagem pelo celular.
    
    
    

    while True:
        
        
        sleep(0.1)