//int leds[] = { 2, 3, 4, 5, 6, 7, 8, 9 };
//minusculas: 97 -122
//mayusculas: 65 - 90 
void setup() {
  // put your setup code here, to run once:
  // for (int i = 0; i < 8; i++) {
  //   pinMODE(leds[i], OUTPUT);
  // }
  Serial.begin(9600);
}

char letra;

void loop() {
  if (Serial.available() > 0) {
    letra = Serial.read();
    if (letra != '\n') {  // Verifica si el carácter leído no es un salto de línea
      Serial.print("Letra: ");
      Serial.print(letra);
      Serial.print(", ASCII: ");
      Serial.print(int(letra));
      Serial.print(", Binario: ");
    
      for (int i = 7; i >= 0; i--) {
        Serial.print(bitRead(letra, i));
      }
      Serial.println();
    }
  }
}
