def inversions(sequence):
    count = 0
    for i in range(len(sequence) - 1):
        for j in range(i, len(sequence)):
            if sequence[i] > sequence[j]:
                count += 1
    return count