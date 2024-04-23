//simulador de un vumetro
int leds[] = { 2, 3, 4, 5, 6, 7, 8, 9 };
int potenciometro = A0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

int valor;
int posicionled;

void loop() {
  // put your main code here, to run repeatedly:
  //0 - 1023 es del convertidor analogo digital de arduino
  valor = analogRead(potenciometro);
  posicionled = map(valor, 0, 1023, 0, 255);  //el valor leido al numero de leds que se deben de encender

  Serial.println("Valor del potenciometro: " + String(valor));
  Serial.println("Posicion al que pertenece led: " + String(posicionled));

  for (int i = 0; i < 8; i++) {
    if (i < posicionled) {
      digitalWrite(leds[i], HIGH);  //analogWrite(leds[i], 255);
    } else {
      digitalWrite(leds[i], LOW);  //analogWrite(leds[i], 0);
    }
  }
  delay(10);
}
