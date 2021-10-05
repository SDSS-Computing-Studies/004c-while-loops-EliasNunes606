#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
integer = ""
incorrectinteger = True
while incorrectinteger:
    integer = float(input("Enter number: "))
    integer = integer / 2
    if integer != int(integer):
        print("That is not an even integer: ")
    else:
        incorrectinteger = False

print("That is an even integer") 