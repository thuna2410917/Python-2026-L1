def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Ví dụ kiểm tra:
print(get_divisors(12))