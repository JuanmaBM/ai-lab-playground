import logging
from fastmcp import FastMCP
import time
import signal
import sys

from kube_client import run_command

# Set up logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# Handle SIGINT (Ctrl+C) gracefully
def signal_handler(sig, frame):
    print("Shutting down server gracefully...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

mcp = FastMCP(
    name="custom-tools",
    host="127.0.0.1",
    port=5000,
    timeout=30
)

@mcp.tool()
def kube_command(
    cmd: str,
    session_id: str = None,
):
    """Executing a command on Kubernetes and return the output
    :param cmd: The command to be executed
    :returns: The output of the command executed
    """
    logger.debug(f"kube_command called with: cmd={cmd}")
    return run_command(cmd)

if __name__ == "__main__":
    try:
        print("Starting MCP server on 127.0.0.1:5000")
        mcp.run("sse")
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
