'''
@Description: wifi_server.py
@Version: new
@Autor: maxin
@Date: 2020-07-12 13:56:01
@LastEditors: maxin
@LastEditTime: 2020-07-12 13:59:24
'''
import network as n
import socket
import time

SSID = "TP-LINK_A377"  # WiFi名
PASSWORD = "majunhu1975"  # WiFi密码
port = 6000  # 服务器端口
wlan = None
listenSocket = None


def connectWifi(ssid, passwd):
    global wlan
    wlan = n.WLAN(n.STA_IF)
    wlan.active(True)
    # 关闭连接，确保没有任何连接，以免失败
    wlan.disconnect()
    wlan.connect(ssid, passwd)
    while(wlan.ifconfig()[0] == '0.0.0.0'):
        time.sleep(1)
    return True


# 用try的方法确保保持连接
try:
    connectWifi(SSID, PASSWORD)
    # 获得IP地址
    ip = wlan.ifconfig()[0]
    # 建立Socket连接
    listenSocket = socket.socket()
    # 绑定IP地址
    listenSocket.bind((ip, port))
    print("TCP SERVER IP:", ip, ":", port)
    # Socket属性
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 侦听
    listenSocket.listen(1)
    print('TCP waiting...')
    while True:
        print("Accepting.....")
        # 获取客户端信息
        conn, addr = listenSocket.accept()
        print(addr, "Connected")
        while True:
            data = conn.recv(1024)
            if(len(data) == 0):
                print("Close socket")  # 无数据关闭Socket
                conn.close()
                break
            print(data)
            conn.send(data)  # 原样发回
except all:
    if(listenSocket):
        listenSocket.close()
    wlan.disconnect()
    wlan.active(False)
