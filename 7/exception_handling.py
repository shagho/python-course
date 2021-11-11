l = []

# try:
#   print(l[0])
# except IndexError:
#   print("list hasn't a memeber.")

# try:
#     if len(l) == 0:
#         raise IndexError
# except:
#     print("an error is occured. please contact the developer.")


#raise IndexError

class MyError(Exception):
    def __init__(self):
        print("a custom error is occured!")

a, b = input("please enter two numbers: ").split(" ")
a = int(a)
b = int(b)

try:
    if b == 0:
        raise MyError
    print(a/b)
except:
    print("zerodivision error occured!")