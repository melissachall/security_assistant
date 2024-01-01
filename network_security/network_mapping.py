'''import networkx as nx
import matplotlib.pyplot as plt
from network_security import scan_network
from .configurations import NetworkConfiguration

def generate_network_map(ip_range):
    active_machines = scan_network(ip_range)
    
    G = nx.Graph()

    for machine in active_machines:
        G.add_node(machine)

    # Add edges or customize the graph further based on your logic

    pos = nx.spring_layout(G)  # You can use a different layout algorithm if needed
    nx.draw(G, pos, with_labels=True, font_weight='bold')

    # Save the network map as an image or render it in the Django template
    plt.savefig("network_map.png")

    return "network_map.png"  # Return the file path or data to be used in the template
    '''
# Assurez-vous d'utiliser une bibliothèque appropriée pour générer des cartes topologiques
# Le code ci-dessous est un exemple simple et peut nécessiter des adaptations en fonction de vos besoins.

import networkx as nx
import matplotlib.pyplot as plt
import socket

def generate_network_map(ip_range):
    G = nx.Graph()

    # Ajoutez des nœuds pour chaque adresse IP active sur le réseau
    active_machines = scan_network(ip_range)
    for ip in active_machines:
        G.add_node(ip)

    # Ajoutez des arêtes pour représenter les connexions entre les adresses IP
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 != node2:
                # Ajoutez une arête si la connexion entre les deux adresses IP est ouverte (par exemple, si le port 80 est ouvert)
                if check_connection(node1, node2):
                    G.add_edge(node1, node2)

    # Dessinez la carte topologique du réseau
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()

def check_connection(ip1, ip2, port=80, protocol=socket.SOCK_STREAM, timeout=2):
    """
    Vérifie si une connexion entre deux adresses IP est ouverte sur un port spécifié.
    :param ip1: Adresse IP du premier nœud
    :param ip2: Adresse IP du deuxième nœud
    :param port: Port sur lequel vérifier la connexion (par défaut : 80)
    :param protocol: Protocole de connexion (par défaut : socket.SOCK_STREAM pour TCP)
    :param timeout: Délai d'attente pour la connexion (par défaut : 2 secondes)
    :return: True si la connexion est ouverte, False sinon
    """
    try:
        with socket.socket(socket.AF_INET, protocol) as s:
            s.settimeout(timeout)
            s.connect((ip1, port))
            s.connect((ip2, port))
            return True
    except (socket.error, socket.timeout):
        return False

# Exemple d'utilisation avec le protocole TCP
ip1 = "192.168.1.1"
ip2 = "192.168.1.2"
if check_connection(ip1, ip2, port=80, protocol=socket.SOCK_STREAM, timeout=2):
    print(f"La connexion entre {ip1} et {ip2} sur le port 80 (TCP) est ouverte.")
else:
    print(f"La connexion entre {ip1} et {ip2} sur le port 80 (TCP) est fermée.")

# Exemple d'utilisation avec le protocole UDP
if check_connection(ip1, ip2, port=53, protocol=socket.SOCK_DGRAM, timeout=2):
    print(f"La connexion entre {ip1} et {ip2} sur le port 53 (UDP) est ouverte.")
else:
    print(f"La connexion entre {ip1} et {ip2} sur le port 53 (UDP) est fermée.")

# Importez scan_network depuis host_enumeration.py pour utiliser la fonction scan_network
from .host_enumeration import scan_network

