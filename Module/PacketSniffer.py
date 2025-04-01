""" This captures the network packets on an interface"""

from scapy.all import sniff

#A callback function to handle captured packets

def PacketCallback(packet):
    print(packet.summary()) #this prints the packet details

# This function is to start packet sniffing on a given interface

def StartSniffing(interface):
    print(f"[*] Starting packet sniffing on {interface}")
    sniff(iface=interface, prn=PacketCallback,store=False) #Sniffs packets

if __name__=="__main__":
    interface = input("Enter network interface (e.g., eth0, wlan0, Wi-Fi): ")
    StartSniffing(interface)