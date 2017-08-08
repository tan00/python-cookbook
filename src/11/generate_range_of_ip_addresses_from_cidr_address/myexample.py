import ipaddress

net = ipaddress.ip_network('123.45.67.64/27')
for ip in net:
     print(ip)

a = ipaddress.ip_address('123.45.67.69')
print( a in net )


net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for ip6 in net6:
     print(ip6)