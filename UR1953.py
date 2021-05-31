while True:
    try:
        students = int(input())

        epr = 0
        ehd = 0
        intrusos = 0
        for i in range(students):
            regNumber, courseSymbol = input().split()
            if courseSymbol == 'EPR':
                epr += 1

            elif courseSymbol == 'EHD':
                ehd += 1

            else:
                intrusos += 1

        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intrusos}')

    except EOFError:
        break