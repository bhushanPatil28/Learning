with open("test.pdf", "rb") as f:
    data = f.read(500)
    # print(data)

with open("test.pdf", "rb") as f:
    data = f.read()

    with open("new_test.pdf", "wb") as d:
        d.write(data)