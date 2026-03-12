import os
import subprocess
import sys

def run_script(script_path):
    print(f"Running script: {script_path}...")
    try:
        result = subprocess.run([sys.executable, script_path], check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}:")
        print(e.stderr)
        sys.exit(1)

def ensure_directories():
    """Ensure that the required directories for bronze data exist."""
    print("Ensuring data directories exist...")
    os.makedirs(os.path.join("data", "bronze"), exist_ok=True)
    os.makedirs(os.path.join("data", "silver"), exist_ok=True)
    os.makedirs(os.path.join("data", "gold"), exist_ok=True)
    print("Data directories are ready.\n")

def run_data_generation():
    print("=== Starting Data Generation Pipeline ===")
    ensure_directories()
    
    scripts_to_run = [
        os.path.join("data_generation", "generate_products.py"),
        os.path.join("data_generation", "generate_customers.py"),
        os.path.join("data_generation", "generate_orders.py")
    ]
    
    for script in scripts_to_run:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"Warning: Script not found: {script}")
            
    print("=== Data Generation Complete ===")

if __name__ == "__main__":
    print("Shopstream Data Engineering - Local Runner")
    
    run_data_generation()
