# O(n logn) time | O(1) space
# n: the number of students
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True) # O(n logn)
    blueShirtHeights.sort(reverse=True) # O(n logn)

    shirtColorInFirstRow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"

    for idx in range(len(redShirtHeights)): # O(n)
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False

    return True
