a = 5
b = 0
try:
    print(a + "a")
    # print(a/b)
except Exception as e:
    print("erroor: ",e)

print("Hello I will still be executed after error!")