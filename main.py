
# Main function
def main():
    result = []

    n = int(input())
    sumOfSquaresOfTests(n, result)

    printList(result, n)

# Computes the sum of squares of all n test cases using recursion
# The result is stored in resultContainer in the order in which the tests were given
# (i.e. index 0 contains result for the first test case, index 1 for the second and so on)
#
# Time complexity is O(N * X) where N is the number of test cases and X is the longest data set in a test case
# Space complexity is O(N + X) where N is the number of test cases and X is the longest data set in a test case
def sumOfSquaresOfTests(n, resultContainer):
    if n == 0:
        return 
    
    x = int(input())
    numbers = input().split()

    resultContainer.append(sumOfSquares(x, numbers))

    sumOfSquaresOfTests(n - 1, resultContainer)

# Computes the sum of squares of the x numbers contained in "numbers"
def sumOfSquares(x, numbers):
    if x == 0:
        return 0
    
    y = int(numbers[x - 1])
    if (y >= 0):
        return y * y + sumOfSquares(x - 1, numbers)
    return sumOfSquares(x - 1, numbers)

# Prints the elements in list
def printList(list, numberOfItems, startIndex = 0):
    if numberOfItems == 0:
        return

    print(list[startIndex])
    printList(list, numberOfItems - 1, startIndex + 1)


if __name__ == "__main__":
    main()