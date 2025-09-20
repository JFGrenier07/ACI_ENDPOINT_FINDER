# ACI Endpoint Finder

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Network](https://img.shields.io/badge/network-Cisco%20ACI-blue.svg)

Un outil professionnel de recherche et de localisation d'endpoints dans les infrastructures Cisco ACI (Application Centric Infrastructure) via SSH.

## 🎯 Vue d'ensemble

**ACI Endpoint Finder** est un utilitaire réseau avancé qui permet aux administrateurs de :
- Localiser rapidement des endpoints par IP ou MAC dans multiple fabrics ACI
- Se connecter simultanément à plusieurs environnements ACI
- Exécuter des recherches d'endpoints via interface interactive
- Troubleshooter efficacement les problèmes de connectivité réseau

## 🚀 Fonctionnalités

### 🔍 Recherche Multi-Critères
- **Recherche par IP** : Localisation d'endpoints via adresse IP
- **Recherche par MAC** : Identification d'endpoints via adresse MAC
- **Multi-Fabric** : Support de plusieurs environnements ACI simultanément
- **Recherche Interactive** : Interface utilisateur conviviale

### 🌐 Environnements Supportés
- **Sandbox** : Environnement de test et développement
- **Home Lab** : Laboratoire personnel
- **Lab 3 & Lab 4** : Environnements de laboratoire avancés
- **Multi-Sélection** : Recherche simultanée sur plusieurs fabrics

### 🔧 Capacités Techniques
- Connexions SSH sécurisées avec authentification
- Gestion des timeouts et erreurs de connexion
- Interface en ligne de commande interactive
- Support des commandes "show endpoint" natives ACI

## 📋 Prérequis

### Environnement Système
- **Python** : 3.6 ou supérieur
- **Accès SSH** : Connectivité vers les switches ACI
- **Permissions** : Accès aux commandes "show endpoint"

### Dépendances Python
```bash
paramiko>=2.7.0
```

## 🛠️ Installation

### 1. Cloner le repository
```bash
git clone https://github.com/JFGrenier07/ACI_ENDPOINT_FINDER.git
cd ACI_ENDPOINT_FINDER
```

### 2. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration
Éditez le fichier `EP_Finder.py` pour configurer vos environnements ACI :
```python
environments = {
    "1": {"name": "Sandbox", "ips": ["10.1.1.1", "10.1.1.2"]},
    "2": {"name": "Home Lab", "ips": ["192.168.1.100", "192.168.1.101"]},
    "3": {"name": "Lab 3", "ips": ["10.3.3.1", "10.3.3.2"]},
    "4": {"name": "Lab 4", "ips": ["10.4.4.1", "10.4.4.2"]}
}
```

## 🎮 Instructions d'Exécution

### Lancement du Script
```bash
python EP_Finder.py
```

### Workflow d'Utilisation

#### 1. Sélection d'Environnement
```bash
$ python EP_Finder.py

=== SÉLECTION D'ENVIRONNEMENT ACI ===
1. Sandbox
2. Home Lab
3. Lab 3
4. Lab 4
5. Tous les environnements

Choisissez un environnement (1-5): 2
```

#### 2. Authentification
```bash
Nom d'utilisateur: admin
Mot de passe: [saisie sécurisée]
```

#### 3. Menu de Recherche
```bash
=== RECHERCHE D'ENDPOINTS ===
1. Rechercher par adresse IP
2. Rechercher par adresse MAC
3. Quitter

Votre choix: 1
```

#### 4. Saisie de Critères
```bash
Entrez l'adresse IP à rechercher: 10.1.100.50

[Recherche en cours sur les fabrics sélectionnés...]
```

### Exemples d'Utilisation

#### Recherche par IP
```bash
$ python EP_Finder.py
Environnement: Home Lab
Choix: 1
IP: 10.1.100.50

Résultats:
Switch: leaf-101
Endpoint trouvé: 10.1.100.50 | MAC: 00:50:56:aa:bb:cc | VLAN: 100
```

#### Recherche par MAC
```bash
$ python EP_Finder.py
Environnement: Sandbox
Choix: 2
MAC: 00:50:56:aa:bb:cc

Résultats:
Switch: leaf-102
Endpoint trouvé: MAC 00:50:56:aa:bb:cc | IP: 10.2.200.75 | VLAN: 200
```

#### Recherche Multi-Fabric
```bash
$ python EP_Finder.py
Environnement: 5 (Tous)
Choix: 1
IP: 10.1.100.50

[Recherche simultanée sur tous les fabrics...]
Fabric Sandbox: Endpoint non trouvé
Fabric Home Lab: Endpoint trouvé sur leaf-101
Fabric Lab 3: Endpoint non trouvé
Fabric Lab 4: Endpoint non trouvé
```

## 📊 Format de Sortie

### Informations Affichées
- **Switch/Leaf** : Identifiant du switch où l'endpoint est connecté
- **Adresse IP** : Adresse IP de l'endpoint
- **Adresse MAC** : Adresse MAC physique
- **VLAN/EPG** : VLAN ou Endpoint Group associé
- **Statut** : État de l'endpoint (actif/inactif)

### Exemple de Rapport
```
=== RÉSULTATS DE RECHERCHE ===
Fabric: Home Lab
Critère: IP 10.1.100.50
Timestamp: 2025-09-20 16:15:30

Switch: leaf-101
├── IP: 10.1.100.50
├── MAC: 00:50:56:aa:bb:cc
├── VLAN: 100
├── EPG: Web-Servers
└── Statut: Active
```

## 🏗️ Architecture Technique

### Structure du Code
```python
def select_environment()     # Sélection d'environnement ACI
def get_credentials()        # Récupération sécurisée des credentials
def connect_to_fabric()      # Établissement connexions SSH
def search_by_ip()          # Recherche par adresse IP
def search_by_mac()         # Recherche par adresse MAC
def execute_command()       # Exécution commandes sur switches
def main()                  # Orchestration principale
```

### Flux de Données
1. **Sélection** → Choix de l'environnement ACI cible
2. **Authentification** → Saisie sécurisée des credentials
3. **Connexion** → Établissement des sessions SSH
4. **Recherche** → Exécution des commandes "show endpoint"
5. **Affichage** → Présentation formatée des résultats

## 🔒 Sécurité

### Bonnes Pratiques Implémentées
- **Saisie sécurisée** des mots de passe (module getpass)
- **Gestion des timeouts** SSH pour éviter les blocages
- **Validation des inputs** utilisateur
- **Fermeture propre** des connexions SSH

### Recommandations
- Utilisez des comptes à privilèges limités
- Configurez des timeouts appropriés
- Monitorer les logs de connexion
- Changez régulièrement les mots de passe

## 🎯 Cas d'Usage Professionnels

### Troubleshooting Réseau
- **Localisation rapide** d'endpoints problématiques
- **Diagnostic de connectivité** inter-fabric
- **Vérification de mobilité** des endpoints

### Administration et Monitoring
- **Audit de placement** des endpoints
- **Vérification de configuration** VLAN/EPG
- **Documentation automatique** de la topologie

### Migration et Maintenance
- **Planification de migration** d'endpoints
- **Vérification post-changement**
- **Cartographie de dépendances**

## 🚀 Améliorations Futures

- Support des APIs REST ACI
- Export des résultats en CSV/JSON
- Interface graphique web
- Historique des recherches
- Alertes et monitoring temps réel

## 🤝 Contribution

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit les changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créer une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Jean-François Grenier**
- GitHub: [@JFGrenier07](https://github.com/JFGrenier07)
- LinkedIn: [Votre profil LinkedIn]

## 🔗 Projets Connexes

- [ACI Contract Parser](https://github.com/JFGrenier07/ACI_CONTRACT_PARSER)
- [ACI Tools Collection](https://github.com/JFGrenier07/ACI)

---
*Développé pour simplifier le troubleshooting et l'administration des infrastructures Cisco ACI*