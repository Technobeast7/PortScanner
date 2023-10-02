import socket
import requests
import time
import os

from exceptions import RequestError, IPDetailsError

# Fetch Public IP
def get_public_ip():
    try:
        response = requests.get("https://ipinfo.io")
        if response.status_code == 200:
            data = response.json()
            return data.get('ip')
        else:
            print("Unable to retrieve IP address.")
    except requests.exceptions.RequestException as e:
        raise RequestError("Failed to retrieve public IP")
    except json.JSONDecodeError as e:
        raise IPDetailsError("Failed to parse JSON response")

def scan_port(host, port):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt (adjust as needed)
        s.settimeout(1)
        
        # Attempt to connect to the host and port
        s.connect((host, port))
        
        # If the connection is successful, the port is open
        print(f"Port {port} is open.")
        
        # Close the socket
        s.close()
        
    except (socket.timeout, ConnectionRefusedError):
        # If the connection times out or is refused, the port is closed
        print(f"Port {port} is closed")
        
def check_command():
    command = input("Want To Continue? (y,n): ")
    if command == "y":
        print("Restarting the Tool...")
        time.sleep(1)
        Main()
    elif command == "n":
        print("Closing The Tool...")
    else:
        print("The Only Options are y for yes and n for no")
        check_command()

def main():
    os.system("cls")
    print("""
        ░▒█▀▀█░▒█▀▀▀█░▒█▀▀▄░▀▀█▀▀░▒█▀▀▀█░▒█▀▀▄░█▀▀▄░▒█▄░▒█░▒█▄░▒█░▒█▀▀▀░▒█▀▀▄
        ░▒█▄▄█░▒█░░▒█░▒█▄▄▀░░▒█░░░░▀▀▀▄▄░▒█░░░▒█▄▄█░▒█▒█▒█░▒█▒█▒█░▒█▀▀▀░▒█▄▄▀
        ░▒█░░░░▒█▄▄▄█░▒█░▒█░░▒█░░░▒█▄▄▄█░▒█▄▄▀▒█░▒█░▒█░░▀█░▒█░░▀█░▒█▄▄▄░▒█░▒█
        
    By Technobeast (@TechnobeastOP on Telegram)                               2023

Warning: using such a tool on networks and systems you don't own or have explicit permission to scan is considered unethical and potentially illegal. Always ensure that you have the proper authorization before scanning any network.
""")
    print(f"Your Public IP Address Is: {get_public_ip()}\n")
    host = input("Enter the target host (IP address or domain): ")
    rangeS = input("Enter Starting Range Of Ports (minimum 1): ")
    print("Note: If you entered 5 as starting rage of ports and 10 in ending range of ports then it will show up ports 5 to 9")
    rangeE = input("Enter Ending Rage Of Ports (maximum 65536): ")
    ports = range(int(rangeS), int(rangeE))  # You can adjust the port range as needed
    
    for port in ports:
        scan_port(host, port)
        
    check_command()

if __name__ == "__main__":
    main()
    
# Created by Technobeast :)