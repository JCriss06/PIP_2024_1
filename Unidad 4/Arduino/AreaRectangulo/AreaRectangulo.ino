int estado = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

double base, altura, resultado;

void loop() {
  // put your main code here, to run repeatedly:
  if (estado == 0) {
    if (Serial.available() > 0) {
      base = Serial.readString().toDouble();
      estado++;
    }
  } else if (estado == 1) {
    if (Serial.available() > 0) {
      altura = Serial.readString().toDouble();
      estado++;
    }
  } else if (estado == 2) {
    resultado = base * altura;
    Serial.println("El area del rectangulo es: " + String(resultado));
    estado = 0;    
  
  }
  delay(100);
}
