# WRITE GROUP_ANAGRAMS FUNCTION HERE #
def group_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = "".join(sorted(string))
        if canonical not in anagrams:
            anagrams[canonical] = []
        anagrams[canonical].append(string)
    
    return [anagrams for canonical, anagrams in anagrams.items()]
######################################




print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
