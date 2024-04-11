try:
    def factorial(n):
        i = 1
        a = 1
        while i <= n:
            a *= i
            i += 1
        return a


    num = int(input("Enter number to find factorial : "))
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")

except Exception as e:
    print("Error found", e)
