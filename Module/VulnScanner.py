"""This scans for the common web vulnerabilities"""
import requests

#Function to check for SQL Injection vulnerabilities

def checkSQLINJ(url):
    testPayload = "' OR '1'='1' -- " #A common SQL injection Payload
    response = requests.get(url +testPayload)
    if "error" in response.text.lower():
        #If there is error in resposne, then there is a possibilty of SQL Injection
        print(f"[+] Possible SQL Injection vulnerability found at {url}")

#Function to run vulnerability scnas

def vulScanner(url):
    print(f"[*] Scanning {url} for vulnerabilities...")
    checkSQLINJ(url)

if __name__ =="__main__":
    targetURL = input("Enter target URL: ")
    vulScanner(targetURL)
    