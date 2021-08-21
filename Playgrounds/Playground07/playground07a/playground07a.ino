
#include <ShiftDisplay.h>
#include <GFButton.h>
#include <RotaryEncoder.h>
#define USE_TIMER_1 true
#include <TimerInterrupt.h>

unsigned long instanteAnteriorDoBotao1 = 0;
unsigned long instanteAnteriorDoEstalo = 0;
unsigned long instanteAnteriorDaContagem1 = 0;

int contaEstalos = 0;
int posicaoAnterior = 0; 
int terra = A5;
int campainha = 5;
int sensorDeSom = 19;        

RotaryEncoder encoder(20, 21);
int leds[] = {13,12,11,10};
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);
GFButton btn_1(A1);
GFButton btn_2(A2);


void press1(GFButton& btn_1)
{
    tone(campainha, 440.0, 500);
}

void press2(GFButton& btn_2)
{
  tone(campainha, 220.0);
}

void release2(GFButton& btn_2)
{
  noTone(campainha);
}

void contaEstalo(){
  unsigned long instanteAtual = millis();
  if(instanteAtual > instanteAnteriorDoEstalo + 50){
      contaEstalos++;
      display.set(contaEstalos);
      instanteAnteriorDoEstalo = instanteAtual;
  }

}

void setup() {
  Serial.begin(9600);
  // leds
  for(int i = 0; i < 4; i++)
  {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], HIGH);
  }
  // campainha 
  pinMode(terra, OUTPUT);
  digitalWrite(terra, LOW);
  pinMode(campainha, OUTPUT);

  // botoes 
  btn_1.setPressHandler(press1);
  btn_2.setPressHandler(press2);
  btn_2.setReleaseHandler(release2);

  // display 
  display.set(contaEstalos);

  // detector de som 
  pinMode(sensorDeSom, INPUT);
  int origem = digitalPinToInterrupt(sensorDeSom);
  attachInterrupt(origem, contaEstalo, RISING);
  

  // encoder 
  int origem1 = digitalPinToInterrupt(20);
  attachInterrupt(origem1, tickDoEncoder, CHANGE);
  int origem2 = digitalPinToInterrupt(21);
  attachInterrupt(origem2, tickDoEncoder, CHANGE);
}

void tickDoEncoder(){
  encoder.tick();
}

void loop() {
  display.update(); // circula rapidamente entre os dígitos
  btn_1.process();
  btn_2.process();

  unsigned long instanteAtual = millis(); 
  if (instanteAtual > instanteAnteriorDaContagem1 + 500) {
    Serial.println("Numero de estalos: %d\n", contaEstalos);
    instanteAnteriorDaContagem1 = instanteAtual;
  }

  int posicao = encoder.getPosition();
  if (posicao != posicaoAnterior) {
    posicaoAnterior = posicao;
    digitalWrite(leds[abs(posicao%4)], LOW);
  }
}
