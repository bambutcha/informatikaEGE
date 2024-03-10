from ipaddress import *

for A in range(0, 256):
	f= False
	net = ip_network(f'243.46.4.198/255.255.{A}.0', 0)
	for ip in net:
		ip2 = f'{ip:b}'
		if ip2[:16].count('0') <= ip2[16:].count('0'):
			f= True
	if f:
		print(ip)
