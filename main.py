from classes.Methods import Methods
from classes.Stroka import Stroka
from classes.Spisok import Spisok

def length(some_object):
    return some_object.length()

def include(some_object):
    return some_object.include(sub_string)


method = Methods()
stroka = Stroka('help!')
Some_list = ['help!', 'me']
spisok = Spisok(Some_list)
sub_string = 'help'

print(length(method))
print(length(stroka))
print(length(spisok))
print()
print(include(method))
print(include(stroka))
print(include(spisok))
print()

old = 'help!'
new = ' me'
print(stroka.replacing(old, new))
print()

new_item = 'The END!'
spisok.adding(new_item)
print(Some_list)
