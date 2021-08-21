#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <JKSButton.h>
#include <TouchScreen.h> 

Adafruit_ILI9341 tela = Adafruit_ILI9341(8, 10, 9);
JKSButton botao;
TouchScreen touch(6, A1, A2, 7, 300);

int contagem = 0;

int screenWidth = 240;
int screenHeight = 320;

void desenhaBandeira() {
  tela.fillRect(50, 30, 150, 30,  ILI9341_WHITE);
  tela.fillRect(50, 60, 150, 30,  ILI9341_RED);
  tela.fillTriangle(50,30, 80, 60, 50, 90,  ILI9341_BLUE);
}

void desenhaCirculos() {
  for (int i=1; i<11; i++) {
    tela.drawCircle(screenWidth/2, screenHeight/2, i*5, ILI9341_WHITE);
  }
}

void botaoPressionado(JKSButton & botao) {
  contagem++;
  Serial.println(contagem);
  
  tela.fillRect(110, 235, 100, 50,  ILI9341_BLACK);
  tela.setCursor(110, 240);
  tela.setTextColor(ILI9341_WHITE);
  tela.setTextSize(4);
  tela.print(contagem);
}

void desenhaBotao() {
  botao.init(&tela, &touch, 50, 260, 100, 50, ILI9341_RED, ILI9341_BLACK, ILI9341_WHITE, "Contar", 2);
  botao.setPressHandler(botaoPressionado);
}

void setup() {
  Serial.begin(9600);
  
  tela.begin();
  tela.fillScreen(ILI9341_BLACK);

  desenhaBandeira();
  desenhaCirculos();
  desenhaBotao();
}

void loop() {
  botao.process();
}

