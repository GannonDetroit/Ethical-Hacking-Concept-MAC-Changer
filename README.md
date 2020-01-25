# Ethical-Hacking-Concept-MAC-Changer

While there are several MAC Changer tools available on the net, I wanted to create a low-level one that will work for linux machines and is written using python (also using optparse and regex).

This tool is just a proof of concept and not intended to be used for any illegal or unethical activity. It should only be used on machines and networks that you as a user own and/or have written permission to use and access.

# Notes of use:

- user can add -i to input the interface that you want to change (this will usually be eth0 or wlan0 depending if you're on wifi or not).

    `"-i", "--interface", dest="interface", help="Interface to change its MAC address, like eth0."
    "-m", "--mac", dest="new_mac", help="Input a desired MAC address"`

- if you don't know what interfaces you can target:
    - on Linux and Mac use the `ifconfig` command.
    - on Windows use `ipconfig`

- use the -m command to enter in the new MAC address you want.

    - note from wikipedia on MAC address formatting:
    
    `Addresses can either be universally administered addresses (UAA) or locally administered addresses (LAA). A universally administered address is uniquely assigned to a device by its manufacturer. The first three octets (in transmission order) identify the organization that issued the identifier and are known as the organizationally unique identifier (OUI).[2] The remainder of the address (three octets for EUI-48 or five for EUI-64) are assigned by that organization in nearly any manner they please, subject to the constraint of uniqueness. A locally administered address is assigned to a device by a network administrator, overriding the burned-in address.`

    `Universally administered and locally administered addresses are distinguished by setting the second-least-significant bit of the first octet of the address. This bit is also referred to as the U/L bit, short for Universal/Local, which identifies how the address is administered. If the bit is 0, the address is universally administered. If it is 1, the address is locally administered. In the example address 06-00-00-00-00-00 the first octet is 06 (hex), the binary form of which is 00000110, where the second-least-significant bit is 1. Therefore, it is a locally administered address.[8] Another example that uses locally administered addresses is the DECnet protocol. The MAC address of the Ethernet interface is changed by the DECnet software to be AA-00-04-00-XX-YY where XX-YY reflects the DECnet network address xx.yy of the host. This eliminates the need for an address resolution protocol since the MAC address for any DECnet host can be simply determined.`
