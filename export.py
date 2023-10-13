#!/usr/bin/env python3

import requests
import json
import os

# Grafana settings
BASE_URL = "https://grafana-source.domain.tld/api"
HEADERS = {
    "Authorization": "Bearer glsa_6Sh12345678900E5xfpxLCMepErkXoKh_3d924635"
}

# Create directory to save dashboards
if not os.path.exists('dashboards'):
    os.makedirs('dashboards')

# Fetch list of all dashboards
response = requests.get(f"{BASE_URL}/search", headers=HEADERS)
dashboard_list = response.json()

# Download each dashboard
for dashboard in dashboard_list:
    uid = dashboard['uid']
    title = dashboard['title'].replace(" ", "_").replace("/", "_")  # Replace spaces and slashes for filename compatibility
    response = requests.get(f"{BASE_URL}/dashboards/uid/{uid}", headers=HEADERS)
    dashboard_data = response.json()

    filename = f"{title}_{uid}.json"
    with open(f"dashboards/{filename}", 'w') as f:
        json.dump(dashboard_data, f)

print(f"Downloaded {len(dashboard_list)} dashboards.")
