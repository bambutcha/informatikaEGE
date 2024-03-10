from ipaddress import*

k= 0
net = ip_network('10.0.0.160/255.255.255.224',0)
for ip in net:
    if f'{ip:b}'.count('1')%2 == 0:
        k+=1
print(k)


