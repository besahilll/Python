def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)







