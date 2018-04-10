#include <Adafruit_Sensor.h>

#include "DHT.h"

#define DHTPIN 8
#define DHTTYPE DHT11 //have dht11 type; not 22 or 21
//int HTout = 8; //output from humidity/temp sensor on pin 8

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println("DHT11 output:");

  dht.begin();
  
  //pinMode(HTout, INPUT);
  //hahaha im funny the output variable is really input hahahaha please laugh
}

void loop() {
  /*
   * int HTreading = digitalRead(HTout);
   * Serial.println(HTreading);
   */

   float hum = dht.readHumidity();
   float temp = dht.readTemperature();
   float fahr = dht.readTemperature(true); //isFahrenheit = true

   if (isnan(hum) || isnan(temp) || isnan(fahr)) {
    Serial.println("Failed read.");
    return;
   }

   float hic = dht.computeHeatIndex(temp, hum, false); //isFahrenheit = false
   float hif = dht.computeHeatIndex(fahr, hum);

   Serial.print("Humidity: ");
   Serial.print(hum);
   Serial.print("%\t Temperature: ");
   Serial.print(temp);
   Serial.print("C (");
   Serial.print(fahr);
   Serial.print("F) \t Heat Index: ");
   Serial.print(hic);
   Serial.print("*C (");
   Serial.print(hif);
   Serial.println("*F)");
   delay(1000);
}
