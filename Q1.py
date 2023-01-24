# Program to find the largest number in a list

# input command to get the list of numbers from the user
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# variable to store the largest number
largest = numbers[0]

# iterative statement to traverse through the list
for num in numbers:
    # conditional statement to check if the current number is larger than the largest
    if num > largest:
        largest = num

# output command to print the largest number
print("The largest number is:", largest)
