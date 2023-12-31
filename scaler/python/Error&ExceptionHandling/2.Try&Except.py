a = 5
b = 0
try:
    print(a/b)
except(ZeroDivisionError):
    print("You cannot divide a numbe by zero!")

print("Hello I will still be executed after error!")