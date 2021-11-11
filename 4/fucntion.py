def func(q, w):
    e = q
    while True:
        if e < w:
            e += 1
            print(e)
        else:
            return

#func(0, 2)
#print(r)



def fib(n):
    if n == 1 or n == 2:
        return 1

    else:
        return(fib(n - 1) + fib(n - 2))

#d = fib(5)
#print(d)

def factoriel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factoriel(n - 1)

#print(factoriel(6))

def merge(l1, l2):
    return l1 + l2

l1 = [i for i in range(0, 9, 3)]
l2 = [i for i in range(0, 9, 2)]

#print(merge(l1, l2))

str1 = '789465'

#print(str1[::-1])

def tmp(l):
    l3 = []
    for item in l:
        yield item

#y = tmp(l1)
#for i in y:
#    print(i)

def sorting(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i] < l[j]:
                l[i], l[j] = l[j], l[i]

l = [5, 8, 3, 7, 1, 9]
#sorting(l)
#print(l)

def find_n_min(n, l):
    sorting(l)
    return l[n - 1]

#print(find_n_min(3, l))

def g(i):
    def f(k):
        return k + 1
    d = f(2)
    return d + i

#print(g(2))


def mean(l, n):
    return sum(l)/len(l)

def mean(l):
    tmp = 0
    for i in l:
        tmp += i #tmp = tmp + i
    
    return tmp/len(l)

#print(mean(l))



print(mean(l))

