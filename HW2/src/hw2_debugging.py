def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr) // 2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))

    # Both left and right are not empty
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):

        # Put left array in mergeArr because its smaller.
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1

    # If left is empty, add right array to mergeArr
    for i in range(rightIndex, len(rightArr)):
        mergeArr[leftIndex + i] = rightArr[i]

    # If right is empty, add left array to mergeArr
    for i in range(leftIndex, len(leftArr)):
        mergeArr[i + rightIndex] = leftArr[i]

    return mergeArr


