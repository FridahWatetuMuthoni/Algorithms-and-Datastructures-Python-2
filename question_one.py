"""
QUESTION 1:
Alice has some cards with numbers written on them. 
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.

PROBLEM:
Searching for a specific number in the array in the least time possible

INPUT:
cards: an array that contains numbers that are sorted in a decreasing order
target: the number that we are searching for
cards = [10, 9, 8, 7, 8]
target = 8

OUTPUT:
output: the index of the number in the array if found else none

EDGE CASES:
The number is somewhere in the middle of the list
target is the first element in the list
target is the last element in the list
the list has only one element
the list is empty
the list contains repeating numbers

PSEUDO CODE
# create a function that takes an array as a parameter and the target value
# since the array is sorted we can use binary search to look for the value
# returns the index of the target value or None if the value is not found
"""


def number_search(arr, target):
    start = 0
    end = len(arr) - 1

    while (start <= end):
        mid = (start + end) // 2

        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            start = mid + 1
        else:
            end = mid - 1
    return None


test = [
    {"input": {
        "array": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "target":4
    },
        "output":6
    },
    {
        "input": {
            "array": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            "target":30
        },
        "output": None
    }
]


def verify(test):
    for element in test:
        result = number_search(
            element["input"]["array"], element["input"]["target"])
        if (result == element["output"]):
            return True
        else:
            return False


print(verify(test))
