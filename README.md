# ACI Endpoint Tracker

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Network](https://img.shields.io/badge/network-Cisco%20ACI-blue.svg)
![API](https://img.shields.io/badge/interface-REST%20API-green.svg)

Un outil professionnel de tracking et d'analyse d'endpoints dans les infrastructures Cisco ACI (Application Centric Infrastructure) via REST API avec historique des transitions.

## 🎯 Vue d'ensemble

**ACI Endpoint Tracker** est un utilitaire réseau avancé qui permet aux administrateurs de :
- Tracker l'historique complet des transitions d'endpoints
- Rechercher des endpoints par IP, MAC ou EPG via REST API
- Analyser les mouvements d'endpoints à travers multiple fabrics ACI
- Obtenir des informations détaillées sur les paths et encapsulations
- Troubleshooter efficacement les problèmes de mobilité réseau

## 🚀 Fonctionnalités

### 🔍 Tracking Multi-Critères
- **Recherche par IP** : Tracking d'endpoints via adresse IP
- **Recherche par MAC** : Suivi d'endpoints via adresse MAC
- **Recherche par EPG** : Analyse par Endpoint Group
- **Historique des Transitions** : Tracking complet des mouvements

### 🌐 Environnements Supportés
- **Sandbox** : 10.10.20.14 - Environnement de test
- **Home Lab** : 192.168.0.200 - Laboratoire personnel
- **Lab 3** : 192.168.0.201 - Environnement Lab 3
- **Lab 4** : 192.168.0.202 - Environnement Lab 4
- **Multi-Sélection** : Tracking simultané sur tous les fabrics

### 🔧 Capacités Techniques
- API REST ACI avec authentification par token
- Interface troubleshoot.eptracker pour l'historique
- Gestion automatique des sessions APIC
- Affichage tabulaire formaté des résultats
- Support multi-environnements simultané

## 📋 Prérequis

### Environnement Système
- **Python** : 3.6 ou supérieur
- **Accès réseau** : Connectivité HTTPS vers les APIC controllers
- **Permissions** : Compte utilisateur ACI avec droits de lecture

### Dépendances Python
```bash
requests>=2.25.0
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
Les environnements ACI sont préconfigurés dans le script :
```python
SANDBOX_IP = "10.10.20.14"
HOMELAB_IP = "192.168.0.200"
LAB3_IP = "192.168.0.201"
LAB4_IP = "192.168.0.202"
```

Pour modifier les adresses IP, éditez directement ces variables dans `EP_Finder.py`.

## 🎮 Instructions d'Exécution

### Lancement du Script
```bash
python EP_Finder.py
```

### Workflow d'Utilisation

#### 1. Authentification
```bash
$ python EP_Finder.py
Enter your ACI username: admin
Enter your ACI password: [saisie sécurisée]
```

#### 2. Sélection d'Environnement
```bash
=== Sélection de l'Environnement ACI ===
1- Sandbox (10.10.20.14)
2- Home Lab (192.168.0.200)
3- Lab 3 (192.168.0.201)
4- Lab 4 (192.168.0.202)
5- All
Enter your choice (1-5): 2
```

#### 3. Type de Recherche
```bash
Select search type:
1- Search by IP address
2- Search by MAC address
3- Search by EPG
Enter your choice (1-3): 1
```

#### 4. Critères de Recherche
```bash
Enter IP address to track: 10.1.100.50

[Tracking en cours...]
```

### Exemples d'Utilisation

#### Tracking par IP
```bash
$ python EP_Finder.py
Username: admin
Password: [hidden]
Environment: 2 (Home Lab)
Search type: 1 (IP address)
IP: 10.1.100.50

Tracking in environment: 192.168.0.200
========================================================================================================
Date                  Tenant         App Profile         EPG            Encap       MAC                 IP                       Path
--------------------------------------------------------------------------------------------------------
2025-09-20 14:30:15   Production     WebApp              Web-Servers    vlan-100    00:50:56:aa:bb:cc   10.1.100.50             topology/pod-1/paths-101/pathep-[eth1/1]
2025-09-20 14:25:10   Production     WebApp              Web-Servers    vlan-100    00:50:56:aa:bb:cc   10.1.100.50             topology/pod-1/paths-102/pathep-[eth1/1]
========================================================================================================
```

#### Tracking par MAC
```bash
$ python EP_Finder.py
Username: admin
Search type: 2 (MAC address)
MAC: 00:50:56:aa:bb:cc

Résultats avec historique complet des transitions:
- Mouvements entre différents paths
- Historique des encapsulations
- Timeline des changements
```

#### Tracking par EPG
```bash
$ python EP_Finder.py
Search type: 3 (EPG)
EPG: Web-Servers

Affichage de tous les endpoints dans l'EPG avec leur historique
```

## 📊 Format de Sortie

### Colonnes du Tableau de Tracking
- **Date** : Timestamp de la transition d'endpoint
- **Tenant** : Tenant ACI où l'endpoint est situé
- **App Profile** : Profil d'application associé
- **EPG** : Endpoint Group de rattachement
- **Encap** : Encapsulation (VLAN) utilisée
- **MAC** : Adresse MAC physique de l'endpoint
- **IP** : Adresse IP de l'endpoint
- **Path** : Chemin physique (leaf, port, etc.)

### Exemple de Rapport Détaillé
```
=== TRACKING D'ENDPOINT ===
Environment: 192.168.0.200
Search Criteria: IP 10.1.100.50
Query URL: https://192.168.0.200/api/node/class/fvCEp.json?...

========================================================================================================
Date                  Tenant         App Profile         EPG            Encap       MAC                 IP                       Path
--------------------------------------------------------------------------------------------------------
2025-09-20 14:30:15   Production     WebApp              Web-Servers    vlan-100    00:50:56:aa:bb:cc   10.1.100.50             topology/pod-1/paths-101/pathep-[eth1/1]
2025-09-20 14:25:10   Production     WebApp              Web-Servers    vlan-100    00:50:56:aa:bb:cc   10.1.100.50             topology/pod-1/paths-102/pathep-[eth1/1]
2025-09-20 14:20:05   Production     WebApp              Web-Servers    vlan-100    00:50:56:aa:bb:cc   10.1.100.50             topology/pod-1/paths-101/pathep-[eth1/2]
========================================================================================================
```

## 🏗️ Architecture Technique

### Structure du Code
```python
def getToken()              # Authentification API et récupération token
def select_environment()    # Sélection d'environnement ACI
def select_search_type()    # Choix du type de recherche (IP/MAC/EPG)
def get_search_criteria()   # Saisie des critères de recherche
def build_query_url()       # Construction des URLs de requête API
def track_endpoints()       # Orchestration principale du tracking
```

### Flux de Données
1. **Authentification** → Récupération du token ACI via API
2. **Sélection** → Choix de l'environnement et type de recherche
3. **Requête** → Appel API pour récupérer les endpoints
4. **Tracking** → Utilisation de l'API troubleshoot.eptracker
5. **Affichage** → Présentation tabulaire des transitions

## 🔒 Sécurité

### Bonnes Pratiques Implémentées
- **Saisie sécurisée** des mots de passe (module getpass)
- **Authentification par token** ACI avec gestion de session
- **Désactivation des warnings SSL** pour environnements lab
- **Validation des formats** (adresses MAC, IP)
- **Gestion d'erreurs** pour les appels API

### Recommandations
- Utilisez des comptes à privilèges limités (lecture seule)
- Activez la validation SSL en production
- Monitorer les accès API dans les logs APIC
- Implementez la rotation des tokens pour production

## 🎯 Cas d'Usage Professionnels

### Troubleshooting Réseau
- **Tracking de mobilité** : Analyser les mouvements d'endpoints
- **Diagnostic de flapping** : Identifier les endpoints instables
- **Historique des transitions** : Timeline complète des changements
- **Vérification de path** : Validation des chemins physiques

### Administration et Monitoring
- **Audit de placement** des endpoints par EPG
- **Monitoring des encapsulations** VLAN
- **Documentation automatique** des topologies
- **Validation post-migration** des endpoints

### Analyse et Reporting
- **Rapports de mobilité** pour audit
- **Détection d'anomalies** de mouvement
- **Cartographie temps réel** des endpoints
- **Métriques de stabilité** des endpoints

## 🚀 Améliorations Futures

- Export des résultats en CSV/JSON
- Interface graphique web avec graphiques
- Alertes temps réel sur anomalies de mobilité
- Intégration avec systèmes de monitoring (Grafana)
- Machine learning pour prédiction de mouvements
- Support multi-tenant avec filtrage
- API REST pour intégration système

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