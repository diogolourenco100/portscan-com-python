import socket
from tqdm import tqdm

ip = input("Digite o IP/URL do alvo: ")
ports_open = []

# MUDE O VALOR DE 'range' PARA O VALOR DE PORTAS DESEJADO PARA ESCANEAR
for port in tqdm(range(100)):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.4)
    result = s.connect_ex((ip, port))
    if result == 0:
        ports_open.append(port)
    s.close()

size = len(ports_open)
i=0
while i == 0:
    op = input("\nDeseja ver a lista de portas abertas? y/n \n$ ")
    op.lower()
    
    if op == 'y':
        i+=1
        print(f"\n{size} portas abertas")
        print('-----------------')
        for port in ports_open:
            print(f'{port} open/aberta')
    
    elif op == 'n':
        i+=1
        print("\nOk.\n")
    
    else:
        i+=0
        print("\nResposta inválida. Tente novamente.\n")
