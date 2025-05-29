from kubernetes import client, config
import subprocess

def run_command(cmd) -> dict: 
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return {"success": True, "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"success": False, "result": str(e)}

if __name__ == "__main__":
    print(run_command("kubectl get pods -A"))
