#!/usr/bin/env python3

import requests
import json
import os

# Grafana settings for the target instance
BASE_URL = "https://grafana-source.domain.tld/api"
HEADERS = {
    "Authorization": "Bearer glsa_6Sh12345678900E5xfpxLCMepErkXoKh_3d924635",
    "Content-Type": "application/json"
}


# Folder ID where you want to save the dashboards
SAVE_FOLDER = 'prepared_dashboards'

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

for filename in os.listdir('dashboards'):
    with open(f'dashboards/{filename}', 'r') as f:
        data = json.load(f)
        dashboard_data = data.get("dashboard", {})
        dashboard_data["id"] = None
        dashboard_data["uid"] = None

        with open(f'{SAVE_FOLDER}/{filename}', 'w') as out_file:
            json.dump(dashboard_data, out_file, indent=4)

    print(f"Dashboard {filename} prepared and saved to {SAVE_FOLDER}/{filename}")
