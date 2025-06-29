import subprocess
import ipaddress
from time import sleep

MAX_TENTATIVAS = 3
tentativas = 0

while tentativas < MAX_TENTATIVAS:
    ip = input("[+] Digite o IP: ").strip()
    try:
        verificar = ipaddress.ip_address(ip)
        break
    except ValueError:
        tentativas += 1
        print(f"[-] IP inválido! Tentativa {tentativas} de {MAX_TENTATIVAS}.")
        if tentativas == MAX_TENTATIVAS:
            print("[-] TENTATIVAS ESGOTADAS! Encerrando...")
            exit()


portas = input("[+] Quais portas serão escaneadas (ex: 22,80,443): ").strip()

print(f"[*] Escaneando o IP {ip} (IPv{verificar.version})...")
sleep(1)

comando = ["nmap", "-sS", "-p", portas, ip]
if verificar.version == 6:
    comando.insert(1, "-6")


resultado = subprocess.run(comando, capture_output=True, text=True)

print("[*] Resultados:")
for linha in resultado.stdout.splitlines():
    if "open" in linha:
        print(f"[+] Porta aberta encontrada: {linha}")