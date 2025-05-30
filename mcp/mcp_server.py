import logging
from fastmcp import FastMCP
import time
import signal
import sys

from tools.kube_client import run_command
from tools.uppercaser import to_uppercase
from tools.maths import add, subtract, multiply, divide

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
def call_add(
    a: int,
    b: int,
    session_id: str = None,
):
    """
    Returns the sum of a and b.

    :param a: The first number (int or float).
    :param b: The second number (int or float).
    :returns: The result of a + b.
    """
    return {"success": True, "result": add(a, b)}

@mcp.tool()
def call_subtract(
    a: int,
    b: int,
    session_id: str = None,
):
    """
    Returns the result of subtracting b from a.

    :param a: The number to subtract from (int or float).
    :param b: The number to subtract (int or float).
    :returns: The result of a - b.
    """
    return {"success": True, "result": subtract(a, b)}

@mcp.tool()
def call_multiply(
    a: int,
    b: int,
    session_id: str = None,
):
    """
    Returns the product of a and b.

    :param a: The first factor (int or float).
    :param b: The second factor (int or float).
    :returns: The result of a * b.
    """
    return {"success": True, "result": multiply(a, b)}

@mcp.tool()
def call_divide(
    a: int,
    b: int,
    session_id: str = None,
):
    """
    Returns the result of dividing a by b.

    :param a: The numerator (int or float).
    :param b: The denominator (int or float).
    :returns: The result of a / b.
    :raises ValueError: If b is zero.
    """
    return {"success": True, "result": divide(a, b)}

@mcp.tool()
def call_to_uppercase(
    text: str,
    session_id: str = None,
):
    """
    Converts a string to uppercase.

    :param text: The input string to convert.
    :returns: The uppercase version of the input string.
    """
    return {"success": True, "result": to_uppercase(text)}


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
