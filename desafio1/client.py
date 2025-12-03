import urllib.request
import time
import sys

# Using the container name 'monitor_server' which will be defined in the run command
TARGET_URL = "http://monitor_server:5000/api/health"

def check_pulse():
    print(f"Initiating uplink to {TARGET_URL}...", flush=True)
    try:
        # Using standard library urllib as requested (no requests lib)
        with urllib.request.urlopen(TARGET_URL) as response:
            if response.status == 200:
                data = response.read().decode('utf-8')
                print(f"[SUCCESS] Uplink established. Telemetry received: {data}", flush=True)
            else:
                print(f"[WARNING] Uplink unstable. Status Code: {response.status}", flush=True)
    except Exception as e:
        print(f"[CRITICAL] Uplink failed. Reason: {e}", flush=True)

if __name__ == "__main__":
    # Simple loop to keep the container alive and polling
    while True:
        check_pulse()
        time.sleep(5)
