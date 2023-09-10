#include <Arduino.h>
#include <DmxSimple.h>
#include "secrets.h"

void setup(){
    pinMode(15, OUTPUT); //RED
    pinMode(4, OUTPUT);  //GREEN
    pinMode(18, OUTPUT); //BLUE
    pinMode(19, OUTPUT); //WHITE

    // Configuring DMX
    pinMode(13, INPUT);  //RO - Receiver Input
    pinMode(12, OUTPUT); //RE - Receiver Enable
    pinMode(14, OUTPUT); //DE - Driver Enable
    pinMode(27, OUTPUT); //DI - Driver Output
    // Setting MAX485 to receive mode
    digitalWrite(14, HIGH); //DE
    digitalWrite(12, LOW);  //RE

    // Wi-Fi Connection
    Wifi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (Wifi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    // MQTT Connection

}

void loop(){

}
