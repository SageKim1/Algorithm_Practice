## WRITE SELECTION_SORT FUNCTION HERE ##\
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_idx = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        if i != min_idx:
            temp = my_list[i]
            my_list[i] = my_list[min_idx]
            my_list[min_idx] = temp
    return my_list
######################################## 




print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """
