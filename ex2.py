# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.



x = input().split() 
for i in range(len(x)):
    x[i] = int(x[i])
    count = x[0:2]
    count1 = x[2:]
    result = map(sum, (count, count1))

print(list(result))