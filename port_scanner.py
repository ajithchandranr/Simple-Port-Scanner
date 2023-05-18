import socket
import argparse

def scan_ports(target_host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Adjust the timeout as needed

        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", type=str, help="Target host to scan")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")

    args = parser.parse_args()

    scan_ports(args.host, args.start_port, args.end_port)
