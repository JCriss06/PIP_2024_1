#include "Server.h";
int pinServo = 9;
Servo servo;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  servo.attach(pinServo);
}

void loop() {
  // put your main code here, to run repeatedly:

  servo.write(0);
  Serial.println("Servo en 0");
  delay(500);

  servo.write(0);
  Serial.println("ervo ")
}
