#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet MACHANGER")
			print(""" 
Welcome to MAC Changer

1)Random
2)Decide
3)Return to Original

		""")
			secim = input("How do you want to change your MAC Address: ")
		
			if(secim == "1"):
				os.system("ifconfig eth0 down")
				os.system("macchanger -r eth0")
				os.system("ifconfig eth0 up")
				print("\n Changed")
				break
			elif(secim == "2"):
				newmac = input("Decide your new MAC address: ")
				os.system("ifconfig eth0 down")
				os.system("macchanger --mac " + newmac + " eth0 ")
				os.system("ifconfig eth0 up")
				print("\n Changed ")
				break
			elif(secim == "3"):
				os.system("ifconfig eth0 down")
				os.system("macchanger -p eth0")
				os.system("ifconfig eth0 up")
				print("\n Changed ")
				break
			else:
				print("\n Funny... Try Again:D")
				os.system(" python macchanger.py")
	except KeyboardInterrupt:
        	print("\nExiting....")			
if __name__ == "__main__":
	menu()
