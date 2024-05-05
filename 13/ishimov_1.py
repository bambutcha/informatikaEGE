from ipaddress import *
k = 0
net = ip_network('192.168.32.96/255.255.255.224',0)
for ip in net:
    ip2 = f'{ip:b}'
    if ip2.count('1') % 2 == 0:
        k += 1
print(k)
