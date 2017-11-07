# Quick Sort
# Reference: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
#
# The quick sort uses divide and conquer to gain the same advantages as the merge sort
#
# How quick sort algorithm works
# We begin by incrementing leftmark until we locate a value that is greater than the pivot value. 
# We then decrement rightmark until we find a value that is less than the pivot value.

def QuickSort(alist):
    QuickSortHelper(alist, 0, len(alist)-1 )

def QuickSortHelper(alist, first, last):
    if first < last:

        # partition function used to find the splitpoint in alist
        splitpoint = partition(alist, first, last)

        # sicide and conquer to solve the subproblems
        QuickSortHelper(alist, first, splitpoint-1)
        QuickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):

    # Although there are many different ways to choose the pivot value, 
    # we will simply use the first item in the list as pivot value.
    pivotvalue = alist[first]

    # define and initialize the leftmark and rightmark [index] 
    leftmark = first+1
    rightmark = last

    done = False

    # when leftmark > rightmark is true
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1

        # when we find the leftmark value greater than pivot value
        # and rightmark value greater than pivot value
        # exchange the value of the leftmark and rightmark
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    # keep exchange leftmark value and rightmark value until rightmark < leftmark
    # then the split value was found
    temp2 = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp2

    # rightmark is my split value 
    return rightmark


alist = [54,26,93,17,77,31,4,55,20]
QuickSort(alist)
print(alist)







