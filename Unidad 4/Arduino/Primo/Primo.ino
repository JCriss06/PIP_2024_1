int estado = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

int num;

  void loop() {
    // put your main code here, to run repeatedly:
    switch (estado) {
      case 0:
        if (Serial.available() > 0) {
          num = Serial.readString().toInt();
          estado++;
        }
        break;
      case 1:
        for (int i = 2; i < num; i++) {
          if (num % i == 0) {
            Serial.println("No es primo");
            break;
          } else {
            Serial.println("ES PRIMO");
            break;
          }
        }
        estado = 0;
        break;
    }
    delay(100);
  }
