def isXMAS(x, m, a, s):
    if x == "X" and m == "M" and a == "A" and s == "S":
        return True
    return False

with open('input/day4_input.txt', 'r') as file:
    lines = file.readlines()

    count = 0
    # line by line
    for hIdx, line in enumerate(lines):
        # char by char
        for wIdx, letter in enumerate(line):
            # if not 'X' pass
            if letter != 'X':
                continue
            # left
            try:
                if wIdx > 2 and isXMAS(letter, line[wIdx-1], line[wIdx-2], line[wIdx-3]):
                    count += 1
            except IndexError:
                print ("not left")
            # right
            try:
                if isXMAS(letter, line[wIdx+1], line[wIdx+2], line[wIdx+3]):
                    count += 1
            except IndexError:
                print ("not right")
            # up
            try:
                if isXMAS(letter, lines[hIdx+1][wIdx], lines[hIdx+2][wIdx], lines[hIdx+3][wIdx]):
                    count += 1
            except IndexError:
                print ("not down")
            # down
            try:
                if hIdx > 2 and isXMAS(letter, lines[hIdx-1][wIdx], lines[hIdx-2][wIdx], lines[hIdx-3][wIdx]):
                    count += 1
            except IndexError:
                print ("not up")

            # diagonal left
            try:
                if hIdx > 2 and wIdx >2 and isXMAS(letter, lines[hIdx-1][wIdx-1], lines[hIdx-2][wIdx-2], lines[hIdx-3][wIdx-3]):
                    count += 1
            except IndexError:
                print ("not up left")
            # right
            try:
                if  hIdx > 2 and isXMAS(letter, lines[hIdx-1][wIdx+1], lines[hIdx-2][wIdx+2], lines[hIdx-3][wIdx+3]):
                    count += 1
            except IndexError:
                print ("not up right")
            # up
            try:
                if  wIdx > 2 and isXMAS(letter, lines[hIdx+1][wIdx-1], lines[hIdx+2][wIdx-2], lines[hIdx+3][wIdx-3]):
                    count += 1
            except IndexError:
                print ("not down left")
            # down
            try:
                if  isXMAS(letter, lines[hIdx+1][wIdx+1], lines[hIdx+2][wIdx+2], lines[hIdx+3][wIdx+3]):
                    count += 1
            except IndexError:
                print ("not down right")

            # if letter is an X, check 8 directions
        
        
    print('count: ', count)