with open('input/day5_input.txt', 'r') as file:
    learn = True
    dataMap = {}
    sum = 0

    for line in file:
        # switch after ordering rules are done
        if line.strip() == "":
            learn = False
            continue

        # creating dictionary of ordering rules
        if learn:
            nums = list(map(int, line.split('|')))
            
            # dictionary where all values in list must be after the key
            if dataMap.get(nums[0], False):
                dataMap[nums[0]].append(nums[1])
            else:
                dataMap[nums[0]] = [nums[1]]
        
        else:
            nums = list(map(int, line.split(',')))
            # middle value
            middle = nums[len(nums) // 2] 
            correct = True

            # loop through list
            for i, x in enumerate(nums):
                # if no rule skip
                if dataMap.get(x, False):
                    # for all items in list before curr number
                    for y in range(0, i):
                        if nums[y] in dataMap[x]:
                            correct = False
                            break
                else:
                    continue
            
            if correct:
                sum += middle

    print(sum)
