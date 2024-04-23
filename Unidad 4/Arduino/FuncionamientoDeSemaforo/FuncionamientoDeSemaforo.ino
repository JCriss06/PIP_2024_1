int led[] = { 2, 3, 4 };
int parpadeo[] = { HIGH, LOW, HIGH, LOW, HIGH, LOW, HIGH, LOW };


void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 3; i++) {
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(20);
}

void loop() {
  // put your main code here, to run repeatedly:
  //verde
  digitalWrite(led[0], HIGH);
  digitalWrite(led[1], LOW);
  digitalWrite(led[2], LOW);
  delay(5000);

  for (int i = 0; i < 8; i++) {
    digitalWrite(led[0], parpadeo[i]); 
    delay(200);
  }

  // amarillo
  digitalWrite(led[0], LOW);
  digitalWrite(led[1], HIGH);
  digitalWrite(led[2], LOW);
  delay(3000);

  for (int i = 0; i < 8; i++) {
    digitalWrite(led[1], parpadeo[i]);  
    delay(200);
  }

  //rojo
  digitalWrite(led[0], LOW);
  digitalWrite(led[1], LOW);
  digitalWrite(led[2], HIGH);
  delay(5000);

  for (int i = 0; i < 8; i++) {
    digitalWrite(led[2], parpadeo[i]);  
    delay(200);
  }
}