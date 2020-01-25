
import subprocess
import optparse
import re

def get_arguments():
    # allow me to parse out arguments/options/flags from the command line.
    parser = optparse.OptionParser()  # optparse is depreciated, refactor with argparse at some point.
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address, like eth0.")
    parser.add_option("-m", "--mac", dest="new_mac", help="Input a desired MAC address")
    (options, arguments) = parser.parse_args()
    # conditionals in case user forgets to enter one of the two args.
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info. ")
    elif not options.new_mac:
        parser.error("[-] Please specify a new MAC Address, use --help for more info. ")
    return options

def change_mac(interface, new_mac):
    # sanity check print statement
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # the actual script
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    # check to make sure the MAC change worked.
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    print(ifconfig_result)

    # using regex to check what the new MAC address is
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    # check to see if there is a MAC address at all
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] sorry, could not get MAC address")

# invoke the get args function.
options = get_arguments()

#Feedback for the end user.
current_mac = get_current_mac(options.interface)
print("Current MAC => " + str(current_mac))

# invoke the script function.
change_mac(options.interface, options.new_mac)

# check that the current MAC is the same as the user requested.
current_mac = get_current_mac((options.interface))
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed")
