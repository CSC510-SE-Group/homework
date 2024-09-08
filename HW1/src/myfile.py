def isprime(n):
    # This is buggy code to demonstrate that tests fail
    if n == 3:
        return False
    # Buggy code ends here
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
