from scapy.all import *


Qdsec  = DNSQR(qname="twysw.example.com")
dns    = DNS(id=0xAAAA, qr=0, qdcount=1, ancount=0,nscount=0, arcount=0, qd=Qdsec)
ip  = IP(dst="10.0.2.5",src = "10.0.2.4");
udp = UDP(dport=53, sport=33333, chksum=0)
request = ip/udp/dns

with open ("ip_req.bin", "wb") as f:
	f.write(bytes(request))

