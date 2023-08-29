squareNumbers = [0] * 10

for i in range(10):
    squareNumbers[i] = (i+1)**2

'''
for squareNumber in squareNumbers:
    print(squareNumber)
'''

[print(squareNumber) for squareNumber in squareNumbers]
