prev_array = [1 for x in range(26)]
next_array = [1 for x in range(26)]

gettingInput = True
n = 0
while gettingInput:
    try:
        n = int(input("Enter a value for n (1 - 300): "))
    except:
        print("Invalid input")
    else:
        if n <= 0 or n > 300:
            print("Invalid input")
        else:
            gettingInput = False

for i in range(n):
    next_array[0] = prev_array[1] * 4
    next_array[1] = prev_array[9] + prev_array[2]*2
    next_array[2] = prev_array[4] + prev_array[5] + prev_array[3]
    next_array[3] = prev_array[6] + prev_array[7]
    next_array[4] = prev_array[10] + prev_array[11] + prev_array[8]
    next_array[5] = prev_array[4] + prev_array[13] + prev_array[12]
    next_array[6] = prev_array[10] + prev_array[11] + prev_array[4]
    next_array[7] = prev_array[4] + prev_array[13] + prev_array[15]
    next_array[8] = prev_array[4] + prev_array[17] + prev_array[16]
    next_array[9] = prev_array[10] + prev_array[18] * 2
    next_array[10] = prev_array[10] + prev_array[19] * 2
    next_array[11] = prev_array[4] + prev_array[17] + prev_array[20]
    next_array[12] = prev_array[6] + prev_array[7]
    next_array[13] = prev_array[4] + prev_array[13] + prev_array[21]
    next_array[14] = prev_array[4] + prev_array[17]
    next_array[15] = prev_array[6] + prev_array[7]
    next_array[16] = prev_array[7]
    next_array[17] = prev_array[4] + prev_array[13] + prev_array[22]
    next_array[18] = prev_array[4] + prev_array[17] + prev_array[23]
    next_array[19] = prev_array[4] + prev_array[17] + prev_array[24]
    next_array[20] = prev_array[25] + prev_array[7]
    next_array[21] = prev_array[6] + prev_array[7]
    next_array[22] = prev_array[6] + prev_array[7]
    next_array[23] = prev_array[25] + prev_array[7]
    next_array[24] = prev_array[25] + prev_array[7]
    next_array[25] = prev_array[10] + prev_array[11]

    prev_array = next_array.copy()
    
print("Number of strings of length", n, "with no cycles length 6 or less:", prev_array[0])