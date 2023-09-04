def mergesort(alist):
    if (len(alist)<2):
        return alist
    mid = int(len(alist)/2)
    sub_list_1 = mergesort(alist[:mid])
    sub_list_2 = mergesort(alist[mid:])
    out = []
    i = 0
    j = 0
    while i<len(sub_list_1) and j<len(sub_list_2):
        if(sub_list_1[i]>sub_list_2[j]):
            out.append(sub_list_2[j])
            j+=1
        else:
            out.append(sub_list_1[i])
            i+=1
    out = out + sub_list_1[i:]
    out = out + sub_list_2[j:]
    return out

print("Merge Sort")
alist = []
print ("enter any 5 numbers",alist)
for i in range(5):
    data = int(input())
    alist.append(data)
print("Unsorted List",alist)
alist = mergesort(alist)      
print("Sorted List",alist)

