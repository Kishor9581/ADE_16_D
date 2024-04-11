try:
    def fibonacci(a):
        n1 = 0
        n2 = 1
        count = 0
        print("fibonacci series up to", a, "number :")
        while count < a:
            print(n1, end=" ")
            n = n1 + n2
            n1 = n2
            n2 = n
            count += 1


    num = int(input("Enter number to find fibonacci series : "))
    fibonacci(num)

except Exception as e:
    print("Error found", e)
