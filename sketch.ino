#define R 2
#define Y 4
#define G 7
#define B 8
#define W 12

const int leds[5] =
  { R, Y, G, B, W };

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], 0);
  }
}

void loop() {
  while (!Serial.available()) {}
  byte x = Serial.parseInt();

       if (x == 10) digitalWrite(R, 0);
  else if (x == 11) digitalWrite(R, 1);

  else if (x == 20) digitalWrite(Y, 0);
  else if (x == 21) digitalWrite(Y, 1);

  else if (x == 30) digitalWrite(G, 0);
  else if (x == 31) digitalWrite(G, 1);

  else if (x == 40) digitalWrite(B, 0);
  else if (x == 41) digitalWrite(B, 1);

  else if (x == 50) digitalWrite(W, 0);
  else if (x == 51) digitalWrite(W, 1);

  else if (x > 0 && x < 6) {
    int l;
    switch (x) {
      case 1: l = R; break;
      case 2: l = Y; break;
      case 3: l = G; break;
      case 4: l = B; break;
      case 5: l = W; break;
    }
    Serial.print(digitalRead(l));
  }
}
