import socket

def identify_services(ip, open_ports):
    """
    Identifie les services qui s'exécutent sur les ports ouverts d'une adresse IP.
    :param ip: Adresse IP de la machine
    :param open_ports: Liste des ports ouverts
    :return: Dictionnaire des services identifiés avec des informations de version (si disponibles)
    """
    services_info = {}

    for port in open_ports:
        service_info = {"port": port}
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                s.connect((ip, port))
                s.sendall(b"GET / HTTP/1.1\r\n\r\n")  # Envoyer une requête pour obtenir une réponse du service
                response = s.recv(1024).decode("utf-8")
                service_info["banner"] = response.strip()
        except (socket.error, socket.timeout):
            pass

        services_info[port] = service_info

    return services_info
