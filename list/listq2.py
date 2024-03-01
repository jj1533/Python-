numlist=input("Enter numbers: ")
l1=numlist.split()
numbers=[int(num) for num in l1]
l=len(numbers)
numbers.sort(reverse=True)

if l>=3:
    third_largest=numbers[2]


print("3rd Largest number is: ",third_largest)
