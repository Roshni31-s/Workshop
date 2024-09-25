Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="Tannu"
>>> type(s)
<class 'str'>
>>> s='Tannu'
>>> type(s)
<class 'str'>
>>> y=""",mhjkhcghghbkjhkuhkh
... hgjdgj"""
>>> type(y)
<class 'str'>
>>> y
',mhjkhcghghbkjhkuhkh\nhgjdgj'
>>> s[0]
'T'
>>> s[1]
'a'
>>> s[4]
'u'
>>> s[6]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[6]
IndexError: string index out of range
>>> s[1]='t'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[1]='t'
TypeError: 'str' object does not support item assignment
>>> s[-1]
'u'
>>> s[-2]
'n'
>>> s[-3]
'n'
>>> s="This is GEC Vaishali Python Worksgop.
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> s="This is GEC Vaishali Python Workshop."
s[0:4]
'This'
s[6:8]
's '
s[5:8}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s[5:7]
'is'
s[0:6]
'This i'
s[-1:-4]
''
s[-2:-5]
''
s[-4:0]
''
s[-4:-1]
'hop'
s[-5:-1]
'shop'
s="tannu"
print("my name is %s",s)
my name is %s tannu
print("my name is %s"%s)
my name is tannu
str="this is tannu's house."
str
"this is tannu's house."
1=[7,"tannu",4.5,true]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
type(1)
<class 'int'>
1[1]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    1[1]
TypeError: 'int' object is not subscriptable
1[5]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    1[5]
TypeError: 'int' object is not subscriptable
1=[7,"tannu",5.6,True]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
type(1)
<class 'int'>
1[1]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    1[1]
TypeError: 'int' object is not subscriptable
1=[7,"tannu",5.6,True]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1.append
SyntaxError: invalid decimal literal
l=[7,"tannu",5.6,True]

l=[7,"d",7]
l.insert(1,8)
l
[7, 8, 'd', 7]
1.insert(2,46)
SyntaxError: invalid syntax
l.insert(2,46)
l
[7, 8, 46, 'd', 7]
l.pop()
7
l
[7, 8, 46, 'd']
l.remove(1)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    l.remove(1)
ValueError: list.remove(x): x not in list
l.remove(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    l.remove(l)
ValueError: list.remove(x): x not in list
l.remove(7)
l
[8, 46, 'd']
l[1:3]
[46, 'd']
l[0:3]
[8, 46, 'd']
list1=[12,23,34,45]
list2=[45,56,25,35]
l1+l2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l1+l2
NameError: name 'l1' is not defined. Did you mean: 'l'?
l=['tannu',35,37]
len(1)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
l=['tannu',35,37]
len(1)
SyntaxError: multiple statements found while compiling a single statement

t=(6,7.7,"g")
type(t)
<class 'tuple'>
t[0]
6
t[0]=8
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    t[0]=8
TypeError: 'tuple' object does not support item assignment
t=(2,3,4,5)
t.count(4)
1
sets={"GECV","GEMC","GECS"}
type(sets)
<class 'set'>
sets2=set(["Mon","Tue","Wed"]}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
sets2=set(["Mon","Tue","Wed"])
type=(sets2)
l=['tannu',35,37]
type(sets2)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    type(sets2)
TypeError: 'set' object is not callable
sets2[1]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    sets2[1]
TypeError: 'set' object is not subscriptable
sets2.add("thru")
sets2
{'Mon', 'Wed', 'Tue', 'thru'}
sats2.discard("wed")
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    sats2.discard("wed")
NameError: name 'sats2' is not defined. Did you mean: 'sets2'?
sets2.discard("Wed")
sets
{'GEMC', 'GECV', 'GECS'}
sets2.discard("Wed")
sets2
{'Mon', 'Tue', 'thru'}
