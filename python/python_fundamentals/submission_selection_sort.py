

def selection_sort(some_list):
    print("starting array ", some_list)
    for j in range(0, len(some_list)):
        min_value =some_list[j]
        min_index =j
        i=0
        for i in range(j, len(some_list)):
            if some_list[i]<min_value:
                min_value = some_list[i]
                min_index = i
        #now we have the min value = min_value
        #print(some_list)
        #print("*"*8)
        for k in range(min_index,j, -1):
            some_list[k]=some_list[k-1]
        some_list[j]= min_value
    return some_list




list_to_sort = [4,7,2,9,1, 99, 60]
y = selection_sort(list_to_sort)
print("sorted array ", y)

