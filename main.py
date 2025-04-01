"""Integration of all the modules into one toolkit"""

import os

def main():
    while True:
        print("\n🔹 PENETRATION TESTING TOOLKIT 🔹")
        print("1. Port Scanner")
        print("2. Brute-Force Attacker")
        print("3. Packet Sniffer")
        print("4. Subdomain Enumeration")
        print("5. Vulnerability Scanner")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            os.system("python Module/PortScanner.py")
        elif choice == "2":
            os.system("python Module/BruteForcer.py")
        elif choice == "3":
            os.system("python Module/PacketSniffer.py")
        elif choice == "4":
            os.system("python Module/SubdomainEnum.py")
        elif choice == "5":
            os.system("python Module/VulnScanner.py")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
