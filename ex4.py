n = int(input("Enter a number? "))

def is_perfect(num):
    sum_div = sum([i for i in range(1, num) if num % i == 0])
    return sum_div == num

if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")