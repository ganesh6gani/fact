n = int(input("Enter number: "))
fact = 1

if n < 0:
    print("neg")
elif n == 0:
    print("{}! = {}".format(n, fact))
else:
    for i in range(n, 1, -1):
        fact = fact * i
    print("{}! = {}".format(n, fact))
print("Hi")
print("Hello")
