def fak(n):
    if n > 0:
        return fak(n - 1) * n
    else:
        return 1