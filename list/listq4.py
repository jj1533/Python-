numlist=input("Enter numbers: ")
numbers=numlist.split()
a=[]
numbers=[int(num) for num in numbers]
for i in range(len(numbers)):
    if numbers[i]%2==0:
            a.append(numbers[i])
            a.sort()
print("Even Numbers: ",a)