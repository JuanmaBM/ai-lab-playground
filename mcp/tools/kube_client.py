import subprocess

def run_command(cmd) -> dict: 
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        return {"success": True, "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"success": False, "result": str(e)}
