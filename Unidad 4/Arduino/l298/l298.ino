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
    digitalWrite(in1, v);
    digitalWrite(in2, v);
  }
  delay(100);
}
