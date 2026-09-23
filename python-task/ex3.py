import math

def calculate_q(d, c=50, h=30):
    """
    Calculates Q = sqrt((2 * C * D) / H)
    Default values: C = 50, H = 30 (commonly used for this standard problem)
    """
    q_value = math.sqrt((2 * c * d) / h)
    return round(q_value)

res=calculate_q(100)
print(res)