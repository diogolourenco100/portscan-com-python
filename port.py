import socket

ip = input("Enter the target: ")
ports = [20, 21, 22, 23, 24, 25, 26, 80, 110, 111, 123, 443, 993, 994, 3306]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.4)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"{port} =====>>>>> [OPEN!]")
    else:
        print(f"{port} CLOSED!")
    s.close()
    print("")
