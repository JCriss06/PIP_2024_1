int leds[] = { 2, 3, 4, 5, 6, 7, 8, 9 };

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {

  if (Serial.available() > 0) {
    int number = Serial.parseInt();

    if (number >= 0 && number <= 255) {
      
      String binario = "";
      for (int i = 7; i >= 0; i--) {
        binario += (bitRead(number, i));
      }
      Serial.println("Decimal: " + String(number));
      Serial.println("Equivalente en binario: " + binario);

      for (int i = 0; i < 8; i++) {
        //bitread(numero que queremos representar, posicion del bit que queremos leer)
        digitalWrite(leds[i], bitRead(number, 7 - i));
      }
    } else {
      Serial.println("Número fuera de rango. Ingrese un número entre 0 y 255.");
    }
  }
  //delay(700);
}