from ipaddress import*

k= 0
net = ip_network('123.222.111.192/255.255.255.248',0)
for ip in net:
    if f'{ip:b}'[24:].count('1')%3 != 0:
        k+=1
print(k)


