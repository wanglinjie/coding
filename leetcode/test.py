def removeduplicate(A):
    if not A:
        return 0
    first = 0
    last = first + 1

    while last < len(A):
        if A[last] == A[first]:
            last += 1
        else:
            A[first+1] = A[last]
            last += 1
            first += 1
    print first+1, A[:first+1]


if __name__ == "__main__":
    A = [1, 2, 2, 3, 4, 4, 6]
    removeduplicate(A)