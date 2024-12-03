##Check if each line is decreasing or increasing
##Check ifdecreasing or increasing in max steps of 3
##7 6 4 2 1 safe 'cause its decreasing in 2's
##1 2 7 8 9 unsafe 'cause it increased 2 -> 7 in 5 steps!
##1 3 2 4 5 unsafe 'cause it first increased then decreased!
##Each line is a report so chechk how many reports are safe!

##44 47 48 49 48
##64 66 68 69 71 72 72


rep_doc = open('2024_day_2_input.txt', 'r')

# def increasing():

# def decresing():


def part_one():
    line_num = ''; report = [];

    for line in rep_doc:
        for c in line:
            if(c != ' ' && c != 'c'):
                line_num = line_num + c
            else:
                print(line_num)
                line_num = ''
        print(report)
        report = []
        

part_one()