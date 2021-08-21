#include <AFMotor.h>

AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);

int sensorOtico1 = A11; 
int sensorOtico2 = A12;

int valorAnalogicoAnterior = 0;
int contadorX = 0;
int estadoSensor = 1;

void mudaEstadoMotor(){
  if (Serial.available() > 0) {
      String valorSerial = Serial.readStringUntil('\n');
      valorSerial.trim();
      int velocidade = 0;
      if(valorSerial.startsWith("f") == true){
        velocidade = valorSerial.substring(7).toInt();
        motor3.run(FORWARD);
      } else {
        velocidade = valorSerial.substring(5).toInt();
        motor3.run(BACKWARD);
      }
      motor3.setSpeed(velocidade);
  }
}


void enviaAnalogico(){
  int valorAnalogico = analogRead(sensorOtico2);
  if(valorAnalogicoAnterior < 800 && valorAnalogico >= 800){
    contadorX++;
    Serial.println("Contagem " + String(contadorX));
  }
  valorAnalogicoAnterior = valorAnalogico;
}

void verificaEstado(){
  //LOW = 1 e HIGH = 0
  int valorDigital = digitalRead(sensorOtico1); 
  if (valorDigital == LOW && estadoSensor == 0) {
    Serial.println("mudou");
    estadoSensor = 1;
  }
  else if(valorDigital == HIGH && estadoSensor == 1) {
    estadoSensor = 0;
    Serial.println("mudou");
  }
}

void setup() {
  pinMode(sensorOtico1, INPUT);
  pinMode(sensorOtico2, INPUT);
  Serial.setTimeout(10);
  Serial.begin(9600);
}

void loop() {
  verificaEstado();
  enviaAnalogico();
  mudaEstadoMotor();
}


