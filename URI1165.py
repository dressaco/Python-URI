testCases = int(input())

for i in range(testCases):
    number = int(input())

    divisores = 0
    for divisor in range(1, number+1):
        if number % divisor == 0:
            divisores += 1

    if divisores == 2:
        print(f'{number} eh primo')

    else:
        print(f'{number} nao eh primo')