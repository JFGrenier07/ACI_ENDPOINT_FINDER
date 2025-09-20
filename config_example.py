"""
Configuration d'exemple pour ACI Endpoint Finder
Copiez ce fichier vers config.py et adaptez vos paramètres
"""

# Configuration des environnements ACI
ACI_ENVIRONMENTS = {
    "SANDBOX": {
        "name": "Sandbox Environment",
        "description": "Environnement de test et développement",
        "switches": [
            {"hostname": "leaf-101", "ip": "10.1.1.101", "role": "leaf"},
            {"hostname": "leaf-102", "ip": "10.1.1.102", "role": "leaf"},
            {"hostname": "spine-201", "ip": "10.1.1.201", "role": "spine"}
        ]
    },
    "HOME_LAB": {
        "name": "Home Lab",
        "description": "Laboratoire personnel",
        "switches": [
            {"hostname": "lab-leaf-01", "ip": "192.168.1.101", "role": "leaf"},
            {"hostname": "lab-leaf-02", "ip": "192.168.1.102", "role": "leaf"}
        ]
    },
    "LAB3": {
        "name": "Lab 3",
        "description": "Environnement Lab 3",
        "switches": [
            {"hostname": "lab3-leaf-01", "ip": "10.3.3.101", "role": "leaf"},
            {"hostname": "lab3-leaf-02", "ip": "10.3.3.102", "role": "leaf"}
        ]
    },
    "LAB4": {
        "name": "Lab 4",
        "description": "Environnement Lab 4",
        "switches": [
            {"hostname": "lab4-leaf-01", "ip": "10.4.4.101", "role": "leaf"},
            {"hostname": "lab4-leaf-02", "ip": "10.4.4.102", "role": "leaf"}
        ]
    }
}

# Configuration SSH par défaut
SSH_CONFIG = {
    "port": 22,
    "timeout": 10,
    "auth_timeout": 5,
    "banner_timeout": 5,
    "look_for_keys": False,
    "allow_agent": False
}

# Configuration des credentials par défaut
DEFAULT_CREDENTIALS = {
    "username": "admin",
    "password": "",  # Sera demandé interactivement
    "enable_password": ""  # Si nécessaire pour certains switches
}

# Configuration des commandes de recherche
SEARCH_COMMANDS = {
    "search_by_ip": "show endpoint ip {ip}",
    "search_by_mac": "show endpoint mac {mac}",
    "show_all_endpoints": "show endpoint",
    "show_endpoint_summary": "show endpoint summary"
}

# Configuration de sortie
OUTPUT_CONFIG = {
    "show_timestamps": True,
    "verbose_mode": False,
    "save_to_file": False,
    "output_file": "endpoint_search_results.txt",
    "format": "table"  # table, json, csv
}

# Configuration des logs
LOGGING_CONFIG = {
    "level": "INFO",  # DEBUG, INFO, WARNING, ERROR
    "file": "endpoint_finder.log",
    "max_size": "10MB",
    "backup_count": 3,
    "format": "%(asctime)s - %(levelname)s - %(message)s"
}