import os
import sys
from scapy.all import sniff, IP, TCP

def display_disclaimer():
    """
    Display the disclaimer message for using the packet sniffer tool.
    The user must read and acknowledge this before using the tool.
    """
    print("------------------------ Packet Sniffer Tool Disclaimer ---------------------------")
    print("This packet sniffer tool is intended for educational and ethical purposes only.")
    print("Unauthorized use, distribution, or modification of this tool is strictly prohibited.")
    print("By using this tool, you agree to the following terms and conditions:")
    print("\n1. You will only use this tool on networks and systems for which you have explicit permission.")
    print("2. You will not use this tool to violate any laws, regulations, or terms of service.")
    print("3. You will not use this tool to harm, disrupt, or exploit any networks or systems.")
    print("4. You will not use this tool to intercept, collect, or store any sensitive or confidential information.")
    print("5. You will not redistribute or sell this tool without the express permission of the author.")
    print("6. The author is not responsible for any damages or losses incurred as a result of using this tool.")
    print("7. You will respect the privacy and security of all networks and systems you interact with using this tool.")
    print("-----------------------------------------------------------------------------------")

def get_user_consent():
    """
    Prompt the user to accept the terms and conditions.
    If the user does not accept, the program terminates.
    """
    accept_terms = input("\nDo you accept these terms and conditions? (y/n): ").strip().lower()
    if accept_terms != 'y':
        print("You must accept the terms and conditions before using this tool.")
        sys.exit()

def save_packet_details(packet):
    """
    Extract details from a packet and save them to a file and print them to the console.
    Only processes TCP packets.
    
    Args:
        packet (scapy.packet): The packet to extract details from.
    """
    if packet.haslayer(TCP):
        # Extract packet details
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        protocol = packet[IP].proto
        payload = str(packet[TCP].payload)[:50]  # Limit payload to the first 50 chars

        output_string = (
            f"Source IP: {src_ip}\n"
            f"Destination IP: {dst_ip}\n"
            f"Source Port: {src_port}\n"
            f"Destination Port: {dst_port}\n"
            f"Protocol: {protocol}\n"
            f"Payload: {payload}...\n"
        )

        print(output_string, end='')

        with open('packet_sniffer_results.txt', 'a') as f:
            f.write(output_string)

def start_packet_sniffing(packet_count=10):
    """
    Start sniffing TCP packets and process them.

    Args:
        packet_count (int): The number of packets to sniff. Default is 10.
    """
    print("\n--------------- Packet Sniffing Tool ---------------")
    sniff(filter="tcp", prn=save_packet_details, store=0, count=packet_count)

def main():
    """
    Main function to run the packet sniffer tool.
    It displays a disclaimer, gets user consent, and starts sniffing packets.
    """
    display_disclaimer()
    get_user_consent()
    start_packet_sniffing()
    print("\nResults saved to: packet_sniffer_results.txt")

if _name_ == "_main_":
    main()