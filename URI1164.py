testCases = int(input())

for i in range(testCases):
    number = int(input())

    soma = 0
    for n in range(1, number):
        if number % n == 0:
            soma += n

    if soma == number:
        print(f'{number} eh perfeito')

    else:
        print(f'{number} nao eh perfeito')