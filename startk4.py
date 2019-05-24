
EMPTY, L, R, U, D, LU, LD, RU, RD, UL, UR, DL, DR, LUR, LDR, RUL, RDL, ULD, URD, DLU, DRU = 0, 1, 2, 3,\
    4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

prev_array = [1 for x in range(21)]
next_array = [1 for x in range(21)]

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
    next_array[EMPTY] = prev_array[L] + prev_array[R] + prev_array[U] + prev_array[D]
    next_array[L] = prev_array[L] + prev_array[LU] + prev_array[LD]
    next_array[R] = prev_array[R] + prev_array[RU] + prev_array[RD]
    next_array[U] = prev_array[UL] + prev_array[UR] + prev_array[U]
    next_array[D] = prev_array[DL] + prev_array[DR] + prev_array[D]
    next_array[LU] = prev_array[UL] + prev_array[LUR] + prev_array[U]
    next_array[LD] = prev_array[DL] + prev_array[LDR] + prev_array[D]
    next_array[RU] = prev_array[RUL] + prev_array[UR] + prev_array[U]
    next_array[RD] = prev_array[RDL] + prev_array[DR] + prev_array[D]
    next_array[UL] = prev_array[L] + prev_array[LU] + prev_array[ULD]
    next_array[UR] = prev_array[R] + prev_array[RU] + prev_array[URD]
    next_array[DL] = prev_array[L] + prev_array[DLU] + prev_array[LD]
    next_array[DR] = prev_array[R] + prev_array[DRU] + prev_array[RD]
    next_array[LUR] = prev_array[R] + prev_array[RU]
    next_array[LDR] = prev_array[R] + prev_array[RD]
    next_array[RUL] = prev_array[L] + prev_array[LU]
    next_array[RDL] = prev_array[L] + prev_array[LD]
    next_array[ULD] = prev_array[DL] + prev_array[D]
    next_array[URD] = prev_array[DR] + prev_array[D]
    next_array[DLU] = prev_array[UL] + prev_array[U]
    next_array[DRU] = prev_array[UR] + prev_array[U]
    prev_array = next_array.copy()
    
print("Number of strings of length", n, "with no cycles length 4 or less:", prev_array[0])


EMPTY, ONE, TWO, THREE, W = 0, 1, 2, 3, 4
prev_array = [1 for x in range(5)]
next_array = [1 for x in range(5)]

for i in range(n):
    next_array[EMPTY] = prev_array[ONE] * 4
    next_array[ONE] = prev_array[ONE] + prev_array[THREE] * 2
    next_array[TWO] = prev_array[ONE] + prev_array[THREE]
    next_array[THREE] = prev_array[ONE] + prev_array[THREE] + prev_array[TWO]
    prev_array = next_array.copy()

print("Number of strings of length", n, "with no cycles length 4 or less:", prev_array[0])