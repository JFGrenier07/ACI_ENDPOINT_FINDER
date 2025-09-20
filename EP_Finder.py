import requests
import json
import datetime, time
from getpass import getpass
requests.packages.urllib3.disable_warnings()

# Définition des environnements ACI
SANDBOX_IP = "10.10.20.14"
HOMELAB_IP = "192.168.0.200"
LAB3_IP = "192.168.0.201"
LAB4_IP = "192.168.0.202"
ALL_IPS = [SANDBOX_IP, HOMELAB_IP, LAB3_IP, LAB4_IP]


def getToken(host, username, password):
    url = f"https://{host}/api/aaaLogin.json"
    payload = json.dumps({"aaaUser": {"attributes": {"name": username, "pwd": password}}})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return json.loads(response.text)['imdata'][0]['aaaLogin']['attributes']['token']

def select_environment():
    while True:
        print("\n=== Sélection de l'Environnement ACI ===")
        print("1- Sandbox (10.10.20.14)")
        print("2- Home Lab (192.168.0.200)")
        print("3- Lab 3 (192.168.0.201)")
        print("4- Lab 4 (192.168.0.202)")
        print("5- All")
        choice = input("Enter your choice (1-5): ").strip()
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
            print("Invalid choice. Please try again.")

def select_search_type():
    while True:
        print("\nSelect search type:")
        print("1- Search by IP address")
        print("2- Search by MAC address")
        print("3- Search by EPG")
        choice = input("Enter your choice (1-5): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_search_criteria(search_type):
    if search_type == "1":
        return input("Enter IP address to track: ").strip()
    elif search_type == "2":
        while True:
            mac = input("Enter MAC address (format: xx:xx:xx:xx:xx:xx): ").strip()
            if len(mac.split(":")) == 6:
                return mac
            print("Invalid MAC address format. Please try again.")
    else:
        return input("Enter EPG name: ").strip()

def build_query_url(host, search_type, search_value):
    base_url = f"https://{host}/api/node/class/fvCEp.json?rsp-subtree=full&rsp-subtree-include=required"
    if search_type == "1": # IP
        return f"{base_url}&rsp-subtree-filter=eq(fvIp.addr,\"{search_value}\")"
    elif search_type == "2": # MAC
        return f"{base_url}&query-target-filter=eq(fvCEp.mac,\"{search_value}\")"
    else: # EPG
        return f"{base_url}&query-target-filter=wcard(fvCEp.dn,\"epg-{search_value}/\")"

def track_endpoints():
    username = input("Enter your ACI username: ").strip()
    password = getpass("Enter your ACI password: ").strip()  # Use getpass to hide password input

    environments = select_environment()
    search_type = select_search_type()
    search_value = get_search_criteria(search_type)

    for host in environments:
        print(f"\nTracking in environment: {host}")
        token = getToken(host, username, password) # Get the token
        headers = {'Cookie': f"APIC-cookie={token}"}
        payload = {}

        url = build_query_url(host, search_type, search_value)
        print(f"Query URL: {url}")

        response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

        totalcount = int(response.get('totalCount', 0))
        URL_LIST = []

        for i in range(totalcount):
            DN = response['imdata'][i]['fvCEp']['attributes']['dn']
            URL_LIST.append(DN)

        print("=" * 170)
        print(f"{'Date':<22}{'Tenant':<15}{'App Profile':<20}{'EPG':<15}{'Encap':<12}{'MAC':<20}{'IP':<25}{'Path':<40}")
        print("-" * 170)

        for DN in URL_LIST:
            url = f"https://{host}/mqapi2/troubleshoot.eptracker.json?ep={DN}"
            response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()

            totalcount2 = int(response.get('totalCount', 0))

            for j in range(totalcount2):
                attributes = response['imdata'][j]['troubleshootEpTransition']['attributes']
                date = attributes['date'].split('.')[0]  # Couper la date après les secondes
                tenant = attributes['tenant']
                ap = attributes['ap']
                epg = attributes['epg']
                encap = attributes['encap']
                mac = attributes['mac']
                ip = attributes['ip']
                path = attributes['path']

                print(f"{date:<22}{tenant:<15}{ap:<20}{epg:<15}{encap:<12}{mac:<20}{ip:<25}{path:<40}")

        print("=" * 170)

if __name__ == "__main__":
    track_endpoints()
  
