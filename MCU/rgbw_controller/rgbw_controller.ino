#include <Arduino.h>
#include <WiFi.h>
#include <math.h>
#include <PubSubClient.h>
#include "connections.hpp"
#include "secrets.h"

//PubSubClient mqtt_client();

#define pwm_frequency 5000
#define pwm_resolution 10

#define red_ch 0
#define green_ch 1
#define blue_ch 2
#define white_ch 3

void setup(){
  Serial.begin(115200);
    // Configuring PWM for RGBW
    
    ledcSetup(0, pwm_frequency, pwm_resolution);
    ledcSetup(1, pwm_frequency, pwm_resolution);
    ledcSetup(2, pwm_frequency, pwm_resolution);
    ledcSetup(3, pwm_frequency, pwm_resolution);

    ledcAttachPin(15, red_ch); //RED
    ledcAttachPin(4, green_ch);  //GREEN
    ledcAttachPin(18, blue_ch); //BLUE
    ledcAttachPin(19, white_ch); //WHITE

    // Configuring DMX
    pinMode(13, INPUT);  //RO - Receiver Input
    pinMode(12, OUTPUT); //RE - Receiver Enable
    pinMode(14, OUTPUT); //DE - Driver Enable
    pinMode(27, OUTPUT); //DI - Driver Output
    // Setting MAX485 to receive mode
    digitalWrite(14, HIGH); //DE
    digitalWrite(12, LOW);  //RE

    // Wi-Fi Connection
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    // MQTT Connection
    //mqtt_client.setServer(MQTT_SERVER, MQTT_PORT);
    //mqtt_client.connect("rgbw_controller");
    //mqtt_client.setCallback(mqtt_callback);
}

void loop(){
    Serial.println("HIGH");
    for(int i=0; i<(pow(2, pwm_resolution)-1); i++){
        ledcWrite(red_ch, i);
        delay(5);
    }
    for(int i=0; i<(pow(2, pwm_resolution)-1); i++){
        ledcWrite(green_ch, i);
        delay(5);
    }
    for(int i=0; i<(pow(2, pwm_resolution)-1); i++){
        ledcWrite(blue_ch, i);
        delay(5);
    }
    for(int i=0; i<(pow(2, pwm_resolution)-1); i++){
        ledcWrite(white_ch, i);
        delay(5);
    }

    delay(1000);
    Serial.println("LOW");
     

    for(int i=pow(2, pwm_resolution)-1; i>=0; i--){
        ledcWrite(red_ch, i);
        delay(5);
    }
    for(int i=pow(2, pwm_resolution)-1; i>=0; i--){
        ledcWrite(green_ch, i);
        delay(5);
    }
    for(int i=pow(2, pwm_resolution)-1; i>=0; i--){
        ledcWrite(blue_ch, i);
        delay(5);
    }
    for(int i=pow(2, pwm_resolution)-1; i>=0; i--){
        ledcWrite(white_ch, i);
        delay(5);
    }
    delay(1000);

}
