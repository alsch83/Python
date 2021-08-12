a = [1, 10, 20]
print(a)
a.append(15) # добавляет аргумет в коец списка
print(a)
a.append('hi')
print(a)
a.append([5, 6])
print(a)
a.pop() # удаляет последний элемент из списка
print(a)
print(a[1])
print(a[-1])
print(a[len(a) - 1])
a[0] = 100
print(a)
a.pop(2)
print(a)
b = ['helllo', 'goodbye', 'hey']
temp = b[0]
b[0] = b[2]
b[-1] = temp
print(b)
b[0], b[2] = b[2], b[0]
print(b)