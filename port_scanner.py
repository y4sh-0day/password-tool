import socket

# ===== SCAN ONE PORT =====
def scan_port(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return "OPEN"
        else:
            return "CLOSED"
    except:
        return "ERROR"

# ===== PORT NAMES =====
port_names = {
    80: "HTTP",
    443: "HTTPS",
    21: "FTP",
    22: "SSH",
    25: "SMTP Email",
    3306: "MySQL Database",
    8080: "Web Server",
    53: "DNS",
    110: "POP3 Email",
    23: "Telnet"
}

# ===== MAIN PROGRAM =====
host = input("Enter website to scan: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning " + host + "...")
print("-------------------")

open_ports = []

for port in range(start_port, end_port + 1):
    result = scan_port(host, port)
    if result == "OPEN":
        open_ports.append(port)
        if port in port_names:
            name = port_names[port]
        else:
            name = "Unknown"
        print("Port " + str(port) + " (" + name + ") → OPEN ✓")

print("-------------------")
print("Scan complete!")
print("Total open ports: " + str(len(open_ports)))
