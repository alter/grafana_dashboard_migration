#!/usr/bin/env python3

import requests
import json
import os

# Grafana settings for the target instance
# Grafana settings
BASE_URL = "https://grafana-target.domain.tld/api"

HEADERS = {
    "Authorization": "Bearer glsa_6Sh12345678900E5xfpxLCMepErkXoKh_3d924635"
    "Content-Type": "application/json"
}

# Folder ID where you want to import the dashboards
FOLDER_ID = 0 

for filename in os.listdir('dashboards'):
    with open(f'dashboards/{filename}', 'r') as f:
        data = json.load(f)
        dashboard_data = data.get("dashboard", {})
        dashboard_data["id"] = None
        dashboard_data["uid"] = None
        payload = {
            "dashboard": dashboard_data,
            "folderId": FOLDER_ID,
            "overwrite": True,
        }
        
        response = requests.post(
            f"{BASE_URL}/dashboards/db",
            headers=HEADERS,
            json=payload
        )
        
        if response.status_code != 200:
            print(f"Failed to import {filename}. Error: {response.content}")
        else:
            print(f"Successfully imported {filename}")

