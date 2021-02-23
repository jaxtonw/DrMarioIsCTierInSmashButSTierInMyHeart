def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    val = 1
    for i in range(n):
        val *= i
    return val
