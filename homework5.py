immutable_var=(15, 'apple', 5.6, 25, 34)
print('Immutable var:', immutable_var)
# immutable_var[1]='orang'



mutable_list = ['a', 'b', 'c', 2.5, 25, 13]
print('Mutable list:', mutable_list)

mutable_list[0] = 100
print('Mutable list:', mutable_list)

mutable_list.append(True) #
print('Mutable list:', mutable_list)

mutable_list.extend('abcd')
print('Mutable list:', mutable_list)

mutable_list.remove(2.5)
print('Mutable list:', mutable_list)
