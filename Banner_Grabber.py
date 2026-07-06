import socket

target_ip = input("Enter IP: ")
target_port = int(input("Enter Port: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((target_ip, target_port))

    s.send(b"HEAD / HTTP/1.1\r\n\r\n") 
    banner = s.recv(1024)
    print(f"Grabbed banner: {banner.decode().strip()}")
except Exception as e:
    print(f"Could not grab banner: {e}")
finally:
    s.close()