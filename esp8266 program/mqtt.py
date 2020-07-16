'''
@Description: mqtt服务代码
@Version: new
@Autor: maxin
@Date: 2020-07-16 17:40:47
@LastEditors: maxin
@LastEditTime: 2020-07-16 19:36:42
'''
import time

import network as n
import simple
from machine import Pin

p4 = Pin(4, Pin.OUT)  # 板载led灯
p4.value(1)

WIFI_SSID = "TP-LINK_A377"  # WiFi名
WIFI_PASSWORD = "majunhu1975"  # WiFi密码
MQTT_SERVER = "81.70.32.13"       # mqtt服务器的IP
CLIENT_ID = "zhenjiu_esp826"  # 设备ID
TOPIC = b"test"  # 设备订阅的主题 客户端推送消息的主题
TOPIC2 = b"ledled"  # 手机客户端订阅的主题  设备推送消息的主题
username = 'esp8266_1'  # 用户名
password = '1501655237'  # 密码
mqtt_connect = None


def connectWifi(ssid, passwd):
    global wlan
    wlan = n.WLAN(n.STA_IF)
    wlan.active(True)  # 关闭连接，确保没有任何连接，以免失败
    wlan.disconnect()
    wlan.connect(ssid, passwd)  # 确保WiFi连接成功
    while(wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    p4.value(0)
    return True


def sub_cb(topic, msg):
    global state
    print((topic, msg))


try:
    connectWifi(WIFI_SSID, WIFI_PASSWORD)  # 连接wifi
    mqtt_connect = simple.MQTTClient(
        CLIENT_ID, MQTT_SERVER, 0, username, password)  # 设置mqtt连接参数
    mqtt_connect.set_callback(sub_cb)  # 设置接收成功回调函数
    mqtt_connect.connect()  # 建立连接
    mqtt_connect.subscribe(TOPIC)  # 设置消息订阅
    print("Connected to %s, subscribed to %s topic" % (MQTT_SERVER, TOPIC))

    while True:
        mqtt_connect.wait_msg()
except all:
    if(mqtt_connect is not None):
        mqtt_connect.disconnect()
    wlan.disconnect()
    wlan.active(False)
