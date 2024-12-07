listA = []
listB = []

with open('input/day1_input.txt', 'r') as file:
    for line in file:
        nums = line.split()
        
        listA.append(int(nums[0]))
        listB.append(int(nums[1]))
        
listA.sort()
listB.sort()

# Part 1
sumPart1 = 0
for x,y in zip(listA, listB):
    sumPart1 += abs(x-y)

# Part 2
sumPart2 = 0
for x in listA:
    sumPart2 += listB.count(x) * x


print(sumPart1)
print(sumPart2)