int leds[] = { 2, 3, 4, 5, 6, 7, 8, 9 };

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i = 1; i <= 255; i++) {
    for (int j = 0; j < 8; j++) {
      digitalWrite(leds[j], bitRead(i, j));  //enciende o apaga el led segun el bit en la posicion j
    }

    String binario = "";
      for (int x = 7; x >= 0; x--) {
        binario += (bitRead(i, x));
      }
      
    Serial.println("Valor: " + String(i)+ " ("+ binario +")");
    delay(800);
  }
}
