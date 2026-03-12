import os
import subprocess
import datetime

def log_docker_status():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    status_file = os.path.join(log_dir, "docker_status.log")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Fetching Docker status at {timestamp}...")
    
    try:
        # Check running containers via docker-compose ps
        ps_result = subprocess.run(
            ["docker-compose", "ps"], 
            capture_output=True, text=True, check=False
        )
        
        # Check resource usage via docker stats
        stats_result = subprocess.run(
            ["docker", "stats", "--no-stream"], 
            capture_output=True, text=True, check=False
        )
        
        with open(status_file, "a", encoding="utf-8") as f:
            f.write(f"===================================================\n")
            f.write(f"Time: {timestamp}\n")
            f.write(f"===================================================\n\n")
            
            f.write("--- SERVICES STATUS (docker-compose ps) ---\n")
            f.write(ps_result.stdout if ps_result.stdout else "No output or no docker-compose running.\n")
            if ps_result.stderr:
                f.write(f"Errors:\n{ps_result.stderr}\n")
                
            f.write("\n--- RESOURCE USAGE (docker stats) ---\n")
            f.write(stats_result.stdout if stats_result.stdout else "No active containers found.\n")
            
            f.write("\n\n")
            
        print(f"Successfully appended Docker status to: {status_file}")
        
    except FileNotFoundError:
        print("Error: 'docker' or 'docker-compose' command not found. Is Docker installed and running?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    log_docker_status()
