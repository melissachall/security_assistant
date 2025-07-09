import subprocess

def scan_network(ip_range):
    """
    Scanne une plage d'adresses (ex: 192.168.1) et retourne la liste des hôtes actifs.
    ip_range: chaîne de base ex: '192.168.1'
    """
    active_hosts = []
    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        try:
            result = subprocess.run(["ping", "-n", "1", "-W", "1000", ip], stdout=subprocess.DEVNULL)
            if result.returncode == 0:
                active_hosts.append(ip)
        except Exception:
            pass
    return active_hosts