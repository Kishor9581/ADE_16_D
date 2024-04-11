try:
    def pyramid(num):
        for i in range(1, num + 1):
            print(" " * (num - i), end="")
            print("* " * i)


    n = int(input("Enter number of rows : "))
    pyramid(n)
except Exception as e:
    print("Error found ", e)
