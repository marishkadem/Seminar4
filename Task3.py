#Задайте последовательность чисел. 
#Напишите программу, которая выведет 
#список неповторяющихся элементов исходной 
#последовательности.
#Пример:
#- Ввод:[1,1,2,4,5,6,7,7,8],
# результат: [2,4,5,6,8]

n = list("111556773322")

list = n
print(list)

list_count = []
for i in list:
    count = 0
    for k in list:
        if k == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(list[i])
print(result)