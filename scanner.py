import argparse
import socket
import time
from concurrent.futures import ThreadPoolExecutor

open_ports = []

def service_name(port): #Fonction qui donne le nom des ports connue
    try:
        return socket.getservbyname(port)
    except OSError:
        return "unidentified"

def port_scan(target, port, timeout=1): #Fonction qui scan le port du target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((target, port))
    s.close()
    if result == 0:
        service = service_name(port)
        open_ports.append((port, service))
    print("Port "+ str(port) + " is open (" + str(service) + ")")

def start_scan(target, start, end, threads, timeout=1):     #Fonction qui permet de tester la validité du target et de lancé le scan sur la plage donnée
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname : " + str(target) +" could not be resolved")
        return

    print("Starting port scanning (" + str(target) + ")")
    print(f"Ports {start} to {end} | {threads} threads\n")
    start_chrono = time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(start, end+1):
            executor.submit(port_scan, ip, port, timeout)
    duration = time.time() - start_chrono

    print(f"Scan completed in : {duration:.2f} seconds")
    print(f"{len(open_ports)} open ports")

def main():     #pour déclancher le programme avec les arguments
    parser = argparse.ArgumentParser(description="Scanner de ports TCP multi-threads")
    parser.add_argument("-t", "--target", help="Target IP or domain name")
    parser.add_argument("-s", "--start", type=int, default=1, help="Starting port")
    parser.add_argument("-e", "--end", type=int, default=65536, help="Ending port")
    parser.add_argument("-n", "--threads", type=int, default=100, help="Number of threads")
    args = parser.parse_args()

    try:
        start_scan(args.target, args.start, args.end, args.threads, args.timeout)
    except KeyboardInterrupt: #Stopping the scan with CTRL+C
        print("Scan interrupted by user")

if __name__ == "__main__": #Fait en sorte que le programme ne lance pas le scan en cas d'importe et se lance qui si le programme est lancé directement
    main()
