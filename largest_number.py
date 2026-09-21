# Ask user for a random number.

a = int(input("Choose a random number: "))
b = int(input("Choose a random number: "))
c = int(input("Choose a random number: "))

# Check if a is greater than b and c.

if a > b and a > c:

    print("a is the largest number") # a is confirmed to be the largest number.

# Check if b is greater than a and c.

elif b > a and b > c:
    
    print("b is the largest number") # b is confirmed to be the largest number.
    
# If neither a and b are largest then, c must be the largest number.

else:
    
    print("c is the largest number") 
