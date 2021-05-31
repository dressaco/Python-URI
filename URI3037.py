testCases = int(input())

for i in range(testCases):
    johnPoints = 0
    maryPoints = 0

    for johnP in range(3):
        score, distance = map(int, input().split())
        johnPoints += score * distance

    for maryP in range(3):
        score, distance = map(int, input().split())
        maryPoints += score * distance

    if johnPoints > maryPoints:
        print('JOAO')

    else:
        print('MARIA')