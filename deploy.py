import subprocess
import os
import signal
import time

def deploy_new_version():
    print("🚀 Senior Dev: Initiating smooth-switch deployment...")
    
    # 1. Find the current PID (if any)
    old_pid = None
    try:
        # Searching for existing Flask processes in this directory
        # Using powershell to find python processes running app.py
        cmd = 'powershell -Command "Get-Process python -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -like \'*app.py*\' } | Select-Object -ExpandProperty Id"'
        result = subprocess.check_output(cmd, shell=True)
        output = result.decode().strip()
        if output:
            # Handle multiple pids if they exist
            pids = output.split('\r\n')
            old_pid = int(pids[0])
            print(f"📡 Current version running on PID: {old_pid}")
    except Exception as e:
        print(f"ℹ️ Info: {e}")

    # 2. Start the NEW version
    print("⚡ Starting new version...")
    
    # Kill the old one first to free the port 5000
    if old_pid:
        try:
            subprocess.run(f"taskkill /F /PID {old_pid}", shell=True, capture_output=True)
            print("🛑 Old version stopped.")
        except:
            pass

    # Give a tiny moment for port to clear
    time.sleep(0.5)

    # Start new process in background
    new_proc = subprocess.Popen(['python', 'app.py'], 
                               cwd=os.path.dirname(os.path.abspath(__file__)),
                               creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.DETACHED_PROCESS if os.name == 'nt' else 0,
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
    
    print(f"✅ New version deployed (PID: {new_proc.pid})")
    print("🌐 Site is LIVE at http://127.0.0.1:5000")

if __name__ == "__main__":
    deploy_new_version()
