from scapy.layers.inet import IP
from scapy.all import sr
from scapy.layers.inet import TCP
from scapy.layers.inet import UDP
from scapy.layers.dns import DNS, DNSQR
import ipaddress

host = input("Enter IP Address: ") 
ports = [25,80,53,443,445,8080,8443]

def SynScan(host):
    ans,unans = sr(IP(dst=host)/TCP(sport=33333,dport=ports,flags="S"),timeout=2, verbose=0)
    print("Open ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA":
            print(s[TCP].dport)
def DNSScan(host):
    ans,unans = sr(IP(dst=host)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="google.com")),timeout=2,verbose=0)
    if ans and ans[UDP]:
        print("DNS Server at %s"%host)

try:
    ipaddress.ip_address(host)
except:
    print("Invalid address")
    exit(-1)
SynScan(host)
DNSScan(host)