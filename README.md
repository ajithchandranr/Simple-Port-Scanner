# Simple Port Scanner

The Simple Port Scanner is a Python script that allows you to scan for open ports on a target host. It provides a basic and straightforward way to identify open ports and can be used for network analysis or security testing.

## Features

- Scans a range of ports on a target host
- Identifies open ports through TCP connection attempts
- Lightweight and easy to use

## Prerequisites

Before running the port scanner, ensure that you have the following prerequisites:

- Python installed on your system (https://www.python.org)
- Required Python libraries (socket, argparse)

## Usage

To use the Simple Port Scanner, follow these steps:

1. Clone or download the repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the `port_scanner.py` file is located.

3. Run the following command:

   ```
   python port_scanner.py <target_host> <start_port> <end_port>
   ```

   - Replace `<target_host>` with the IP address or hostname of the target machine.
   - Replace `<start_port>` and `<end_port>` with the range of ports you want to scan.

4. The port scanner will attempt a TCP connection to each port within the specified range and display the open ports.

## Example

Here's an example command to scan ports 1 to 100 on a target machine with IP address 192.168.0.1:

```
python port_scanner.py 192.168.0.1 1 100
```

## License


```
This project is licensed under the MIT License.
```

## Contact

e-mail     : ajithchandranr@protonmail.com 

linkedin  : https://www.linkedin.com/in/ajithchandranr/
