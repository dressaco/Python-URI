# while True:
#     try:
#         n, m = map(int, input().split())
#         naoRepete = 0
#         for num in range(n, m+1):
#             numConverted2String = str(num)
#             numSplited = []
#             numsRepetidos = 0
#             for digit in range(0, len(numConverted2String)):
#                 numSplited.append(numConverted2String[digit])

#             for num1 in range(0, len(numSplited)):
#                 for numSeguinte in range(num1 + 1, len(numSplited)):
#                     if numSplited[num1] == numSplited[numSeguinte]:
#                         numsRepetidos += 1

#             if numsRepetidos == 0:
#                 naoRepete += 1

#         print(naoRepete)

#     except EOFError:
#         break
while True:
    try:
        n, m = input().split()
        qt = 0
        for x in range(int(n), int(m)+1):
            if len(set(list(str(x)))) == len(str(x)):
                qt += 1
        print(qt)

    except EOFError:
        break