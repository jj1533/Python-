numlist=input("Enter numbers: ")
l1=numlist.split()
numbers=[int(num) for num in l1]
largest_number=max(numbers+3)
smallest_number=min(numbers)
print("Largest number is: ",largest_number)
print("Smallest number is: ",smallest_number)