tab = [[3, 2], [4, 5], [2,1]]
import parser as ps

def quickSortTuple(tab):
    indiceTab = []
    tabValue = []
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            indiceTab.append((i,j))
            tabValue.append(tab[i][j])

    return tabValue,indiceTab

def quickSort(tab):
   alist, indiceTab = quickSortTuple(tab)
   quick_sort_iterative(alist, indiceTab,0,len(alist)-1)
   return indiceTab

def quick_sort_iterative(alist, tab, left, right):
    """
    Iterative version of quick sort
    """
    temp_stack = []
    temp_stack.append((left,right))

    #Main loop to pop and push items until stack is empty
    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(alist, tab,left,right)
        #If items in the left of the pivot push them to the stack
        if piv-1 > left:
            temp_stack.append((left,piv-1))
        #If items in the right of the pivot push them to the stack
        if piv+1 < right:
            temp_stack.append((piv+1,right))

def quickSortHelper(alist, indiceTab,first,last):
   if first<last:

       splitpoint = partition(alist, indiceTab,first,last)

       quickSortHelper(alist,indiceTab, first,splitpoint-1)
       quickSortHelper(alist,indiceTab, splitpoint+1,last)


def partition(alist, indiceTab,first,last):
   pivotvalue = alist[first]
   pivotvalueIndice = indiceTab[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           tempIndice = indiceTab[leftmark]
           alist[leftmark] = alist[rightmark]
           indiceTab[leftmark] = indiceTab[rightmark]
           alist[rightmark] = temp
           indiceTab[rightmark] = tempIndice

   temp = alist[first]
   tempIndice = indiceTab[first]
   alist[first] = alist[rightmark]
   indiceTab[first] = indiceTab[rightmark]
   alist[rightmark] = temp
   indiceTab[rightmark] = tempIndice


   return rightmark
