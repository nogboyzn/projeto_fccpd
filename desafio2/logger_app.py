import time
import datetime
import os

DATA_DIR = "/app/data"
LOG_FILE = os.path.join(DATA_DIR, "history.log")

def ensure_dir():
    if not os.path.exists(DATA_DIR):
        print(f"Creating directory: {DATA_DIR}")
        os.makedirs(DATA_DIR)

def log_entry():
    timestamp = datetime.datetime.now().isoformat()
    # Unique message format as requested
    entry = f"[{timestamp}] Node status: ONLINE | Persistence check.\n"
    
    print(f"Writing to persistent store: {entry.strip()}", flush=True)
    
    try:
        with open(LOG_FILE, "a") as f:
            f.write(entry)
    except IOError as e:
        print(f"Error writing to file: {e}", flush=True)

if __name__ == "__main__":
    print("Starting File-Based Persistence Service...", flush=True)
    ensure_dir()
    
    # Read previous history if exists to demonstrate persistence
    if os.path.exists(LOG_FILE):
        print("\n--- [RECOVERED DATA START] ---", flush=True)
        try:
            with open(LOG_FILE, "r") as f:
                print(f.read().strip(), flush=True)
        except Exception as e:
            print(f"Error reading file: {e}")
        print("--- [RECOVERED DATA END] ---
", flush=True)
    else:
        print("No previous history found. Starting fresh.", flush=True)
    
    while True:
        log_entry()
        time.sleep(5)
