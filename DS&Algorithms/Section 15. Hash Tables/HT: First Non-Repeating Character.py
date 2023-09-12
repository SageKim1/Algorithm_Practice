# WRITE THE FUNCTION HERE #
def first_non_repeating_char(string):
    char_cnt = {}
    for char in string:
        char_cnt[char] = char_cnt.get(char, 0) + 1
    for char in string:
        if char_cnt[char] == 1:
            return char
    return None
###########################



print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
