
#include <ShiftDisplay.h>
#include <GFButton.h>
#include <RotaryEncoder.h>
#define USE_TIMER_1 true
#include <TimerInterrupt.h>
#define N 100

char* nomeDasNotas[] = {"DO ", "REb", "RE ", "MIb", "MI ", "FA ", "SOb", "SOL", "LAb", "LA ", "SIb", "SI "};
int frequencias[] = {131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247};

int terra = A5;
int campainha = 5;
int sensorDeSom = 19;      
int posicaoAnterior = 0;
int contaEstalos = 0;
unsigned long instantes[N];
unsigned long contagemMetronomo;
unsigned long instanteAnteriorDoEstalo = 0;
//modo 
int modo = 0;
int indice = 0;

RotaryEncoder encoder(20, 21);
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);
GFButton btn_1(A1);
GFButton btn_2(A2);



void press1(GFButton& btn_1)
{
  modo = 1;
  tocaNota(indice, -1);
}

void release1(GFButton& btn_1)
{
  noTone(campainha);
}


void contaEstalo(){
  if(modo == 2){
    unsigned long instanteAtual = millis();
    if(instanteAtual > instanteAnteriorDoEstalo + 200){
      instantes[contaEstalos] = instanteAtual;
      contaEstalos++;
      instanteAnteriorDoEstalo = instanteAtual;
    }
    if(contaEstalos == 2){
      int intervalo = instantes[1] - instantes[0];
      int batidasPorMinuto = 60000 / intervalo;
      display.set(batidasPorMinuto);
    }
  }

}

void tickDoEncoder(){
  encoder.tick();
}

void press2(GFButton& btn_2)
{
  modo = 2;
  contaEstalos = 0;
}

void release2(GFButton& btn_2)
{
  noTone(campainha);
}

void tocaNota(int indiceNota, int duracao){
  if(duracao > 0){
    tone(campainha, frequencias[indiceNota], duracao);
  }else {
    tone(campainha, frequencias[indiceNota]);
  }
  display.set(nomeDasNotas[indiceNota]);
}

void setup() {
  // campainha 
  pinMode(terra, OUTPUT);
  digitalWrite(terra, LOW);
  pinMode(campainha, OUTPUT);

  // botoes 
  btn_1.setPressHandler(press1);
  btn_2.setPressHandler(press2);
  btn_1.setReleaseHandler(release1);
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

void encoderLogic(){
  int posicao = encoder.getPosition();
  if(posicao > 11){
    encoder.setPosition(11);
  }
  if(posicao < 0){
    encoder.setPosition(0);
  }
  
  if (posicao != posicaoAnterior) {
    posicaoAnterior = posicao;
    indice = posicao;
    tocaNota(indice, 200);
  }
}

void loop() {
  display.update(); // circula rapidamente entre os dígitos
  btn_1.process();
  btn_2.process();
  if(modo == 1)
    encoderLogic();

  if(modo == 2){
    if(contaEstalos >= 2){
      unsigned int instanteAtual = millis();
      if (instanteAtual > contagemMetronomo + (instantes[1] - instantes[0])){
        tone(campainha, 220.0, 200);
        contagemMetronomo = instanteAtual;
      }
    }
  }

}





