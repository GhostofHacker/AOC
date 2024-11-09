#You got a calibration document but due to a artistic elv document cant no longer be readable. 
#You gotta fix it.
#First and last digits are number to be put togather to find calibration value.
#Such as first line equals to 98 and second 55 and so and so
#In the end total of this numbers will give you the calibration value.
#two1nine 11

import re

cal_doc = open('2023_day_1_input.txt', 'r')

def part_one():
    total = 0; currentLineNumbers = []; number = 0
    for line in cal_doc:
        for char in line:
            if char.isdigit():
                currentLineNumbers.append(char)
        if len(currentLineNumbers) > 1:
            number = int(currentLineNumbers[0] + currentLineNumbers[-1])
        else:
            number = int(currentLineNumbers[0] + currentLineNumbers[0])
        print("Current line number is: " , number)
        total += number
        currentLineNumbers = []; number = 0
    print("Total is: ", total)

#Oops! Well you also need to check the words for digits!
#two1nine 2 and 9 29!
#4nineeightseven2 42!
def part_two():
    total = 0; number = 0; numITR = 0
    lookUpTable = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',]
    for line in cal_doc:
        matchedNumber = re.findall('(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))', line)
        for num in matchedNumber:
            if num.isdigit() == False:
                for i in range(0, 9):
                    if num == lookUpTable[i]:
                        matchedNumber[numITR] = str(i+1)
                        numITR = numITR + 1
            else:
                numITR = numITR + 1
        numITR = 0
        if len(matchedNumber) > 1:
            number = int(matchedNumber[0] + matchedNumber[-1])
        else:
            number = int(matchedNumber[0] + matchedNumber[0])
        total += number
        number = 0
    print("Total is: ", total)

part_two()