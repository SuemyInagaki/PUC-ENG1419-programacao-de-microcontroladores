#include <AFMotor.h>

int sensorOtico1 = A11; 
int sensorOtico2 = A12;

AF_DCMotor motor3(3); // esquerda
AF_DCMotor motor4(4); // direita

int millisUltimoEnvio = 0;

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
  motor4.run(RELEASE);
  motor3.run(FORWARD);
}

void parar(){
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void verificaSePrecisaEnviarValores(){
  int agora = millis();
  if (agora > millisUltimoEnvio + 100) {
    int valorDigital1 = digitalRead(sensorOtico1);
    int valorDigital2 = digitalRead(sensorOtico2);
    Serial.println(String(valorDigital1) + String(valorDigital2));
    millisUltimoEnvio = agora;
  }

}


void recebeComandos(){
  if (Serial.available() > 0) {
    String valorSerial = Serial.readStringUntil('\n');
    valorSerial.trim();
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
    else if(valorSerial.startsWith("p") == true){
      parar();
    }
  }
}
void setup() {
  motor3.setSpeed(velocidade);
  motor4.setSpeed(velocidade);
  pinMode(sensorOtico1, INPUT);
  pinMode(sensorOtico2, INPUT);
  Serial.setTimeout(10);
  Serial.begin(9600);
}

void loop() {
    verificaSePrecisaEnviarValores();
    recebeComandos();
}

