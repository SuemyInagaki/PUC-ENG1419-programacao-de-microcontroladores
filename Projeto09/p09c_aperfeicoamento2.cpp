#include <ShiftDisplay.h>
#include <GFButton.h>

GFButton botao1(A1);
GFButton botao2(A2);
GFButton botao3(A3);
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true);
int leds[] = {13, 12};

bool modoAuto = false;
int sensorOtico1 = A11; 
int sensorOtico2 = A12;

int estadoAtual = 0;
unsigned long millisUltimoEnvio = 0;
unsigned long millisUltimoInstanteSensor = 0;

String comandos [] = {"frente", "tras", "esquerda", "direita"};

void botao1Pressionado(GFButton& botaoDoEvento){
  estadoAtual++;
  if(estadoAtual == 4){
    estadoAtual = 0;
  }
  display.set(comandos[estadoAtual]);
}

void botao2Pressionado(GFButton& botaoDoEvento){
  if(modoAuto == false){
    Serial.println(comandos[estadoAtual]);
  } 
  
}

void botao2solto(GFButton& botaoDoEvento){
  if(modoAuto == false){
     Serial.println("parar");
  } 
}

void botao3Pressionado(GFButton& botaoDoEvento){
  if(modoAuto == false){
    modoAuto = true;
    display.set("auto");
  }
  else{
    display.set("");
    modoAuto = false;
  }
}

void acendeLed(){
  if (Serial.available() > 0) {
      String valorSerial = Serial.readStringUntil('\n');
      if(valorSerial == "11"){
        digitalWrite(leds[0], HIGH);
        digitalWrite(leds[1], HIGH);
      } else if(valorSerial == "01" ) {
        digitalWrite(leds[0], LOW);
        digitalWrite(leds[1], HIGH);
      } else if(valorSerial == "10") {
        digitalWrite(leds[0], HIGH);
        digitalWrite(leds[1], LOW);
      } else if(valorSerial == "00") {
        digitalWrite(leds[0], LOW);
        digitalWrite(leds[1], LOW);
      }

      unsigned long agora = millis();
      if (valorSerial != "00") {
        millisUltimoInstanteSensor = agora;
      }
      else if (agora > millisUltimoInstanteSensor + 5000) {
        modoAuto = false;
        display.set("");
      }
  }
}

void enviaDirecao(){
  unsigned long agora = millis();
  if (agora > millisUltimoEnvio + 50) {
    Serial.println(comandos[estadoAtual]);
    if(modoAuto){
      Serial.println("auto");
    } else {
      Serial.println("parar");
    }
    millisUltimoEnvio = agora;
  }
}

void setup() {
  pinMode(leds[0], OUTPUT);
  pinMode(leds[1], OUTPUT);
  digitalWrite(leds[0], HIGH);
  digitalWrite(leds[1], HIGH);

  Serial.begin(9600);
  Serial.setTimeout(10);
  botao1.setPressHandler(botao1Pressionado);
  botao2.setPressHandler(botao2Pressionado);
  botao3.setPressHandler(botao3Pressionado);
  botao2.setReleaseHandler(botao2solto);
}

void loop() {
  botao1.process();
  botao2.process();
  botao3.process();
  display.update();
  acendeLed();
  enviaDirecao();
}

