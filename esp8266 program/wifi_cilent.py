
'''
@Description: wifi_connect,py
@Version: 1.0
@Autor: maxin
@Date: 2020-07-10 19:51:38
@LastEditors: maxin
@LastEditTime: 2020-07-12 13:51:47
'''
import socket
import time

import network as n

SSID = "TP-LINK_A377"  # WiFi名
PASSWORD = "majunhu1975"  # WiFi密码
host = "192.168.2.106"  # 服务器IP地址
port = 5000  # 服务器端口
wlan = None
s = None


def connectWifi(ssid, passwd):
    global wlan
    wlan = n.WLAN(n.STA_IF)
    wlan.active(True)  # 关闭连接，确保没有任何连接，以免失败
    wlan.disconnect()
    wlan.connect(ssid, passwd)  # 确保WiFi连接成功
    while(wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    return True


# 用try的方法确保保持连接
try:
    connectWifi(SSID, PASSWORD)
    s = socket.socket()  # 建立socket连接
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Socket属性
    s.connect((host, port))  # 连接服务器
    print("TCP Connected to:", host, ":", port)  # 发送数据
    while True:
        data = s.recv(1024)
        if(len(data) == 0):  # 无数据关闭Socket
            print("Close socket")
            s.close()
            break
        print(data)
        ret = s.send(data)  # 数据原样发回
except all:
    if (s):
        s.close()
    wlan.disconnect()
    wlan.active(False)
