import numpy as np
import time


def bubbleSort(arr):
      start = time.time()  # starting the timer
      n = len(arr)  # storing length of array as n
      swapped = False
      for i in range(n):  # sort through all array elements
            for k in range(0, n - i - 1):  # sorting though 0 to length of the array - i - q
                  if arr[k] > arr[k + 1]:
                        swapped = True  # swapped if greater
                        arr[k], arr[k + 1] = arr[k + 1], arr[k]
            if not swapped:
                  end = time.time()  # end timer
                  print(end - start)  # print total time

      end = time.time()  # ending the timer
      print(round((end - start), 5))  # printing total time, rounded to 4 decimals

def insertionSort(arr):
      start = time.time()  # starting the timer
      n = len(arr)  # storing the length of the array as n
      for i in range(1, n):  # start at the second line
            j = i - 1
            while j >= 0 and arr[i] < arr[j]:  # shifting the items
                  arr[j + 1] = arr[j]
                  j = j - 1
            arr[j + 1] = arr[i]  # inserting the item

      end = time.time()  # ending the timer
      print(round((end - start), 5))  # printing total time, rounded to 4 decimals


def combine(left, right):
      l = r = 0
      arr = [] # saying array is blank

      while l < len(left) and r < len(right):
            if left[l] < right[r]:
                  arr.append(left[l]) # adding l to left side of the array
                  l += 1
            else:
                  arr.append(right[r]) # adding r to right side of the array
                  r += 1
      while l < len(left):
            arr.append(left[l]) # adding l to left side of the array
            l += 1
      while r < len(right):
            arr.append(right[r]) # adding r to right side of the array
            r += 1
      return arr


def mergeSort(arr):
      start = time.time()  # starting the timer
      if len(arr) == 1: # can't perform this sort unless the length of the array is greater than 1
            return arr

      k = len(arr) // 2 # creating variables
      left = arr[k:]
      right = arr[:k]

      left = mergeSort(left) # running the function on the left half of the array
      right = mergeSort(right) # running the function on the right half of the array
      arr = combine2(left, right)  # combining left and right halves
      end = time.time()  # ending the timer
      print(round((end - start), 5))  # printing total time, rounded to 4 decimals

      return arr


def quickSortHelper(arr, lo, hi): #lecture example
      if lo >= hi:
            return
      p = partition(arr, lo, hi)
      quicksortHelper(arr, lo, p)
      quicksortHelper(arr, p + 1, hi)


def partition(arr, lo, hi):  #lecture example
      pivot = arr[lo]  # choose first element as pivot
      i, j = lo, hi
      while True:
            while arr[i] < pivot: i = i + 1
            while arr[j] > pivot: j = j - 1
            if i >= j: return j
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1


def quickSort(arr):  #lecture example
      start = time.time()  # starting the timer
      quicksortHelper(arr, 0, len(arr) - 1)
      end = time.time()  # ending the timer
      print(round((end - start), 5))  # printing total time, rounded to 4 decimals


def sortArray(size, order, algorithm, outputfile):
      if size >= 1:
            arr = np.random.randint(10, size=size)  # creating the array in a default random
            if order == "ascending":
                  arr.sort()  # Sorting the array in ascending order
                  if algorithm == 'bubbleSort':
                        bubbleSort(arr) # applying bubble sort
                        np.savetxt(outputfile, arr, delimiter =", ") # creating txt file
                  else:
                        if algorithm == 'insertionSort':
                              insertionSort(arr) # applying insertion sort
                              np.savetxt(outputfile, arr, delimiter =", ")
                        else:
                              if algorithm == 'mergeSort':
                                    mergeSort(arr) # applying merge sort
                                    np.savetxt(outputfile, arr, delimiter =", ")
                              else:
                                    if algorithm == "quickSort":
                                          quickSort(arr) # applying quick sort
                                          np.savetxt(outputfile, arr, delimiter=", ")
                                    else:
                                          print("Try again. Spelling error") # error checking
                                          return
            else:
                  if order == "descending":
                        arr = np.sort(arr)[::-1]  # Sorting the array in descending order
                        if algorithm == 'bubbleSort':
                              bubbleSort(arr)
                              np.savetxt(outputfile, arr, delimiter =", ")
                        else:
                              if algorithm == 'insertionSort':
                                    insertionSort(arr)
                                    np.savetxt(outputfile, arr, delimiter =", ")
                              else:
                                    if algorithm == 'mergeSort':
                                          mergeSort(arr)
                                          np.savetxt(outputfile, arr, delimiter =", ")
                                    else:
                                          if algorithm == "quickSort":
                                                quickSort(arr)
                                                np.savetxt(outputfile, arr, delimiter =", ")
                                          else:
                                                print("Try again. Spelling error")
                                                return
                  else:
                        if order == "random":
                              arr = arr  # leaving the array in random order
                              if algorithm == 'bubbleSort':
                                    bubbleSort(arr)
                                    np.savetxt(outputfile, arr, delimiter =", ")
                              else:
                                    if algorithm == 'insertionSort':
                                          insertionSort(arr)
                                          np.savetxt(outputfile, arr, delimiter =", ")
                                    else:
                                          if algorithm == 'mergeSort':
                                                mergeSort(arr)
                                                np.savetxt(outputfile, arr, delimiter =", ")
                                          else:
                                                if algorithm == "quickSort":
                                                      quickSort(arr)
                                                      np.savetxt(outputfile, arr, delimiter =", ")
                                                else:
                                                      print("Try again. Spelling error")
      else:
            print("Try a larger number") # error checking



sortArray(100, 'ascending', 'bubbleSort', 'outputfile.txt')