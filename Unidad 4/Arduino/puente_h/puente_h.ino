///puente h -diseñado psolo para corriente continua
int ENA = 3;
int in1 = 5;
int in2 = 6;

void setup() {
  // put your setup code here, to run once:
  pinMode(in1, output);
  pinMode(in2, otput);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available > 0) {
    int v = Serial.readString().toInt();
    if (v == 0) {
      Serial.println("detenerse")
      digitalWrite(in1, 0);
      digitalWrite(in2, 0);
      digitalWrite(ENA, 0);

    } else if (v == = 1) {
      Serial.println("girar izquierda")
      digitalWrite(in1, 0);
      digitalWrite(in2, 1);
      digitalWrite(ENA, 255);

    } else if (v == = 2) {
      Serial.println("girar derecha")
      digitalWrite(in1, 1);
      digitalWrite(in2, 0);
      digitalWrite(ENA, 255);

    } else {
      Serial.printl("Movimiento no valido")
    }
  }
  delay(100);
}
