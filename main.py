inputArray = [4, 7, 9, 12, 11, 89]  # Given Array


def solution(givenArray, numberofRotations):
    n = len(givenArray)
    if n == 0: return []
    numberofRotations = numberofRotations % n
    givenArray = givenArray[n - numberofRotations:] + givenArray[0:n - numberofRotations]
    return givenArray


print(f'The Array is: {inputArray}')
print("Right Rotated list is: ", solution(inputArray, 1))


def rotateList(array, numberofRotations, lenArray):
    if lenArray == 0: return []
    array[:] = array[numberofRotations:lenArray] + array[0:numberofRotations]
    return array


print(f'\nThe Array is: {inputArray}')
print("Left Rotated list is: ", rotateList(inputArray, 1, len(inputArray)))