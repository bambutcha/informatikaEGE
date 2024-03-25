from ipaddress import *
k= []
net = ip_network('124.6.101.0/255.255.254.0', 0)
for ip in net:
    c = f'{ip:b}'.count('0')
    k.append(c)
print(max(k))


