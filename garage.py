Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> garage = ['toyota','honda','izusu']
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'honda', 'izusu', 'suzuki']
>>> prinf(garage[2])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    prinf(garage[2])
NameError: name 'prinf' is not defined
>>> print(garage[2])
izusu
>>> garage.remove('honda')
>>> print(garage)
['toyota', 'izusu', 'suzuki']
>>> 
>>> garage.insert(1,'benz')
>>> print(garage)
['toyota', 'benz', 'izusu', 'suzuki']
>>> del garage[2]
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> print(garage[-1])
suzuki
>>> print(garage[-2])
benz
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> mycar = garage.pop(-1)
>>> print(mycar)
suzuki
>>> 
>>> print(garage)
['toyota', 'benz']
>>> garage.attend('suzuki')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    garage.attend('suzuki')
AttributeError: 'list' object has no attribute 'attend'
>>> garage.append('suzuki')
>>> print(garage)
['toyota', 'benz', 'suzuki']
>>> 
>>> garage[1] = 'tesla'
>>> print(garage)
['toyota', 'tesla', 'suzuki']
>>> print(len(garage))
3
>>> 
>>> 
>>> users = ['z','r','t','b','n','p']
>>> print(users)
['z', 'r', 't', 'b', 'n', 'p']
>>> users.sort()
>>> print(users)
['b', 'n', 'p', 'r', 't', 'z']
>>> 