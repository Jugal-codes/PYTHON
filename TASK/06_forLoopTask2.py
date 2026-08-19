# Practice Qs 1 - Find the Sum and Average of List Elements
numbers = [5, 10, 15, 20, 25]
total = 0

for n in numbers:
    total += n 

avg = total / len(numbers)

print("Sum:", total)
print("Average:", avg)


# Practice Qs 2 - Find the Maximum and Minimum Number
nums = [12, 45, 23, 67, 34]
max_val = nums[0]
min_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Maximum:", max_val)
print("Minimum:", min_val)



# Practice Qs 3 - Reverse a List Without Using reverse()
list = [10, 20, 30, 40, 50]
rev = []

for i in range(len(list)-1, -1, -1): 
    rev.append(list[i])

print("Reversed List:", rev)



# Practice Qs 4 - Find Even and Odd Numbers from a List
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []

for n in nums:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Even Numbers:", even)
print("Odd Numbers:", odd)



# Practice Qs 5 - Remove Duplicates from a List
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Without Duplicates:", unique)




# Practice Qs 6 - Find Common Elements Between Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements:", common)




# Practice Qs 7 - Flatten a Nested List
nested = [[1, 2], [3, 4], [5, 6]]
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print("Flattened List:", flat)



# Practice Qs 8 - Remove All Even Numbers from a List
nums = [10, 15, 20, 25, 30, 35]
result = []

for n in nums:
    if n % 2 != 0:
        result.append(n)

print("After Removing Even:", result)




# Practice Qs 9 - Find All Elements Greater Than a Given Value
nums = [5, 10, 15, 20, 25, 30]
limit = 15
greater = []

for n in nums:
    if n > limit:
        greater.append(n)

print("Numbers greater than", limit, ":", greater)




# Practice Qs 10 - Find Elements Present in One List but Not in the Other
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
diff = []

for i in list1:
    if i not in list2:
        diff.append(i)
for j in list2:
    if j not in list1:
        diff.append(j)

print("Unique Elements:", diff)




# Practice Qs 11 - Sort a List in Ascending Order
nums = [5, 2, 9, 1, 7]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap

print("Sorted List:", nums)



# Practice Qs 12 - Check if a List is a Palindrome
list = [1, 2, 3, 2, 1]
rev = []

for i in range(len(list) - 1, -1, -1):
    rev.append(list[i])

if list == rev:
    print("Palindrome List")
else:
    print("Not a Palindrome")




# Practice Qs 13 - Find All Unique Elements in a List
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []

for n in nums:
    if nums.count(n) == 1:
        unique.append(n)

print("Unique Elements:", unique)




# Practice Qs  14 - Move All Zeros to the End
nums = [0, 1, 0, 2, 3, 0, 4]
result = []

for n in nums:
    if n != 0:
        result.append(n)

# count zeros
zeros = nums.count(0)
for _ in range(zeros):
    result.append(0)

print("After Moving Zeros:", result)

