def safeLevel(report):
    fail = False
    last = 0
    remove = -1
    increase = True if (report[0] - report[1]) < 0 else False
    # level loop
    for index, level in enumerate(report):
        if last == 0:
            last = level
            continue

        diff = last - level  # the difference between levels
        
        # if increasing
        if increase:
            # ensure increasing or difference is in range
            if diff >= 0 or diff < -3:
                fail = True
                remove = index - 1
                break
        # else decreasing
        else:
            # ensure decreasing or difference is in range
            if diff <= 0 or diff > 3:
                fail = True
                remove = index - 1
                break

        # update last
        last = level
    return fail, remove 

with open('input/day2_input.txt', 'r') as file:
       # Read all lines from the file
    lines = file.readlines()

    # Convert each line to a list of integers
    reports = []
    for line in lines:
        # Split the line by spaces (or other delimiters like commas) and convert each part to an integer
        reports.append([int(num) for num in line.split()])

# safe reports count
safe = 0

# report loop
for report in reports:
    fail, remove = safeLevel(report)

    if fail:
        try:
            report.pop(remove)
            fail2, remove2 = safeLevel(report)
            if not fail2:
                safe += 1
        except IndexError:
            print("Index OB")

    if not fail:
        safe += 1

print(safe)
