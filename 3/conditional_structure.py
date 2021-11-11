x = int(input())
y = int(input())

#if x > y:
#    print("x greater than y")
#elif x < y:
#    print("y grater than x")
#else:
#    print("x equal y")


#if (2 < 1) or (3 > 2):
    #print("it's true")

# if x > y:
#     print("x greater than y")
#     a = y
# elif x < y:
#     print("y grater than x")
#     a = x

a = x if x < y else y
print(a)