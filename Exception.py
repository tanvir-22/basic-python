try:
    fp = open("mynewfile.txt","r")
    content = fp.read()
    fp.close()
except FileNotFoundError:
    print("your file is not found")