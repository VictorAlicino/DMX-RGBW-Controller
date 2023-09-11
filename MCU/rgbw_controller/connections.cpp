#include <Arduino.h>

void mqtt_callback(char* topic, byte* message, unsigned int length){
    ESP_LOGD(TAG, "Data Received");

    String sub_topic = "rgbw";
    if(!strcmp(topic, sub_topic.c_str())){
        char buffer[length + 1];
        for(int i = 0; i < length; i++) {
            buffer[i] = message[i];
        }
        buffer[length] = '\0';
    }
}

String get_mac_address(){
    uint8_t baseMac[6];
    //Get MAC address for Wi-Fi station
    esp_read_mac(baseMac, ESP_MAC_WIFI_STA);
    char baseMacChr[18] = {0};
    sprintf(baseMacChr, "%02X:%02X:%02X:%02X:%02X:%02X", baseMac[0], baseMac[1], baseMac[2], baseMac[3], baseMac[4], baseMac[5]);
    return {baseMacChr};
}
