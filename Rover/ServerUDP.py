import socket

# Set up the UDP server
rpi_ip = "127.0.0.1"   # The IP address where the server listens
rpi_port = 2222       # The port on which the server listens

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((rpi_ip, rpi_port))

print("UDP server listening on {}:{}".format(rpi_ip, rpi_port))


while True:
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print("Received message:", data.decode(), "from", addr)

