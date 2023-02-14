qtd = int(input())
numbers = []
sep_number = []


for i in range(qtd):
    numbers.append(int(input()))

i = 0
while i < qtd:
    if sep_number.__contains__(numbers[i]) == False:
        sep_number.append(numbers[i])
    i+= 1

sep_number.sort()
for i in sep_number:
    print(str(i) + ' aparece ' + str(numbers.count(i)) + ' vez(es)')