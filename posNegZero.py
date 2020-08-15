negatives = positives = zeroes = 0
print("enter -1 to exit: ")
while 1:
    num = int(input("enter any number: "))
    if num == -1:
        break
    if num == 0:
        zeroes += 1
    elif num > 0:
        positives += 1
    else:
        negatives += 1
print("count of positive numbers are: ", positives)
print("count of negative numbers are: ", negatives)
print("count of zeroes numbers are: ", zeroes)

