with open('input/day3_input.txt', 'r') as file:
    # hold sum
    sum = 0

    # each line
    for line in file:

        # separate by multiply calls
        line = line.split('mul(')
        
        # for each multiply call
        for l in line:
            
            # split by comma, go through first argument
            l = l.split(',')
            
            # check first argument
            if l[0].isdigit():
                x = int(l[0])
                k = l[1].split(')')
                
                # check second argument
                if k[0].isdigit():
                    y = int(k[0])
                    sum += x*y
    print(sum)