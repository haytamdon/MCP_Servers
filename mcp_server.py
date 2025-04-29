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

@mcp.tool()
def multiplication(a: int, b: int) -> int:
    """Multiply 2 numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: Multiplication
    """
    print(f"Multiplying {a} and {b}")
    return a * b

@mcp.tool()
def divide(a: int, b:int) -> int:
    """Divide 2 numbers a by b

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: Division
    """

    print(f"Dividing {a} by {b}")
    return a / b   

if __name__ == "__main__":
    mcp.run(transport="sse")