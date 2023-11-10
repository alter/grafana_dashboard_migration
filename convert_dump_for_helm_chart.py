#!/usr/bin/env python3

import json

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
