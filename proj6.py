import re
import random
import string

filename = 'password.txt'
with open (filename) as file:
    data = file.read()

password = re.findall(r'[A-Z]\d+[a-zA-Z]', data)

a = random.choice(string.punctuation)
b = a.join(password)
#print(b)

with open('text.txt', 'a') as file:
    file.write(r.text)

#for i in range(3):
    #password = re.findall(r'[A-Z]\d+[a-zA-Z]', data)
    #a = random.choice(string.punctuation)
    #print(a)
    #b = password += a
    #print(b)


#for i in range(3):
    #k = random.randrange(1, 4)
    #if k == 1:
        #b = random.choice(string.punctuation)
        #password += b
    #elif k == 2:
        #c = random.choice(string.punctuation)
        #password += c
    #else:
        #d = random.choice(string.punctuation)
        #password += d

#def password_picker():

    



