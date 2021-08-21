// 16 notas
int indicesDeNotaDaMusica[] = {7, 2, 0, 11, 9, 7, 2, 0, 11, 9, 7, 2, 0, 11, 0, 9};
int oitavasDaMusica[] = {0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0};
unsigned long intervalosEntreNotas[] = {1000, 1000, 167, 167, 167, 1000, 500, 167, 167, 167, 1000, 500, 167, 167, 167, 1000};


// COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
// DEPOIS FAÇA OS NOVOS RECURSOS

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
int oitavaCorrente;
int indiceMusica = 0;
unsigned long contagemMusica = 0;



RotaryEncoder encoder(20, 21);
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);
GFButton btn_1(A1);
GFButton btn_2(A2);
GFButton btn_3(A3);



void press1(GFButton& btn_1)
{
  modo = 1;
  tocaNota(indice, -1, oitavaCorrente);
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

void press3(GFButton& btn_2)
{

  modo = 3;
  contagemMusica = millis();
  indiceMusica = 0;
  tocaNota(indicesDeNotaDaMusica[indiceMusica] , intervalosEntreNotas[indiceMusica],oitavasDaMusica[indiceMusica]);
  
}

void tocaNota(int indiceNota, int duracao, int oitava){
  float frequencia = frequencias[indiceNota] * pow(2, oitava);
  if(duracao > 0){
    tone(campainha, frequencia, duracao);
  }else {
    tone(campainha, frequencia);
  }
  char buffer [50];
  
  int n=sprintf(buffer, "%s%d",nomeDasNotas[indiceNota], oitava);
  display.set(buffer);
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
  btn_3.setPressHandler(press3);
  
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
  if(posicao > 35){
    encoder.setPosition(35);
  }
  if(posicao < 0){
    encoder.setPosition(0);
  }
  posicao = encoder.getPosition();
  
  if (posicao != posicaoAnterior) {
    posicaoAnterior = posicao;
    oitavaCorrente = posicao/12;
    indice = posicao%12;
    tocaNota(indice, 200, oitavaCorrente);
  }
}

void loop() {
  display.update(); // circula rapidamente entre os dígitos
  btn_1.process();
  btn_2.process();
  btn_3.process();
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

  if(modo == 3){
    unsigned int instanteAtual = millis();
      if (instanteAtual > contagemMusica + intervalosEntreNotas[indiceMusica]){
        contagemMusica = instanteAtual;
        int len = (int)indicesDeNotaDaMusica/(int)sizeof(int);
        indiceMusica++;
        if(indiceMusica >= len)
          modo = 1;
        tocaNota(indicesDeNotaDaMusica[indiceMusica] , intervalosEntreNotas[indiceMusica],oitavasDaMusica[indiceMusica]);
      }
  }

}