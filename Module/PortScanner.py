import socket 
import threading
'''This scans open ports on the given target'''
#Function to scan a single port
def ScanPort(target, port):
    try:
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) #Timeout for the connection attempt
        result= sock.connect_ex((target,port)) # 0 = Open, else closed
        if result ==0:
            print(f"[+] Port {port} is open")
            sock.close()


    except Exception as e:
        print(f"[-] Error scanning the port {port}: {e}")

#Function to scan multiple ports using threading
def PortScanner(target, ports):
    print(f"[*] Scanning {target} for open ports..")
    threads=[]
    for i in ports:
        thread=threading.Thread(target=ScanPort,args=(target,i))
        thread.start()
        threads.append(thread)
    for i in threads:
        thread.join() #Waits for all the threads to finish
if __name__ == "__main__":
    target_ip=input("Enter the target IP: ")
    ports= range(1,1025) #Scans the first 1024 ports
    PortScanner(target_ip,ports)
