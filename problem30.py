fifthPowers = []
def split(word):
    return [char for char in word]
for i in range(2,355000):
    d = split(str(i))
    d = list(map(int, d))
    sumOfPowers = 0
    for dInt in d:
        sumOfPowers += dInt**5
    if sumOfPowers==i:
        fifthPowers.append(i)
print(sum(fifthPowers))
