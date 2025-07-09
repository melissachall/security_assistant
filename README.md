# 🛡️ Security Assistant

Security Assistant est un outil d’analyse et de cartographie de la sécurité réseau, offrant à la fois une interface web (Django) et des scripts Python en ligne de commande. Il permet d’explorer, d’évaluer et de visualiser la sécurité d’un réseau local à travers plusieurs modules interactifs.

---

## 🚀 Fonctionnalités principales

- **Interface Web (Django) :**
  - Cartographie réseau interactive (visualisation des nœuds et connexions)
  - Énumération des hôtes actifs sur le réseau
  - Scan de ports sur les machines détectées
  - Détection du système d’exploitation (OS) via analyse ICMP
  - Identification des services et bannières sur les ports ouverts
  - Authentification et espace utilisateur

- **Scripts CLI (Python) :**
  - Scan de ports TCP/UDP sur une plage d’adresses IP ou une machine spécifique
  - Identification de services via bannière sur ports ouverts
  - Génération de graphes réseau via NetworkX et Matplotlib

---

## 🧑‍💻 Cas d’usage

- Tester la sécurité d’un réseau interne (LAN)
- Former ou sensibiliser des utilisateurs à l’analyse de sécurité réseau
- Visualiser la topologie réseau pour identifier les points faibles et services exposés

---

## ⚙️ Prérequis

- Python 3.9+
- Modules : Django, scapy, networkx, matplotlib, tqdm
- **Windows uniquement : [Npcap](https://nmap.org/npcap/) doit être installé pour permettre l’utilisation de Scapy et des fonctionnalités réseau avancées.**
    - Pendant l’installation, cochez l’option "Install Npcap in WinPcap API-compatible Mode".
    - Redémarrez votre ordinateur après l’installation.

---

## 🏃‍♂️ Démarrage rapide

### 1. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 2. Lancer l’interface web

```bash
python manage.py runserver
```
Rendez-vous sur [http://localhost:8000](http://localhost:8000) pour accéder à l’application.

### 3. Exécution en ligne de commande

Pour utiliser les scripts en CLI :
```bash
python network_security/port_scanner.py
```
Adaptez les paramètres (adresses IP, ports) selon vos besoins dans les fichiers correspondants.

---

## 📂 Structure du projet

- `network_security/` : Modules Django et scripts d’analyse réseau
- `templates/` : Templates HTML pour l’interface web
- `network_security/port_scanner.py` : Scan de ports en CLI
- `network_security/service_identification.py` : Identification des services réseau
- `network_security/os_detection.py` : Détection du système d’exploitation distant
- `network_security/network_mapping.py` : Cartographie réseau via NetworkX

---

## ℹ️ Remarques

- **Npcap** est obligatoire sous Windows pour les fonctionnalités de scan réseau avancées (Scapy, détection d’OS, etc.).
- Ajoutez `# Npcap doit être installé manuellement sous Windows pour Scapy` dans votre `requirements.txt` pour rappel.

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Merci de soumettre vos issues ou pull requests pour toute amélioration, correction ou suggestion.