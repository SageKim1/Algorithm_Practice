# WRITE ITEM_IN_COMMON FUNCTION HERE #
def item_in_common(list1, list2):
    dict1 = {key:True for key in list1}
    
    for item in list2:
        if item in dict1:
            return True
    return False
######################################




list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
