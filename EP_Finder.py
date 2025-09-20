import paramiko
import time
import getpass
import sys

# Définition des environnements ACI
SANDBOX_IP = "10.10.20.14"
HOMELAB_IP = "192.168.0.200"
LAB3_IP = "192.168.0.201"
LAB4_IP = "192.168.0.202"
ALL_IPS = [SANDBOX_IP, HOMELAB_IP, LAB3_IP, LAB4_IP]

def select_environment():
    while True:
        print("\n=== Sélection de l'Environnement ACI ===")
        print("1- Sandbox (10.10.20.14)")
        print("2- Home Lab (192.168.0.200)")
        print("3- Lab 3 (192.168.0.201)")
        print("4- Lab 4 (192.168.0.202)")
        print("5- All")
        
        choice = input("\nEntrez votre choix (1-5): ").strip()
        
        if choice == "1":
            return [SANDBOX_IP]
        elif choice == "2":
            return [HOMELAB_IP]
        elif choice == "3":
            return [LAB3_IP]
        elif choice == "4":
            return [LAB4_IP]
        elif choice == "5":
            return ALL_IPS
        else:
            print("Choix invalide. Veuillez réessayer.")

def connect_to_fabric(hostname, username, password):
    """Établit une connexion SSH vers la fabric ACI"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)
        return ssh
    except Exception as e:
        print(f"Erreur de connexion à {hostname}: {str(e)}")
        return None

def execute_command(ssh, command):
    """Exécute une commande sur la fabric ACI"""
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode()
        return output
    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande: {str(e)}")
        return None

def main():
    # Sélection de l'environnement
    selected_ips = select_environment()
    
    # Demande des credentials
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    # Établir les connexions
    connections = {}
    for ip in selected_ips:
        ssh = connect_to_fabric(ip, username, password)
        if ssh:
            connections[ip] = ssh
    
    if not connections:
        print("Aucune connexion n'a pu être établie.")
        sys.exit(1)
    
    while True:
        # Menu des commandes
        print("\n=== Menu des Commandes ===")
        print("1. show endpoint ip")
        print("2. show endpoint mac")
        print("3. Quitter")
        
        cmd_choice = input("\nChoisissez une commande (1-3): ")
        
        if cmd_choice == "1":
            ip_address = input("\nEntrez l'adresse IP à rechercher: ")
            
            # Exécuter la commande sur chaque fabric sélectionnée
            for fabric_ip, ssh in connections.items():
                print(f"\n=== Résultats pour la fabric {fabric_ip} ===")
                command = f"show endpoint ip {ip_address}"
                output = execute_command(ssh, command)
                if output:
                    print(output)
        
        elif cmd_choice == "2":
            mac_address = input("\nEntrez l'adresse MAC à rechercher: ")
            
            # Exécuter la commande sur chaque fabric sélectionnée
            for fabric_ip, ssh in connections.items():
                print(f"\n=== Résultats pour la fabric {fabric_ip} ===")
                command = f"show endpoint mac {mac_address}"
                output = execute_command(ssh, command)
                if output:
                    print(output)
        
        elif cmd_choice == "3":
            print("Fermeture des connexions...")
            for ssh in connections.values():
                ssh.close()
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide!")

if __name__ == "__main__":
    main()
