a = 5
b = 0

try: 
    print("open file")
    print(a/b)
    # print("close file")     It will not work in exception
except Exception as e:
    print("Error ", e)
finally:
    print("close file")  #executes in any case