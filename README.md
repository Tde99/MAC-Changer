```text
  __  __    _    ____ _   _    _    _   _  ____ _____ ____  
 |  \/  |  / \  / ___| | | |  / \  | \ | |/ ___| ____|  _ \ 
 | |\/| | / _ \| |   | |_| | / _ \ |  \| | |  _|  _| | |_) |
 | |  | |/ ___ \ |___|  _  |/ ___ \| |\  | |_| | |___|  _ < 
 |_|  |_/_/   \_\____|_| |_/_/   \_\_| \_|\____|_____|_| \_\
```
MAC-Changer
A simple and effective Python automation tool to change your network interface's MAC address on Linux systems. It provides a menu-driven interface to randomize, manually set, or restore your MAC address to its original state.

**Features**
* **Random MAC:** Generate and apply a completely random MAC address.
* **Manual Entry:** Set a specific MAC address of your choice.
* **Restore Original:** Quickly revert the interface to its permanent/original hardware MAC.
* **Automated Interface Handling:** Automatically takes the interface (eth0) down and up during the change process.

* **Prerequisites**
The following tools are required for the script to function:
Python 3.x
Nmap & Macchanger: (The script uses macchanger command)

**Installation**

Clone the repository:
    * git clone [https://github.com/Tde99/MAC-Changer.git](https://github.com/Tde99/MAC-Changer.git)

Navigate to the directory:
   * cd MAC-Changer

Make the script executable:
   * chmod +x machanger.py

Usage
Since changing a MAC address requires administrative access, run with sudo:

sudo python3 machanger.py

Menu Options:
1. Random: Generates a random MAC for anonymity.
2. Decide: Allows you to type in a specific MAC address.
3. Return to Original: Reverts all changes back to the factory MAC.
Figlet: For the ASCII header.

Root Privileges: Changing network hardware settings requires sudo.
