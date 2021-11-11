# L = [i for i in range(10)]
# f = open('/media/navid/NewVolume/python course/5/temp2.txt', 'w')
# for item in L:
#     f.write(str(item) + '\n')
# f.close()

L = [(i, i) for i in range(10)]
f = open('/media/navid/NewVolume/python course/5/temp3.txt', 'w')
for item in L:
    f.write(str(item[0]) + ',' + str(item[1]) + '\n')
f.close()