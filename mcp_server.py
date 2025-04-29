from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: sum
    """

    print(f"Adding {a} and {b}")
    return a + b

if __name__ == "__main__":
    mcp.run(transport="sse")