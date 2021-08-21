#include <AFMotor.h>

int sensorOtico1 = A11; 
int sensorOtico2 = A12;
int automatico = 0;
AF_DCMotor motor3(3); // esquerda
AF_DCMotor motor4(4); // direita

bool modoAuto = false;
unsigned long millisUltimoEnvio = 0;
int velocidade = 160;

void frente(){
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}
void tras(){
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}
void esquerda(){
  motor3.run(RELEASE);
  motor4.run(FORWARD);
}
void direita(){
  motor3.run(FORWARD);
  motor4.run(RELEASE);
}

void parar(){
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void verificaSePrecisaEnviarValores(){
  unsigned long agora = millis();
  if (agora > millisUltimoEnvio + 100) {
    int valorDigital1 = digitalRead(sensorOtico1);
    int valorDigital2 = digitalRead(sensorOtico2);
    Serial.println(String(valorDigital1) + String(valorDigital2));
    millisUltimoEnvio = agora;

    if(modoAuto){
      rodaAutomatico();
    } 
  }
}

void recebeComandos(String valorSerial){
  if(valorSerial.startsWith("f") == true){
    frente();
  }
  else if(valorSerial.startsWith("t") == true){
    tras();
  }
  else if(valorSerial.startsWith("e") == true){
    esquerda();
  }
  else if(valorSerial.startsWith("d") == true){
    direita();
  }
}

void verificaAuto(String valorSerial){
  if(valorSerial.startsWith("a") == true){
    parar();
    modoAuto = true;
  }
  if(valorSerial.startsWith("p") == true){
    modoAuto = false;
    parar();
  }
}

void rodaAutomatico(){
  int valorAnalogico1 = analogRead(sensorOtico1);
  int valorAnalogico2 = analogRead(sensorOtico2);
  Serial.print(valorAnalogico1);
  Serial.print(',');
  Serial.println(valorAnalogico2);
  //os dois estao na linha preta
  if(valorAnalogico1 >= 512 && valorAnalogico2 >= 512){
    frente();
  }
  // o sensor da esquerda esta fora da linha. Tem que virar pra direita
  else if(valorAnalogico1 < 512 && valorAnalogico2 >= 512){
    direita();
  }
  // o sensor da direita esta fora da linha. Tem que virar pra esquerda
  else if(valorAnalogico1 >= 512 && valorAnalogico2 < 512){
    esquerda();
  }
}


void setup() {
  motor3.setSpeed(velocidade);
  motor4.setSpeed(velocidade);
  pinMode(sensorOtico1, INPUT);
  pinMode(sensorOtico2, INPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}


void loop() {
  verificaSePrecisaEnviarValores();
  if (Serial.available() > 0) {
    String valorSerial = Serial.readStringUntil('\n');
    valorSerial.trim();
    verificaAuto(valorSerial);
    if(modoAuto == false){
      recebeComandos(valorSerial);
    }
  }
}

