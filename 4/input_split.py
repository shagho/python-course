x = input()
y = input()

temp = 0
for item in x:
    if y==item:
        temp += 1

print(temp)
print(x.count(y))