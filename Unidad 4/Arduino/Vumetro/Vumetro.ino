//simulador de un vumetro
int leds[] = { 2, 3, 4, 5, 6, 7, 8, 9 };
int potenciometro = A0;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

int valor;
int posicionled;

void loop() {
  //0 - 1023 es del convertidor analogo digital de arduino
  valor = analogRead(potenciometro);
  posicionled = map(valor, 0, 1023, 0, 255);

  Serial.println("Valor del potenciometro: " + String(valor));
  Serial.println("Posicion al que pertenece led: " + String(posicionled));

  for (int i = 0; i < 8; i++) {
    if (i < posicionled) {
      digitalWrite(leds[i], HIGH);
    } else {
      digitalWrite(leds[i], LOW); 
    }
  }
  delay(10);
}