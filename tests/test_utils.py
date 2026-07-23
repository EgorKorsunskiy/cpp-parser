def compareLists(listA, listB):
    if len(listA) != len(listB):
        return False
    for i in range(len(listA)):
        if listA[i] != listB[i]:
            return False
    return True