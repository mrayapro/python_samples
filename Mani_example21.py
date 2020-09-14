list1 = [10, 15, 20, 25, 30, 35, 40]
list2 = [25, 40, 35]

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif

list1 = Diff(list1,list2)

print(list1)
