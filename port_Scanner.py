import subprocess
import ipaddress
import time
from time import sleep

control = 1
while control < 4:
    try:
        ip = input("[+] Digite o ip:").strip()
        verificar = ipaddress.ip_address(ip)
        break
    except ValueError:
        print("[-]INVALIDO!!Digite em Numeros,e conforme a sintaxe do IP")
        print(f"São 3 tentativas,total de tentativas: {control} ")
        control += 1
    if control == 4:
        print("TENTATIVAS ESGOTADAS!!!")
        exit()
try:
    portas = input("Qual portas serão scaneadas: ")
except ValueError:
    print("Invalido!!, Digite um numero correto")
if verificar.version == 6:
    print(f"[*]Escaneando o ip: {ip}")
    sleep(2)
    scan = subprocess.run(["nmap","-6","-sS",f"-p {portas}",ip], capture_output=True, text=True)
    for linha in scan.stdout.splitlines():
        if "open" in linha:
            print(f"[*] Porta Aberta Encontrada:{linha}")
            sleep(2)
if verificar.version == 4:
    print(f"[*]Escaneando o ip: {ip}")
    sleep(2)
    scan = subprocess.run(["nmap","-sS", f"-p {portas}", ip], capture_output=True, text=True)
    for linha in scan.stdout.splitlines():
        if "open" in linha:
            print(f"[*] Porta Aberta Encontrada:{linha}")
            sleep(2)





