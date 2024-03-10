from ipaddress import*

k = 0
net = ip_network('154.24.165.32/255.255.255.224', 0)
for ip in net:
    b = f'{ip:b}'
    if b[:16].count('1') < b[16:].count('1'):
        k += 1
print(k)
