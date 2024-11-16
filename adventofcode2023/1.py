import os


def readFirstAndLastDigit(str):
    l, r = 0, len(str)-1
    firstDigit, lastDigit = "", ""
    while l <= r:
        if firstDigit and lastDigit:
            break
        if not firstDigit:
            if not str[l].isdigit():
                l+=1
            else:
                firstDigit = str[l]
        if not lastDigit:
            if not str[r].isdigit():
                r-=1
            else:
                lastDigit = str[r]
    
    if not firstDigit and not lastDigit:
        return 0
    
    return int(firstDigit+lastDigit)

def main():
    res=0
    base_path = os.path.dirname(__file__)  # Directory of the current script
    relative_path = "input_data/1.txt"
    file_path = os.path.join(base_path, relative_path)
    with open(file_path) as f:
        for line in f:
            res += readFirstAndLastDigit(line.strip())
    return res

print(main())