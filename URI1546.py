testCases = int(input())
colabs = ['Rolien', 'Naej', 'Elehcim','Odranoel']

for i in range(testCases):
    feedbacks = int(input())
    for j in range(feedbacks):
        FeedbackCategory = int(input())
        print(colabs[FeedbackCategory-1])