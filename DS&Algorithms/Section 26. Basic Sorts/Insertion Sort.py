## WRITE INSERTION_SORT FUNCTION HERE ##
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while j > -1 and temp < my_list[j]:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list
######################################## 




print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """
