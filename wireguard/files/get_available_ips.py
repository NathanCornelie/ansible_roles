from ipaddress import ip_address, ip_network
import re
import argparse

def extract_ips_from_file(file_path: str) -> list:
    ips = []
    # Define the regular expression pattern for extracting IP addresses
    address_pattern = re.compile(r'Address\s*=\s*(\d+\.\d+\.\d+\.\d+)')
    allowed_ips_pattern = re.compile(r'AllowedIPs\s*=\s*(\d+\.\d+\.\d+\.\d+)')

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Check for Address line
            match = address_pattern.search(line)
            if match:
                ips.append(match.group(1))
                continue  # Move to the next line

            # Check for AllowedIPs line
            match = allowed_ips_pattern.search(line)
            if match:
                ips.append(match.group(1))
    
    return ips



def get_available_ip(ip_range: str, used_ips: list[str],number:str) -> str:
    # Convert the IP range to a network object
    network = ip_network(ip_range)
    
    # Convert used IPs to a set of ip_address objects for faster lookup
    used_ips_set = set(ip_address(ip) for ip in used_ips)
    available_ips = []
    # Iterate over the IPs in the network
    for ip in network.hosts():
        if ip not in used_ips_set :
           available_ips.append(str(ip))
        if len(available_ips) == int(number): 
            return available_ips
    
    # If no available IP is found, return a message indicating that
    return "Not enough available IP in the range."





def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Return available IPs from vpn conf file")
    parser.add_argument('file_path', type=str, help='Path to the file containing IP addresses.')
    parser.add_argument('range', type=str, help='intance Ip range')
    parser.add_argument('number',type=int,help="number of IPs to generate")
    # Parse arguments
    args = parser.parse_args()
    
    # Extract IPs from the file
    ips = extract_ips_from_file(args.file_path)
    print(get_available_ip(args.range, ips,args.number))


if __name__ == '__main__':
    main()