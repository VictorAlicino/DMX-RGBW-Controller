#include <stdio.h>
#include "nvs_flash.h"
#include "wifi.hpp"
#include "esp_log.h"
#include "mqtt.hpp"
#include <esp_wifi.h>
#include "esp_wifi_types.h"

extern "C"
{
    void app_main(void);
}

void app_main(void)
{
    //Initialize NVS
    esp_err_t ret = nvs_flash_init();
    if (ret == ESP_ERR_NVS_NO_FREE_PAGES || ret == ESP_ERR_NVS_NEW_VERSION_FOUND) {
      ESP_ERROR_CHECK(nvs_flash_erase());
      ret = nvs_flash_init();
    }
    ESP_ERROR_CHECK(ret);

    // Connect to Wi-Fi
    bool is_wifi_connected = wifi_init_sta();

    uint8_t mac[6];
    esp_wifi_get_mac(WIFI_IF_STA, mac);
    ESP_LOGI("MAC address", "MAC address: %02x:%02x:%02x:%02x:%02x:%02x",
             mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);

    // Initialize MQTT
    mqtt_app_start();
}
