# Network Port Scanner
This Python script is a simple network port scanner that allows you to check if specific ports on a target host are open or closed. It also retrieves your public IP address using the "ipinfo.io" API.

Please note that using such a tool on networks and systems you don't own or have explicit permission to scan is considered unethical and potentially illegal. Always ensure that you have the proper authorization before scanning any network.

## Usage
  1. Run the script using Python 3.x.
  ```bash
    python port_scanner.py
  ```

  2. The script will prompt you for the following information:
    - Target host (IP address or domain name): Enter the IP address or domain name of the target you want to scan.
    - Starting range of ports (minimum 1): Enter the starting port number for the scan.
    - Ending range of ports (maximum 65536): Enter the ending port number for the scan. Note that it will scan ports from the starting range up to, but not including, the ending range.
  
  3. The script will then start scanning the specified range of ports on the target host, indicating whether each port is open or closed.
  
  4. After completing the scan, you will be prompted to either continue or exit the tool.

## Requirements
  - Python 3.x
  - Requests library (install using pip install requests)

## Author
  This script was created by Technobeast (@TechnobeastOP on Telegram).

## Disclaimer

Warning: This tool should only be used for legitimate and authorized purposes, such as network administration and security testing. Unauthorized scanning of networks or systems is illegal and unethical. Always obtain proper authorization before scanning any network. The author and the script are not responsible for any misuse or illegal activities.
