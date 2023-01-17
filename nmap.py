#!/usr/bin/python3

#first make sure you have nmap installed module on the attacking machine

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<------------------------------->")

ip_address=input("Enter Target IP : ")
print("The IP you enteered is:",ip_address)
type(ip_address)

resp = input("""\n Please enter the type of scan you want to run 
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan \n""")

print("You have selected option:",resp)

if resp=='1':
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Ports Open: ", scanner[ip_address]['TCP'].keys())
elif resp=='2':
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Ports Open: ", scanner[ip_address]['UDP'].keys())
elif resp=='3':
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_address,'1-1024','-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ",scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Ports Open: ", scanner[ip_address]['tcp'].keys())
else:
    print("Option Not Valid")

