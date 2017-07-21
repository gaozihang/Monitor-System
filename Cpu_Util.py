#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wmi
import time
import requests

c = wmi.WMI()
mac = 0
ip = 0
util = 0

def cpu_use():
    global util
    for cpu in c.Win32_Processor():
        timestamp = time.strftime('%a, %d %b %Y %H:%M:%S', time.localtime())
        print('%s | Utilization: %s: %d %%' % (timestamp, cpu.DeviceID, cpu.LoadPercentage))
        util = cpu.LoadPercentage

def network():
    global mac, ip
    interface = c.Win32_NetworkAdapterConfiguration(IPEnabled=1)[2]
    mac = interface.MACAddress
    print("MAC: %s" % interface.MACAddress)
    ip_address = interface.IPAddress[0]
    ip = ip_address
    print("ip_add: %s" % ip_address)

if __name__ == '__main__':
    while True:
        network()
        cpu_use()
        #url = 'http://192.168.1.249:8000/cmdb/monitor/upload'
        url = 'http://106.14.15.58/cmdb/monitor/upload'
        d = {'ip':ip, 'mac':mac, 'util':util}
        r = requests.post(url, d)
        print(r.text)
        time.sleep(1)
