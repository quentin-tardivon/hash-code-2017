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
   quickSortHelper(alist, indiceTab,0,len(alist)-1)
   return indiceTab

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
           temIndice = indiceTab[leftmark]
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
