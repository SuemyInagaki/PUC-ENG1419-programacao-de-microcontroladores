#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <JKSButton.h>
#include <TouchScreen.h> 

JKSButton botaoDecolar;
JKSButton botaoPousar;
JKSButton botaoFrente;
JKSButton botaoDireita;
JKSButton botaoEsquerda;

int x_offset = 19;
int y_offset = 168;

Adafruit_ILI9341 tela = Adafruit_ILI9341(8, 10, 9);
TouchScreen touch(6, A1, A2, 7, 300);

void botaoDecolarPressed(JKSButton& botao){
  Serial.println("Decolar");
  Serial1.println("Decolar");
}

void botaoPousarPressed(JKSButton& botao){
  Serial.println("Pousar");
  Serial1.println("Pousar");  
}

void botaoEsquerdaPressed(JKSButton& botao){
  Serial.println("esquerda");
  Serial1.println("esquerda");  
}

void botaoDireitaPressed(JKSButton& botao){
  Serial.println("direita");
  Serial1.println("direita");
}

void botaoFrentePressed(JKSButton& botao){
  Serial.println("frente");
  Serial1.println("frente");
}

void release(JKSButton& botao){
  Serial.println("Parar");
  Serial1.println("Parar");
}

void recebeSerial(){
  if (Serial1.available() > 0) {
    String valorSerial = Serial1.readStringUntil('\n');
    valorSerial.trim();
    Serial.println(valorSerial); 
    if(valorSerial.startsWith("retangulo")){
      int x = valorSerial.substring(10, 13).toInt();
      int y = valorSerial.substring(14, 17).toInt();
      int altura = valorSerial.substring(18, 21).toInt();
      int largura = valorSerial.substring(22, 25).toInt();

      tela.fillRect(x_offset, y_offset, 202, 152, ILI9341_BLACK);
      tela.drawRect(x_offset, y_offset, 202, 152, ILI9341_WHITE);
      tela.fillRect(x_offset+x, y_offset+y, altura, largura, ILI9341_ORANGE);
    }
  }

}

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  tela.begin();
  tela.fillScreen(ILI9341_BLACK);
  Serial.setTimeout(10);
  Serial1.setTimeout(10);

  botaoDecolar.init(&tela, &touch, 60, 50, 100, 50, ILI9341_WHITE, ILI9341_GREEN, ILI9341_BLACK, "Decolar", 2); 
  botaoPousar.init(&tela, &touch, 180, 50, 100, 50, ILI9341_WHITE, ILI9341_RED, ILI9341_WHITE, "Pousar", 2); 
  botaoEsquerda.init(&tela, &touch, 35 , 120, 50, 50, ILI9341_WHITE, ILI9341_LIGHTGREY, ILI9341_BLACK, "<", 2);
  botaoFrente.init(&tela, &touch, 110 , 120, 50, 50, ILI9341_WHITE, ILI9341_LIGHTGREY, ILI9341_BLACK, "^", 2);
  botaoDireita.init(&tela, &touch, 190 , 120, 50, 50, ILI9341_WHITE, ILI9341_LIGHTGREY, ILI9341_BLACK, ">", 2);


  tela.drawRect(x_offset, y_offset, 202, 152, ILI9341_WHITE); 

  botaoDecolar.setPressHandler(botaoDecolarPressed);
  botaoPousar.setPressHandler(botaoPousarPressed); 
  botaoEsquerda.setPressHandler(botaoEsquerdaPressed);
  botaoDireita.setPressHandler(botaoDireitaPressed);
  botaoFrente.setPressHandler(botaoFrentePressed);
  botaoEsquerda.setReleaseHandler(release);
  botaoDireita.setReleaseHandler(release);
  botaoFrente.setReleaseHandler(release);
}

void loop() {
    botaoDecolar.process();
    botaoPousar.process();
    botaoFrente.process();
    botaoDireita.process();
    botaoEsquerda.process();
    recebeSerial();
}

