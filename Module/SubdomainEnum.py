import requests

def subdomainEnum(domain, wordlist):
    print(f"\n🔍 Scanning for subdomains of {domain}...\n")
    
    with open(wordlist, 'r') as file:
        for sub in file:
            sub = sub.strip()
            url = f"https://{sub}.{domain}"

            try:
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=5, verify=False)

                if response.status_code == 200:
                    print(f"[+] Found Subdomain: {url}")
                else:
                    print(f"[-] {url} returned status code {response.status_code}")

            except requests.exceptions.RequestException as e:
                print(f"[!] Error checking {url}: {e}")  # Print error if request fails

if __name__ == "__main__":
    targetDomain = input("Enter target domain: ")
    wordlist_path = input("Enter subdomain wordlist path: ")

    print("\n📌 Running Subdomain Enumeration...\n")
    subdomainEnum(targetDomain, wordlist_path)
    print("\n✅ Scan Complete!\n")
