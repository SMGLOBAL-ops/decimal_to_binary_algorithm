
# aim is to be able to convert any input "decimal" format e.g. 0, 1, 4, 13 etc ... -> binary format i.e. 0, 1, 001, 1101 etc ...

def decimal_to_binary(w):
    b = []

    if w == 0:
        b.append(0)
        print(b)
        return b
    else:
        while w > 0:
            if w % 2 != 0:
                b.insert(0, 1)
                w = (w - 1) / 2
            elif w % 2 == 0:
                b.insert(0, 0)
                w = w / 2

            if w == 0:
                print(b)
                return b
            else:
                continue
           
for i in range(0, 16):
    print(f'For value, {i}, binary equivalent is: ')
    decimal_to_binary(i)
