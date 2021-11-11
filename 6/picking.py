import pickle

#L = [i for i in range(10)]

#f = open('/media/navid/NewVolume/python course/6/temp.pkl', 'wb')

#pickle.dump(L, f)
#f.close()

f = open('/media/navid/NewVolume/python course/6/temp.pkl', 'rb')
L = pickle.load(f)
print(L)