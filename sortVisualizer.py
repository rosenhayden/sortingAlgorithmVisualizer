
import tkinter as tk
from tkinter import ttk
import random

def buildBars(arr):
    """This clears the screen then redraws all the bars"""
    C.delete("rect")  # Clear previous rectangles
    for i in range(len(arr)):
        rect = C.create_rectangle(40+(i*40), 720, 10+(i*40), 720-arr[i], fill='#8ec07c',outline="#3c3836", width="4", tag="rect")


def bubbleSort(arr):
    n = len(arr)
    # For loop to traverse through all 
    # elements in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            # is greater than the adjacent element
             if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                buildBars(arr)  # Redraw bars after each swap
                C.update()  # Update the canvas to reflect changes
                root.after(50)  



def insertionSort(list1):  
   
        # Outer loop to traverse on len(list1)  
        for i in range(1, len(list1)):  
   
            a = list1[i]  
   
            # Move elements of list1[0 to i-1], 
            # which are greater to one position
            # ahead of their current position  
            j = i - 1 
           
            while j >= 0 and a < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1 
                buildBars(arr)  # Redraw bars after each swap
                C.update()  # Update the canvas to reflect changes
                root.after(50)  

                 
            list1[j + 1] = a  
             
def bogoSort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)
        buildBars(arr)  # Redraw bars after each swap
        C.update()  # Update the canvas to reflect changes
        root.after(50)  

 
# To check if array is sorted or not
 
 
def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            return False
    return True
 
# To generate permutation of the array
 
 
def shuffle(arr):
    n = len(arr)
    for i in range(0, n):
        r = random.randint(0, n-1)
        arr[i], arr[r] = arr[r], arr[i]
 



def selectAlgorithm(c, arr):
    print(c + "YEA NO")
    if c == "bubble":
        bubbleSort(arr)
    elif c == "bogo":
        bogoSort(arr)
    elif c == "insertion":
        insertionSort(arr)

def generateArray(length):
    arr = []
    for i in range(length):
        arr.append(random.randint(1, 720))
   
    buildBars(arr)  # Redraw bars after each swap
    C.update()  # Update the canvas to reflect changes

    return arr

def get_index(*arg): 
    """Returns the value from the combobox"""
    return(str(n.get()))

root = tk.Tk()
root.geometry('500x250') 
C = tk.Canvas(root, width=1280, height=720, bg='#fbf1c7')
C.pack()

arr = generateArray(30)
buildBars(arr)  # Initial visualization

ttk.Label(root, text = "Select Algorithm :").pack()  
# Combobox creation 
n = tk.StringVar() 
algochoosen = ttk.Combobox(root, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
algochoosen['values'] = ('bogo',  
                          'bubble', 
                          'insertion') 
algochoosen.pack() 
#n.trace('w', get_index) 

button = tk.Button(root, text="Sort", command=lambda:selectAlgorithm(get_index(), arr))
button2 = tk.Button(root, text="Generate New Numbers", command=lambda:generateArray(10))
button.pack(padx=20, pady=20)
button2.pack()




root.mainloop()
