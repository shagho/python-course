import re

#s = re.compile('[a-z]+')

string = "a99945as5"
#print(s.match(string).group())

print(re.sub('[0-9]+', '', string))