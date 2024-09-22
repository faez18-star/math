# Function to find and print all factors of a given number
def print_factors(number):
    # Printing the number for which we are finding factors
    print("The factors of", number, "are:")
    # Iterating through all numbers from 1 to the given number
    for i in range(1, number + 1):
        # Checking if 'i' is a factor of 'number'
        if number % i == 0:
            print(i)

# Taking input from the user
number = int(input("Enter a number to find its factors: "))

# Calling the function to print the factors of the number
print_factors(number)
