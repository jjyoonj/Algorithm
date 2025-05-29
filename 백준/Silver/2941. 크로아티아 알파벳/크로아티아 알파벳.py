word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in word_list :
    a = a.replace(i, '*')
print(len(a))