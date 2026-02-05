W = []
K = []
for i in range(20):
    score = int(input())
    if i < 10:
        W.append(score)
    else:
        K.append(score)

W.sort(reverse=True)
K.sort(reverse=True)

print(W[0]+ W[1] + W[2], K[0] + K[1] + K[2])
